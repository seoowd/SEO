# SEO Audit: Integrity Exterior Solutions
**Website:** integrityexteriorsolutions.com
**Audit Date:** March 31, 2026
**Business Type:** Local Service — Roofing, Gutters, Siding, Windows (Exterior Contractor)
**Location:** Lincoln, NE | Also serves Omaha and southeast Nebraska
**Contact:** 402-730-3077 | info@integrityexteriorsolutions.com

---

## Executive Summary

Integrity Exterior Solutions has a solid SEO foundation — the homepage title is well-optimized for their primary keyword, they have FAQ pages, service area pages, and a reasonable number of indexed pages. However, there are several structural problems hurting performance: two nearly-identical Lincoln location pages creating keyword cannibalization, a WordPress media attachment page being indexed, weak service sub-page titles, and a site that's functionally focused on roofing while offering 7+ services that aren't getting equal SEO attention.

**Overall SEO Health: 6/10 — Good foundation, fixable issues**

### Top 3 Priority Issues
1. **Duplicate Lincoln location pages** — `/lincoln-ne/` and `/service-areas/lincoln-ne/` compete against each other with near-identical content
2. **WordPress attachment page indexed** — `/home/screen-shot-2018-01-25-at-3.35.58-pm/` is a media page indexed in Google, wasting crawl budget and diluting the site
3. **Service sub-pages have weak titles** — "Roofing Services - Lincoln" and "Services - Integrity Exterior Solutions" are underoptimized for keyword targeting

### Quick Wins
- Add canonical or noindex to one of the duplicate Lincoln pages (30 min)
- Noindex WordPress attachment pages via plugin (15 min with Yoast/RankMath)
- Rewrite title tags for Roofing, Gutters, Siding, Windows service pages (1 hr)

---

## Technical SEO Findings

### 1. Duplicate Location Pages (Keyword Cannibalization)
- **Issue:** Two pages target "Lincoln NE" with near-identical content:
  - `/lincoln-ne/` — Title: "Lincoln, NE - Integrity Exterior Solutions"
  - `/service-areas/lincoln-ne/` — Title: "Lincoln, NE – Integrity Exterior Solutions"
- **Impact:** HIGH — Google can't determine which page to rank, so it may rank neither, or alternate between them, suppressing both. This splits link equity and dilutes authority.
- **Evidence:** Both titles visible in `site:integrityexteriorsolutions.com` search results
- **Fix:** Pick one canonical Lincoln page (recommend `/service-areas/lincoln-ne/` for URL structure consistency). Add `<link rel="canonical">` pointing from `/lincoln-ne/` to `/service-areas/lincoln-ne/`, OR 301 redirect `/lincoln-ne/` to `/service-areas/lincoln-ne/`. Differentiate content if keeping both.
- **Priority:** Critical

### 2. WordPress Media Attachment Page Indexed
- **Issue:** `integrityexteriorsolutions.com/home/screen-shot-2018-01-25-at-3.35.58-pm/` is appearing in Google's index
- **Impact:** HIGH — This is a WordPress media attachment page with no SEO value. It:
  - Wastes crawl budget
  - Dilutes overall site quality signals
  - Sends "thin content" signals to Google
- **Fix:** If using Yoast SEO: Settings → Search Appearance → Media → redirect media attachments to parent post. Or add `noindex` to all attachment pages. Then request removal via Google Search Console.
- **Priority:** Critical

### 3. Site Architecture — Two Location Hierarchies Exist
- **Issue:** The site has both `/lincoln-ne/` (flat) and `/service-areas/lincoln-ne/` (nested under service-areas). This inconsistency suggests the site-area structure was added later as an afterthought.
- **Impact:** Medium — Inconsistent URL structure confuses crawlers and dilutes link equity
- **Fix:** Standardize all city pages under `/service-areas/[city-name]/`. Redirect any orphan city pages to the proper nested structure.
- **Priority:** High

### 4. Robots.txt & Sitemap — Unconfirmed
- **Issue:** Cannot confirm sitemap submission and robots.txt from this audit
- **Fix:** Verify `integrityexteriorsolutions.com/robots.txt` and confirm sitemap is at `/sitemap.xml` and submitted to Google Search Console. Ensure the attachment page URL is blocked or removed.
- **Priority:** High

### 5. Page Speed / Core Web Vitals — Unverified
- **Issue:** Site not tested via PageSpeed Insights in this audit
- **Fix:** Run `https://pagespeed.web.dev/` for both mobile and desktop. Priority targets: LCP < 2.5s, CLS < 0.1, INP < 200ms. Common issues for WordPress roofing sites: large uncompressed hero images, render-blocking scripts.
- **Priority:** High

---

## On-Page SEO Findings

### 6. Homepage Title — Decent, But Roofing-Only Focus
- **Current:** `"Roofing Companies Lincoln NE | Best Lincoln Roofers | Integrity Exterior Solutions"`
- **Assessment:** Good — includes primary keyword and location. However, it only signals roofing. The business also offers gutters, siding, and windows.
- **Impact:** Low-Medium — Homepage is likely ranking for roofing terms already; this is a polish item
- **Recommendation:** Consider testing: `"Roofing, Gutters & Siding in Lincoln NE | Integrity Exterior Solutions"` — but do not change without benchmarking current rankings first.
- **Priority:** Low (don't fix what's working)

### 7. Roofing Service Page Title — Too Short/Weak
- **Current:** `"Roofing Services - Lincoln"`
- **Impact:** HIGH — This page should be a major organic traffic driver but the title is thin
- **Fix:** `"Roofing Installation & Replacement in Lincoln, NE | Integrity Exterior Solutions"`
- **Priority:** High

### 8. Services Overview Page Title — Generic
- **Current:** `"Services - Integrity Exterior Solutions"`
- **Impact:** Medium — Generic title won't rank for anything specific
- **Fix:** `"Exterior Services in Lincoln, NE: Roofing, Gutters, Siding & Windows"`
- **Priority:** Medium

### 9. Service Sub-Pages — No Evidence of Gutters, Siding, Windows Pages with Good Titles
- **Issue:** From indexed results, only `/services/roofing/` has a visible service sub-page. Gutters, siding, and windows pages aren't appearing (or have weak titles)
- **Impact:** HIGH — Each service is a separate keyword cluster with significant local search volume
  - "gutter installation Lincoln NE" — separate page needed
  - "vinyl siding Lincoln NE" — separate page needed
  - "window replacement Lincoln NE" — separate page needed
- **Fix:** Ensure each service has a dedicated page with a strong title:
  - `"Gutter Installation & Replacement in Lincoln, NE | Integrity Exterior Solutions"`
  - `"Vinyl Siding Installation in Lincoln, NE | Integrity Exterior Solutions"`
  - `"Window Replacement in Lincoln, NE | Integrity Exterior Solutions"`
- **Priority:** High

### 10. FAQ Pages — Good Structure (Keep & Expand)
- **Issue:** The site has `/faqs/roofing-faqs/`, `/faqs/gutter-faqs/`, `/faqs/vinyl-siding-faqs/` — this is excellent for long-tail keyword capture
- **Impact:** Positive — FAQ pages rank well for question-based searches and can earn Google's "People Also Ask" features
- **Fix:** Keep these. Add FAQ schema markup (JSON-LD). Add FAQ pages for windows and garage construction. Ensure each FAQ links back to the relevant service page.
- **Priority:** Medium (enhancement)

### 11. Meta Descriptions — Unverified Quality
- **Issue:** Meta descriptions were inferred from page content in search snippets — actual written meta descriptions may be missing or auto-generated
- **Fix:** Write unique, click-optimized meta descriptions for every page. Include: primary keyword, location, differentiated value prop (GAF certified, free inspections, insurance claims).
  - Homepage: `"Lincoln's most trusted roofing, gutter, siding & window contractor. GAF certified. Free inspections & insurance claim help. Call 402-730-3077."`
- **Priority:** High

### 12. Free Roof Inspections Page — Long, Unoptimized Title
- **Current:** `"Free Roof Inspections Lincoln and Omaha areas, Nebraska - Integrity Exterior Solutions"`
- **Assessment:** Decent keyword inclusion, but very long (72+ characters — gets truncated in SERP)
- **Fix:** `"Free Roof Inspections in Lincoln & Omaha, NE | Integrity Exterior Solutions"`
- **Priority:** Low-Medium

---

## Content Quality Assessment

### 13. Service Pages Need More Depth
- **Issue:** From search snippet previews, service pages likely cover the basics but may not match the content depth of top competitors
- **Impact:** Medium — For competitive local service terms, content depth matters
- **Fix:** Each service page should include: process overview, materials/brands used (GAF for roofing), common problems solved, Nebraska weather context, FAQs section, before/after, and a clear CTA
- **Priority:** Medium

### 14. Blog / Content — Limited Evidence
- **Issue:** One blog post is indexed: `/best-practices-for-new-construction-roofing-in-lincoln-ne/` — suggests a blog exists but is not regularly updated
- **Impact:** Medium — A consistent blog targeting seasonal and storm-related queries would drive significant traffic (e.g., "hail damage roof repair Lincoln NE," "how to tell if roof needs replacement")
- **Fix:** Publish 2–3 blog posts/month. Priority topics:
  - "Signs your roof was damaged by hail in Nebraska"
  - "How long does a roof replacement take in Lincoln?"
  - "GAF vs. CertainTeed shingles: which is better for Nebraska weather?"
- **Priority:** Medium

### 15. Insurance Claim Assistance — Strong Differentiator
- **Issue:** The site mentions insurance claim assistance, which is a high-conversion differentiator — but may not have a dedicated page
- **Fix:** Create `/insurance-claim-roofing-lincoln-ne/` — this is a high-intent search term homeowners use after storm damage
- **Priority:** High

---

## Local SEO Findings

### 16. Google Business Profile — Verify Multi-Service Optimization
- **Issue:** Cannot confirm GBP optimization from website audit alone; the business has 19 Yelp reviews (low)
- **Impact:** HIGH — GBP is critical for "roofing company near me" searches
- **Fix:**
  - Ensure all 7+ services are listed in GBP (roofing, gutters, siding, windows, garage, snow removal, dumpster rental)
  - Upload 20+ photos (installs, team, before/after)
  - Respond to all reviews
  - Post monthly updates with seasonal offers
  - Add Q&A answers to common questions
- **Priority:** Critical

### 17. Review Volume — Low on Yelp (19 Reviews)
- **Issue:** Only 19 Yelp reviews; Google review count unknown from this audit
- **Impact:** High — Low review volume weakens local pack ranking signals. Competitors with 100+ reviews will outrank.
- **Fix:** Implement an active review request workflow. After every job: send a follow-up text/email with a direct link to leave a Google review. Target: 5+ new reviews per month.
- **Priority:** High

### 18. NAP Consistency — Verify
- **Issue:** Business address: 1524 Pioneers Blvd, Lincoln, NE 68502 | Phone: 402-730-3077
- **Fix:** Audit all citations (Google, Yelp, BBB, Angi, Houzz, Networx, HomeAdvisor) for exact NAP match. The BBB listing and Yelp listing should match the website exactly.
- **Priority:** High

### 19. Schema Markup — Likely Missing or Incomplete
- **Issue:** No JSON-LD schema markup confirmed (JS-rendered schema cannot be verified via static audit)
- **Fix:** Add the following schema types:
  - `LocalBusiness` / `RoofingContractor` on homepage
  - `Service` schema on each service page
  - `FAQPage` schema on all FAQ pages
  - `BreadcrumbList` for site navigation
  - `AggregateRating` if reviews are displayed on-site
- **Priority:** High

### 20. Service Area Pages — Good Foundation, Expand
- **Issue:** Lincoln and Omaha pages exist. The first search result also mentions Ashland, Waverly, and southeast Nebraska.
- **Fix:** Create dedicated `/service-areas/` pages for:
  - Omaha, NE (likely exists)
  - Bellevue, NE
  - Papillion, NE
  - Gretna, NE
  - Waverly, NE
  - Ashland, NE
  Each needs unique content (not just swapped city name).
- **Priority:** Medium

---

## Prioritized Action Plan

### Critical (Do First — Structural Issues)
1. Resolve Lincoln page duplication: 301 redirect `/lincoln-ne/` → `/service-areas/lincoln-ne/`
2. Noindex all WordPress attachment pages (Yoast/RankMath setting)
3. Request removal of attachment page URL from Google Search Console
4. Verify and fully optimize Google Business Profile

### High Impact (Do Next)
5. Rewrite service page title tags: roofing, gutters, siding, windows
6. Write meta descriptions for all pages (include location + differentiator)
7. Create dedicated `/insurance-claim-roofing-lincoln-ne/` page
8. Add LocalBusiness + FAQPage schema markup
9. Implement review request workflow (text/email after every job)
10. Audit NAP consistency across all directories

### Quick Wins (Easy, Immediate Benefit)
11. Add FAQ schema to existing FAQ pages
12. Update blog post to link to service pages (internal linking)
13. Verify sitemap is submitted to Google Search Console
14. Add structured breadcrumbs to service area pages

### Long-Term Recommendations
15. Consistent blog: 2–3 posts/month on storm damage, seasonal roofing, Nebraska weather topics
16. Expand service area pages for Bellevue, Papillion, Gretna, Waverly
17. Create insurance claim landing page targeting storm/hail damage searches
18. Build backlinks from Lincoln Chamber of Commerce, Nebraska Contractors Association, local news coverage

---

## Summary Score Card

| Area | Score | Notes |
|------|-------|-------|
| Technical SEO | 5/10 | Duplicate pages, attachment page indexed |
| Title Tags | 6/10 | Homepage good, service pages weak |
| Meta Descriptions | 5/10 | Likely auto-generated on service pages |
| Content | 6/10 | FAQ pages are strong; blog underutilized |
| Local SEO | 6/10 | GBP unverified; low review volume on Yelp |
| E-E-A-T | 7/10 | Since 2009, GAF certified, owner named (Tom Buck) |
| **Overall** | **6/10** | **Solid foundation, fixable structural issues** |
