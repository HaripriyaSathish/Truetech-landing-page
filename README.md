# Truetechs Landing Page

Stack: Django (templates for the public site + built-in admin for the dynamic
admin panel) + MySQL. HTML/CSS/JS drives the page and its animations; Django
serves it and stores content in MySQL so every section is editable from
`/admin/` without touching code.

## 1. Prerequisites

- Python 3.11+
- MySQL Server + MySQL Workbench (already installed per your setup)
- Git

## 2. Create the database in MySQL Workbench

1. Open MySQL Workbench, connect to your local MySQL instance.
2. Run in a new SQL tab:
   ```sql
   CREATE DATABASE truetechs_db CHARACTER SET utf8mb4;
   CREATE USER 'truetechs_user'@'localhost' IDENTIFIED BY 'yourpassword';
   GRANT ALL PRIVILEGES ON truetechs_db.* TO 'truetechs_user'@'localhost';
   FLUSH PRIVILEGES;
   ```
3. Execute (lightning bolt icon). You now have an empty `truetechs_db`
   database — Django will create all the tables for you via migrations
   (step 4 below), you never hand-write `CREATE TABLE`.

## 3. Project setup

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# edit .env: set DATABASE_URL to
# mysql://truetechs_user:yourpassword@127.0.0.1:3306/truetechs_db
```

> If `mysqlclient` fails to install (common on Windows without build tools),
> `pip install pymysql` instead and add this to the very top of
> `truetechs/__init__.py`:
> ```python
> import pymysql
> pymysql.install_as_MySQLdb()
> ```

## 4. Create tables and an admin login

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- Public site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/ — log in with the superuser you
  just created.

The homepage is empty until you add content in the admin. Fill these in,
roughly top to bottom of the page:

| Admin section | Controls |
|---|---|
| Site Settings (1 row) | Logo text, header CTA, footer description/tagline, social links |
| Navigation Links | Header nav bar items |
| Hero Sections + Hero Feature Pills | Top banner: heading, CTAs, stat badge, the 4 pills |
| Automation Sections + Services | "AI & Automation" block + its 4 feature cards |
| CTA Banners | The gradient "Ready to automate?" bar |
| BPO Sections + BPO Feature Cards | "Business Process Outsourcing" block |
| Offices Sections + Offices | Dubai/Chennai cards + the "Around the clock" bar |
| Why Us Sections + Why Us Feature Cards | 6-card grid around the center image |
| Commitments Sections + Commitment Steps | "How we work" 3 image cards |
| Process Sections + Process Steps | Blue 6-step timeline |
| Service Lines Sections + Service Lines | The interactive 8-row tabbed panel |
| FAQ Sections + FAQ Items | The accordion + quote card |
| Contact Sections | Left-hand copy on the contact form section |
| Info Strip Items | The 4-column bar above the footer |
| Footer Links | Quick Links / Services footer columns |
| Enquiries | Read-only — submissions from the contact form land here |

Every model has an `is_active` checkbox and an `order` field — untick to
hide a row without deleting it, change `order` to reorder.

## 5. Project structure

```
truetechs/          Django project config (settings, root urls)
core/                The app: models, admin registration, views, urls
  models.py          Database tables — one class per content type
  admin.py            Registers models so they get an admin UI for free
  views.py            Reads from DB, passes to templates
templates/
  base.html           Shared header/footer/nav
  core/index.html      Homepage sections
static/
  css/style.css        Styles + the .reveal scroll-animation pattern
  js/main.js            IntersectionObserver that drives .reveal
```

## 6. Workflow: turning each Figma screenshot into a working section

Repeat this loop per screenshot you send me:

1. **Model** — add a class to `core/models.py` for that section's content
   (e.g. `Testimonial`, `TeamMember`, `PricingPlan`).
2. **Migrate** — `python manage.py makemigrations && python manage.py migrate`.
3. **Register** — add it to `core/admin.py` so it's editable in `/admin/`.
4. **Template** — add the markup block to `templates/core/index.html` (or a
   new template), looping over the DB objects.
5. **Animate** — add the CSS/JS for that section's specific motion (see
   below for how to get the exact spec from Figma).
6. **Check in browser** — refresh, add sample content via `/admin/`, confirm
   it matches the screenshot and the animation feels right.

This keeps each section small and testable instead of building the whole
page at once — much safer against your deadline.

## 7. How to read the exact animation spec out of Figma

A screenshot only shows you the *end state* of an animation, not its motion.
Figma stores the actual interaction (trigger, animation type, easing,
duration) as prototype data — here's how to pull it out:

1. **Open the Figma *design* file** (the `/design/...` link you shared), not
   just the prototype player — you need edit/inspect access, not the
   playback-only view.
2. **Select the frame or layer** that animates. In the right sidebar, switch
   to the **Prototype** tab.
3. Every arrow leaving that frame is an interaction. Click the arrow itself
   (on the canvas, between two frames) to open its settings panel, which
   shows exactly:
   - **Trigger** — On Click, While Hovering, After Delay, Mouse Enter, etc.
   - **Action** — Navigate To, Open Overlay, Swap, Scroll To, etc.
   - **Animation** — Instant, Dissolve, Smart Animate, Move In/Out, Push,
     Slide In/Out
   - **Easing** — Ease In, Ease Out, Ease In & Out, Linear, spring/bounce presets
   - **Duration** — in milliseconds — this is your CSS `transition-duration`
4. **For hover/state animations on one component** (e.g. a button that
   scales on hover): these are usually two variants of the same component.
   Compare the layer properties (position, opacity, scale, rotation)
   between the default and hover variant — the *difference* between them is
   the animation; the interaction's easing/duration (from step 3) is the
   timing.
5. **For scroll-triggered reveals** (elements fading/sliding in as you
   scroll down the page — very common on landing pages): Figma prototypes
   don't actually simulate scroll-linked animation between frames, so these
   are usually implied rather than literally specified. Treat these as "the
   element should enter like this" and I'll implement them with the
   `.reveal` / `IntersectionObserver` pattern already in this project —
   you just need to tell me start/end state (e.g. "fades in and slides up
   20px") from the screenshot.
6. **If you don't have edit access to the Figma file**, use **Present mode**
   (▶ button, top-right) and screen-record it (Loom, OBS, or your OS's
   built-in recorder), then scrub the recording frame-by-frame to eyeball
   timing and motion. It's less precise than reading the Prototype panel
   directly, but works when you only have the proto link.
7. **Best option given your timeline**: when you send me a section
   screenshot, also send a screenshot of that frame's **Prototype panel**
   (step 3) if it has an interaction attached. That gives me exact numbers
   instead of me guessing durations/easing from a static image.

## 8. What to send me per section

For each part of the page (hero, services, testimonials, portfolio,
contact, footer, etc.), send:
- The screenshot of that section's static design
- The Prototype-panel screenshot for its interaction (if any), per §7
- Any copy/text you already have for it

I'll turn each one into a model + admin entry + template + animation, in
the order you send them.
