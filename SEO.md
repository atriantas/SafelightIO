# SEO notes — SafelightIO landing page

The page is one URL on GitHub Pages until it moves to its own server. Everything
here is written for that move: the absolute URLs live in four places and must be
changed together.

## What the page targets

| Priority | Query | US/mo | Where it lives |
| --- | --- | --- | --- |
| Money page | `darkroom printing` | 720 | `<title>`, `<h1>`, lead, OG card |
| Best asset | `darkroom test strips`, `test strip darkroom`, `darkroom test strip` | 110–140 each | “Test strips, and what the ladder costs” section |
| Top of funnel | `what is a test strip`, `test strips photography` | 110–140 | first note of that section |
| Supporting | `darkroom setup`, `darkroom paper`, `ilford multigrade filters`, `darkroom enlarger` | 140–1900 | compatibility ledger, setup steps, paper list, filter editor |

Deliberately **not** in titles: `darkroom light meter` (no Ads volume),
`enlarger light meter` (1/mo), `darkroom exposure meter` (10/mo), `split grade
printing` (1/mo). They describe the product perfectly and nobody types them —
they belong in body copy, which is where they are.

## Changed in the SEO pass

- **Canonical fixed.** It pointed at `https://www.cyanowood.com/lightmeter`,
  which returns 404. Now self-referential, with `og:url` and `Product.url`
  agreeing. This was the bug that could keep the page out of the index entirely.
- **Title and description** now lead with `darkroom printing` + `test strips`
  (51 / 144 characters).
- **H1** is `Darkroom printing, one reading.` — keyword first, same voice.
- **New section** `#test-strips`: one H2 and three H3s on what a test strip is,
  why one is rarely enough, and the one-reading alternative. ~230 words.
- **Compatibility H2** now names the enlarger as well as the darkroom.
- **Product schema** gained `image` (required for product rich results), `sku`,
  `itemCondition`, and a self URL. Organization gained a `logo`.
- **Social cards**: 1200×630 `assets/og-safelightio.jpg`, `summary_large_image`,
  dimensions and alt text declared.
- **Favicon** + apple-touch-icon.
- **Images**: WebP (3.89 MB of PNG → ~0.29 MB), `loading="lazy"` below the fold,
  hero preloaded with `fetchpriority="high"`. Width/height kept, so no CLS.
- **Firmware links fixed**: they pointed at `assets/…uf2`, which 404s; the file
  is at the repo root.
- **sitemap.xml** and **robots.txt** added. `robots.txt` only takes effect at a
  domain root — GitHub project sites answer at `/SafelightIO/` and read the host
  root's robots.txt, which this repo cannot set.
- **Footer** links to the Shopify product page, so the two pages stop competing
  silently.

## When it moves to a server

Change these together, then keep the GitHub URL redirecting (301) to the new one:

1. `<link rel="canonical">`
2. `og:url`
3. `og:image` and `twitter:image`
4. `Product.url` and every entry in `Product.image[]`
5. `sitemap.xml` → `<loc>` and `<lastmod>`
6. `robots.txt` → `Sitemap:` line

If the new home is `cyanowood.com`, the cleanest version is a Shopify page or a
subdomain that serves this file, with the product page canonicalising to itself
and linking here.

## The dongle (described, not yet sold)

The page now covers two forms of the same meter: the 7-inch instrument and the
USB-C dongle that uses an Android phone as its screen. The dongle is **not for
sale**: there is no price, no CTA and no second `Offer` in the schema, and the
buy block says so. The title still carries `darkroom printing`; the meta
description now names both forms, which is the only SEO change this needed.

When the dongle goes on sale:

1. Add its Shopify product or variant link to the buy block (the 7-inch cart
   link stays where it is).
2. Either extend `Product` with a second `Offer`, or make the dongle its own
   page if it gets a different price — one Offer with two prices is not valid.
3. Update the buy lead: replace “the dongle is coming”.

Downloads are live: the header **Firmware** menu now lists both UF2s and links
the update guide, the footer lists both firmware files and the APK, and the FAQ
answer about the phone links the Android app (`SafelightIO.apk`, 13 MB). The
dongle manual still says firmware 0.11 while the file is named v1.0, so the
download is labelled without a version until the two agree.

## Still missing

- **Search Console.** Verify `https://atriantas.github.io/SafelightIO/` with the
  HTML-file method (the prefix works), submit `sitemap.xml`, and check coverage
  after a week. Without it there is no way to see which queries the page earns.
- **No analytics.** The page deliberately ships none; GSC impressions are enough
  to start, and a privacy-friendly counter can come later.
- **No backlinks.** One link from the Shopify product page to this page (and the
  one added here in the footer) is the cheapest first citation.
- **Host limits.** `github.io` is a shared host: no host-root robots.txt, no
  server redirects, and no domain authority of its own. Acceptable until the
  move, not a long-term home.
- **Thin product page.** The Shopify page's description is ~300 characters; if
  that page is meant to rank too, it needs the manual's detail, not a summary.
