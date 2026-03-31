#!/usr/bin/env python3
"""
Save SEO audit markdown files to Google Docs.

Usage:
    python save_to_google_docs.py audits/jakescarpetcleaning-seo-audit.md
    python save_to_google_docs.py audits/integrityexteriorsolutions-seo-audit.md
    python save_to_google_docs.py --all

Authentication:
    This script uses OAuth 2.0. On first run it will open a browser window
    to authorize access to your Google account. A token is cached in
    token.json for subsequent runs.

    To set up credentials:
    1. Go to https://console.cloud.google.com/
    2. Create a project (or select an existing one)
    3. Enable the Google Docs API and Google Drive API
    4. Create OAuth 2.0 credentials (Desktop app type)
    5. Download the credentials JSON and save as credentials.json
       in this directory

    Required scopes:
    - https://www.googleapis.com/auth/documents
    - https://www.googleapis.com/auth/drive.file
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except ImportError:
    print("Missing dependencies. Install with:")
    print("  pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client")
    sys.exit(1)

SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive.file",
]

CREDENTIALS_FILE = Path(__file__).parent / "credentials.json"
TOKEN_FILE = Path(__file__).parent / "token.json"
AUDITS_DIR = Path(__file__).parent / "audits"


def authenticate() -> Credentials:
    """Authenticate with Google and return credentials."""
    creds = None

    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CREDENTIALS_FILE.exists():
                print(f"ERROR: credentials.json not found at {CREDENTIALS_FILE}")
                print()
                print("To set up Google credentials:")
                print("  1. Go to https://console.cloud.google.com/")
                print("  2. Enable Google Docs API and Google Drive API")
                print("  3. Create OAuth 2.0 credentials (Desktop app type)")
                print("  4. Download credentials JSON as: credentials.json")
                sys.exit(1)

            flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_FILE), SCOPES)
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    return creds


def parse_markdown_to_requests(content: str) -> list[dict]:
    """
    Convert markdown content to Google Docs API batchUpdate requests.
    Handles: H1/H2/H3 headings, bold, tables, bullet lists, horizontal rules.
    """
    requests = []
    current_index = 1  # Google Docs body starts at index 1

    def insert_text(text: str, style: str = "NORMAL_TEXT") -> list[dict]:
        nonlocal current_index
        reqs = []
        end_index = current_index + len(text)

        reqs.append({
            "insertText": {
                "location": {"index": current_index},
                "text": text,
            }
        })

        if style != "NORMAL_TEXT":
            reqs.append({
                "updateParagraphStyle": {
                    "range": {"startIndex": current_index, "endIndex": end_index},
                    "paragraphStyle": {"namedStyleType": style},
                    "fields": "namedStyleType",
                }
            })

        current_index = end_index
        return reqs

    lines = content.split("\n")

    for line in lines:
        stripped = line.rstrip()

        # Headings
        if stripped.startswith("### "):
            text = stripped[4:] + "\n"
            requests.extend(insert_text(text, "HEADING_3"))
        elif stripped.startswith("## "):
            text = stripped[3:] + "\n"
            requests.extend(insert_text(text, "HEADING_2"))
        elif stripped.startswith("# "):
            text = stripped[2:] + "\n"
            requests.extend(insert_text(text, "HEADING_1"))
        # Horizontal rule — render as a blank line with a visual separator
        elif stripped == "---":
            requests.extend(insert_text("\n"))
        # Bullet list items
        elif stripped.startswith("- ") or stripped.startswith("* "):
            text = stripped[2:] + "\n"
            requests.extend(insert_text(text))
            # Apply list style
            end_index = current_index
            start_index = end_index - len(text)
            requests.append({
                "createParagraphBullets": {
                    "range": {"startIndex": start_index, "endIndex": end_index},
                    "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE",
                }
            })
        # Table rows (simplified — render as normal text preserving | chars)
        elif stripped.startswith("|") and stripped.endswith("|"):
            # Skip separator rows like |---|---|
            if re.match(r"^\|[-| :]+\|$", stripped):
                continue
            # Convert table row to tab-separated text
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            text = "  |  ".join(cells) + "\n"
            requests.extend(insert_text(text))
        # Numbered list
        elif re.match(r"^\d+\. ", stripped):
            text = re.sub(r"^\d+\. ", "", stripped) + "\n"
            requests.extend(insert_text(text))
            end_index = current_index
            start_index = end_index - len(text)
            requests.append({
                "createParagraphBullets": {
                    "range": {"startIndex": start_index, "endIndex": end_index},
                    "bulletPreset": "NUMBERED_DECIMAL_ALPHA_ROMAN",
                }
            })
        # Bold text inline — strip markdown bold markers for plain insertion
        elif "**" in stripped:
            text = re.sub(r"\*\*(.*?)\*\*", r"\1", stripped) + "\n"
            requests.extend(insert_text(text))
        # Empty line
        elif stripped == "":
            requests.extend(insert_text("\n"))
        # Normal paragraph
        else:
            text = stripped + "\n"
            requests.extend(insert_text(text))

    return requests


def create_google_doc(creds: Credentials, title: str, markdown_content: str) -> str:
    """Create a new Google Doc with the given title and markdown content. Returns the doc URL."""
    try:
        docs_service = build("docs", "v1", credentials=creds)
        drive_service = build("drive", "v3", credentials=creds)

        # Create empty document
        doc = docs_service.documents().create(body={"title": title}).execute()
        doc_id = doc.get("documentId")

        print(f"  Created document: {title}")
        print(f"  Document ID: {doc_id}")

        # Build update requests from markdown
        requests = parse_markdown_to_requests(markdown_content)

        if requests:
            docs_service.documents().batchUpdate(
                documentId=doc_id,
                body={"requests": requests},
            ).execute()

        # Make the document viewable by anyone with the link (optional)
        drive_service.permissions().create(
            fileId=doc_id,
            body={"type": "anyone", "role": "reader"},
        ).execute()

        doc_url = f"https://docs.google.com/document/d/{doc_id}/edit"
        return doc_url

    except HttpError as e:
        print(f"  ERROR: Google API error: {e}")
        raise


def save_audit_to_docs(audit_path: Path) -> str:
    """Read an audit markdown file and save it to Google Docs. Returns the doc URL."""
    if not audit_path.exists():
        print(f"ERROR: File not found: {audit_path}")
        sys.exit(1)

    content = audit_path.read_text(encoding="utf-8")

    # Use the first H1 line as the document title
    title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
    title = title_match.group(1) if title_match else audit_path.stem

    print(f"\nSaving: {audit_path.name}")
    print(f"  Title: {title}")

    creds = authenticate()
    url = create_google_doc(creds, title, content)

    print(f"  URL: {url}")
    return url


def main():
    parser = argparse.ArgumentParser(
        description="Save SEO audit markdown files to Google Docs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="Audit markdown file(s) to upload",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Upload all .md files in the audits/ directory",
    )
    args = parser.parse_args()

    if args.all:
        audit_files = sorted(AUDITS_DIR.glob("*.md"))
        if not audit_files:
            print(f"No .md files found in {AUDITS_DIR}")
            sys.exit(1)
    elif args.files:
        audit_files = [Path(f) for f in args.files]
    else:
        parser.print_help()
        sys.exit(1)

    results = {}
    for audit_file in audit_files:
        url = save_audit_to_docs(audit_file)
        results[audit_file.name] = url

    print("\n" + "=" * 60)
    print("Done! Google Docs links:")
    for filename, url in results.items():
        print(f"  {filename}")
        print(f"    {url}")


if __name__ == "__main__":
    main()
