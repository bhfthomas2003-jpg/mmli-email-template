# MMLI Email Template System

**Mind Masters Liberia Initiative** — *"Unleashing the Genius Within"*
*Home of the Serious Thinkers*

A complete, reusable, email-client-safe HTML email design system: 22 templates, a shared design system, and a static preview dashboard you can browse from your phone and later host free on GitHub Pages.

---

## 1. What's in this folder

```
mmli-email-system/
├── README.md                     ← this file
├── assets/
│   ├── logo/mmli-logo.png        ← MMLI logo
│   └── images/                   ← other images (e.g. signature)
├── styles/
│   └── mmli-design-system.css    ← design tokens reference (colors, type, spacing)
├── templates/                    ← 22 standalone .html email templates
└── preview/
    ├── index.html                ← the static preview dashboard
    └── templates-data.js         ← template content, generated — don't hand-edit
```

Every file in `templates/` is a **complete, self-contained email** — table-based layout, inline CSS, Outlook VML button fallback, and a mobile media query. You can copy any one of them straight into an email platform without touching anything else.

---

## 2. The 22 templates

| # | File | Purpose |
|---|------|---------|
| 1 | `master-newsletter.html` | Flagship, multi-story newsletter |
| 2 | `official-announcement.html` | Formal org-wide announcements |
| 3 | `school-invitation.html` | Invite a school to partner |
| 4 | `university-invitation.html` | Invite a university/institution |
| 5 | `partnership.html` | Formal partnership proposal |
| 6 | `sponsorship.html` | Request sponsorship/funding |
| 7 | `competition.html` | Announce a competition |
| 8 | `registration.html` | Invite registration for an event |
| 9 | `olympiad-training.html` | Announce Olympiad training |
| 10 | `teacher-recruitment.html` | Recruit coaches/teachers |
| 11 | `student-invitation.html` | Personal invitation to a student |
| 12 | `event-reminder.html` | Upcoming event reminder |
| 13 | `deadline-reminder.html` | Deadline approaching reminder |
| 14 | `program-launch.html` | Launch a new program |
| 15 | `membership-welcome.html` | Welcome a new member |
| 16 | `congratulations.html` | Congratulate an achievement |
| 17 | `award.html` | Award / recognition |
| 18 | `thank-you.html` | Thank sponsors/partners |
| 19 | `monthly-newsletter.html` | Recurring monthly update |
| 20 | `event-report.html` | Post-event summary/report |
| 21 | `academic-resource.html` | Announce a new resource |
| 22 | `international-outreach.html` | International partnership update |

---

## 3. Using the preview dashboard (from your phone)

1. Open `preview/index.html` in any mobile browser (Chrome, Safari, etc.) — no internet or install needed, it works as a plain file.
2. Tap any template card to preview it full-size.
3. Use **🖥 Desktop / 📱 Mobile** to switch preview widths.
4. Tap **Copy HTML** to copy the raw template (with `{{PLACEHOLDERS}}` intact) to your clipboard — ready to paste into an email platform.
5. Tap **Open in New Tab** to view a filled-in sample version full screen.
6. Tap **Download .html** to save the raw file to your device.
7. Use the search bar at the top to filter templates by name or purpose.

The dashboard needs no backend, no build step, and no internet connection once the folder is on your device — it's plain static HTML/CSS/JS.

---

## 4. The design system

All brand values live in `styles/mmli-design-system.css` as CSS variables **and** are duplicated as inline styles inside every template (email clients strip `<style>`/external CSS unreliably, so inline is the source of truth for actual sending — the CSS file is documentation you edit alongside it).

| Token | Value | Used for |
|---|---|---|
| Deep Navy | `#0B2545` | Header/footer background, primary text on light |
| Navy | `#123B70` | Gradient accent, secondary elements |
| Navy Light | `#1F4E8C` | Links on dark backgrounds |
| Gold | `#C9A227` | Primary buttons, dividers, eyebrow text |
| Gold Light | `#E8C860` | Highlights, hover states |
| Gold Pale | `#F6ECC9` | Alert/highlight box background |
| Background | `#F4F6FA` | Page canvas behind the email |
| Card Background | `#F8F9FC` | Info cards |
| Body Text | `#2B2F38` | Paragraph copy |
| Muted Text | `#6B7280` | Secondary/meta copy |

**Typography:** Georgia (serif) for headlines and the eyebrow/organization wordmark — gives the "serious, prestigious, academic" tone; Arial/Helvetica for all body copy — reliable across every email client.

**Shared components used across every template:** gradient divider bar (navy → gold), circular logo badge, eyebrow label, info/details card, gold alert box, gold primary button with Outlook VML fallback, navy footer with social row and legal/unsubscribe line.

---

## 5. Placeholders

Every template uses `{{PLACEHOLDER}}` tokens. Replace these via your email platform's merge-tag/mail-merge feature, or with find-and-replace before sending.

```
{{FIRST_NAME}}          {{LAST_NAME}}           {{EMAIL}}
{{EVENT_NAME}}           {{EVENT_DATE}}          {{EVENT_TIME}}
{{VENUE}}                {{REGISTRATION_LINK}}   {{WEBSITE}}
{{CONTACT_EMAIL}}        {{CONTACT_ADDRESS}}     {{PHONE}}
{{FACEBOOK_URL}}         {{INSTAGRAM_URL}}       {{WHATSAPP_URL}}
{{LOGO_URL}}             {{CURRENT_YEAR}}        {{UNSUBSCRIBE_LINK}}
{{SENDER_NAME}}          {{SENDER_TITLE}}
```

Plus template-specific tokens (e.g. `{{SCHOOL_NAME}}`, `{{COMPETITION_NAME}}`, `{{AWARD_NAME}}`) — open a template and search for `{{` to see all tokens it uses.

---

## 6. How-to guide

### 6.1 Add the MMLI logo
Replace `assets/logo/mmli-logo.png` with your final logo file (keep the filename, or update `{{LOGO_URL}}` everywhere). For sending, `{{LOGO_URL}}` must point to a **publicly hosted** image URL (email clients cannot load local files) — e.g. your GitHub Pages URL: `https://yourusername.github.io/mmli-email-system/assets/logo/mmli-logo.png`.

### 6.2 Change colors
Edit the hex values in `styles/mmli-design-system.css`, then find-and-replace the same hex codes across `templates/*.html` (they're inline). The main ones to change: `#0B2545` (navy), `#C9A227` (gold).

### 6.3 Change contact information
Fill in `{{CONTACT_EMAIL}}`, `{{CONTACT_ADDRESS}}`, `{{PHONE}}`, `{{WEBSITE}}` — either via your email platform's merge tags, or find-and-replace before sending.

### 6.4 Add social media links
Set `{{FACEBOOK_URL}}`, `{{INSTAGRAM_URL}}`, `{{WHATSAPP_URL}}` to your real profile URLs. To add another platform (e.g. LinkedIn, X/Twitter, TikTok), copy one `<a>` tag in the footer's social row in any template and duplicate it for the new platform.

### 6.5 Add buttons
Copy the `<!--[if mso]> ... <![endif]-->` button block from any template (search for `roundrect`) into your content area, and update the button label and `href`. This keeps the Outlook-safe rounded-button fallback.

### 6.6 Add images
Insert an `<img>` tag with an explicit `width` and `height`, `style="display:block;border:0;"`, and a publicly hosted `src` URL. Keep images under ~200KB — large images slow email load and hurt deliverability. Never rely on background images for essential content — some clients (Outlook) block them.

### 6.7 Create a new template from the master
Copy `templates/master-newsletter.html`, rename it, then edit only the content inside the `<!-- BODY -->` table — leave the `<!-- HEADER -->` and `<!-- FOOTER -->` sections untouched so branding stays consistent. Add it to `preview/templates-data.js`'s source list by re-running the generator (see §8) or manually following the same JSON shape.

### 6.8 Export/copy HTML into an email marketing platform
Open the dashboard, tap a template, tap **Copy HTML**, then paste directly into your platform's "Custom HTML" / "Code editor" view (not the visual/drag-and-drop editor).

### 6.9 Using with Gmail / Brevo / Mailchimp
- **Gmail:** Open the `.html` file in a browser, select all rendered content (Ctrl/Cmd+A), copy, and paste into a new Gmail compose window — Gmail will preserve most inline styles. For merge tags, use Gmail's mail-merge add-ons.
- **Brevo:** Campaigns → Create a campaign → **Rich-text/HTML editor → Code view** → paste the raw HTML. Map `{{PLACEHOLDER}}` tokens to Brevo's `{{ contact.ATTRIBUTE }}` syntax, or find-and-replace before upload.
- **Mailchimp:** Campaigns → Create → **Code your own → Paste in code** → paste the raw HTML. Replace `{{PLACEHOLDER}}` tokens with Mailchimp merge tags (e.g. `*|FNAME|*`) or find-and-replace before pasting.

### 6.10 Hosting the template library on GitHub Pages
1. Create a new GitHub repository (e.g. `mmli-email-system`) and push this entire folder to it.
2. In the repo, go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to `Deploy from a branch`, branch `main`, folder `/ (root)`.
4. Save. GitHub will publish at `https://yourusername.github.io/mmli-email-system/`.
5. Your live preview dashboard will be at `https://yourusername.github.io/mmli-email-system/preview/`.
6. Your publicly hosted logo (for use in `{{LOGO_URL}}` when actually sending emails) will be at `https://yourusername.github.io/mmli-email-system/assets/logo/mmli-logo.png`.
7. No build step, no backend, and no repo secrets are required — everything here is static.

---

## 7. Email-client compatibility notes

- **Layout:** table-based (`role="presentation"` tables), not CSS flexbox/grid — required for Outlook desktop (which uses Word's rendering engine).
- **Styling:** all critical styles are inline; a `<style>` block adds mobile-responsive enhancements for clients that support it (Gmail, Apple Mail, Outlook.com, most mobile clients) and is safely ignored by clients that don't.
- **Buttons:** use a VML fallback (`<!--[if mso]>...<![endif]-->`) so Outlook desktop renders a proper rounded button instead of a plain link.
- **Images:** all `<img>` tags include explicit `width`/`height` and `border:0` to prevent layout shift and blue link borders.
- **Preheader text:** each template includes a hidden preheader line (the gray preview text next to the subject line in inbox lists).
- **No JavaScript, no web fonts requiring external CSS, no unsupported CSS** (no flexbox/grid, no `position`, no CSS variables) inside the templates themselves — all of that is confined to the preview dashboard, which is a *browser* tool, not an email.
- **Dark mode:** `<meta name="color-scheme" content="light">` and `<meta name="supported-color-schemes" content="light">` tell supporting clients (Apple Mail, Outlook iOS) to keep the design in light mode rather than auto-inverting colors.

---

## 8. Regenerating the templates (optional, for developers)

The templates were built from two Python scripts kept alongside this project for future edits:

- `build_templates.py` — defines the shared skeleton (header/footer/buttons/cards) and each of the 22 templates' content, then writes `templates/*.html`.
- `build_preview_data.py` — reads the generated templates, fills them with sample data, and writes `preview/templates-data.js` for the dashboard.

To add a 23rd template or edit shared branding in one place: edit `build_templates.py`, re-run it, then re-run `build_preview_data.py`.

---

## 9. Pre-flight checklist before sending a real campaign

- [ ] Replace `{{LOGO_URL}}` with a real, publicly hosted URL (not a local file path)
- [ ] Fill in or merge-tag every `{{PLACEHOLDER}}` — search the HTML for `{{` to confirm none remain
- [ ] Test send to a Gmail address, an Outlook address, and a phone mail app
- [ ] Confirm all links (`{{REGISTRATION_LINK}}`, `{{WEBSITE}}`, social URLs) are live
- [ ] Keep total email HTML under ~100KB (Gmail clips larger emails)
- [ ] Compress any added images before uploading
