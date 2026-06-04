# SEO Audit — T26 Design Build

**Website:** https://www.t26designbuild.com/
**Prepared for:** T26 Design Build Co.
**Date:** June 4, 2026
**Data source:** Screaming Frog crawl (15 indexable HTML pages)

---

## 1. Executive Summary

The site is technically healthy at the foundation level — every page returns a clean `200 OK`, all pages are indexable, and canonical tags are correctly self-referencing. There are no broken pages, redirect chains, or `noindex` problems.

However, the audit surfaced several **on-page and content issues that are likely holding back rankings**, especially on the money pages (kitchen, bathroom, home, and landscape remodeling). The two biggest issues:

1. **Missing H1 tags on 6 of the most important pages**, including the homepage.
2. **A leftover WordPress placeholder meta description on the homepage** ("Just another construction site"), which looks unprofessional in search results and wastes the highest-value snippet on the site.

Site speed is also a concern — several pages have very slow server response times.

**Overall health: 6.5 / 10** — solid technical base, but clear, fixable on-page gaps.

---

## 2. Priority Issues (Fix First)

### 🔴 Homepage meta description is a placeholder
The homepage meta description currently reads **"Just another construction site"** — the default WordPress tagline. This is the single most damaging issue found. It appears in Google results and actively hurts click-through and credibility.

> **Fix:** Write a compelling, keyword-rich description, e.g.
> *"T26 Design Build Co. delivers expert home, kitchen, bathroom & landscape remodeling in Phoenix, Scottsdale & Chandler. Book your free estimate today."* (~150 chars)

### 🔴 Missing H1 tags on 6 key pages
The following pages have **no H1**, which weakens topical relevance for their target keywords:

| Page | Target intent |
|------|---------------|
| Homepage | Brand / Phoenix remodeling |
| /home-remodeling-in-phoenix/ | Home remodeling Phoenix |
| /kitchen-remodel-phoenix/ | Kitchen remodel Phoenix |
| /bathroom-remodel-phoenix/ | Bathroom remodel Phoenix |
| /landscape-design-phoenix/ | Landscape design Phoenix |
| /remodel-service/ | Phoenix remodeling services |

These pages currently lead with an H2 instead. Promote the lead heading to an `<h1>` containing the primary keyword (e.g., *"Kitchen Remodeling in Phoenix & Scottsdale"*).

### 🔴 Homepage title is too short / under-optimized
Title is just **"T26 Design Build"** (16 characters). It uses none of the available space and no service or location keywords.

> **Fix:** *"Phoenix Home Remodeling & Design Build Contractor | T26"* (~50–55 chars)

---

## 3. Medium-Priority Issues

### 🟠 Meta descriptions too long (will be truncated)
Six pages exceed the ~155–160 character limit and get cut off in search results:

| Page | Length |
|------|--------|
| /remodel-service/ | 341 |
| /contact-us/ | 323 |
| /kitchen-remodel-phoenix/ | 307 |
| /landscape-design-phoenix/ | 291 |
| /about-us/ | 269 |
| /our-work/ | 259 |

Trim each to a tight, single-sentence summary with a call to action. (Note: the bathroom and home-remodeling pages are already a good length — use those as the template.)

### 🟠 Thin content on project / portfolio pages
The six project pages (Grand Vista Duplex, Cedar Cabin, Chandler Home Remodel, etc.) have **52–68 words each**. These are essentially image galleries with no descriptive text, which gives Google little to rank.

> **Fix:** Add 150–250 words per project — scope of work, location, materials, challenges solved, and outcome. This also builds local relevance ("Chandler", "Scottsdale", etc.).

### 🟠 Slow server response times
Several pages are slow to respond (Time to First Byte):

| Page | Response time |
|------|---------------|
| /contact-us/ | 12.98 s |
| /landscape-design-phoenix/ | 10.81 s |
| /about-us/ | 7.79 s |
| Homepage | 6.76 s |

Anything over ~1 second is a problem; these are well beyond that. Investigate hosting, caching, and unoptimized plugins/images. Slow TTFB hurts both rankings and conversions.

---

## 4. Low-Priority / Housekeeping

- **Typo in content:** the "Our Work" page reads *"home and **ourdoor** remodeling projects"* — should be "outdoor". Worth a quick proofread across the site.
- **Weak internal linking to projects:** the Scottsdale Kitchen Remodel page receives only **1 internal link**. Link portfolio pages from relevant service pages (e.g., link the Scottsdale Kitchen project from the Kitchen Remodeling page) to spread authority.
- **Readability:** several service pages score "Fairly Hard". Shorten sentences and break up paragraphs to improve user experience.
- **HTTP/1.1:** the site is served over HTTP/1.1. Moving to HTTP/2 (usually a host/CDN setting) gives a small performance gain.
- **Generic H1s where present:** the Contact page H1 is *"Have a Question ?"* — fine for UX, but consider a more descriptive heading.

---

## 5. What's Working Well ✅

- All 15 pages return `200 OK` and are **indexable** — no crawl or indexation errors.
- **Canonical tags** are present and self-referencing on every page.
- Clean, **keyword-friendly URL structure** (e.g., `/kitchen-remodel-phoenix/`).
- Logical site architecture — **crawl depth never exceeds 2 clicks**.
- Service page titles (kitchen, bathroom, home) are mostly well-formed and include location keywords.

---

## 6. Recommended Action Plan

| # | Action | Priority | Effort |
|---|--------|----------|--------|
| 1 | Replace homepage placeholder meta description | 🔴 High | Low |
| 2 | Add H1 tags to the 6 affected pages | 🔴 High | Low |
| 3 | Rewrite & lengthen homepage title tag | 🔴 High | Low |
| 4 | Trim 6 over-length meta descriptions | 🟠 Med | Low |
| 5 | Expand thin project-page content | 🟠 Med | Med |
| 6 | Investigate & reduce server response times | 🟠 Med | Med |
| 7 | Fix typos, improve internal links to projects | 🟢 Low | Low |

**Quick wins (items 1–4) can be completed in a few hours and address the highest-impact issues.**

---

*Audit based on a single Screaming Frog crawl. For a complete picture, pair this with Google Search Console (impressions/clicks/queries), Google Analytics (conversions), and a backlink profile review.*
