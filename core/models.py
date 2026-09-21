from django.core.exceptions import ValidationError
from django.db import models


class SiteSettings(models.Model):
    """Global site config (header + footer), edited from the admin. Only one row should ever exist."""

    site_name = models.CharField(max_length=100, default="TrueTechs")
    logo = models.ImageField(upload_to="site/", blank=True, null=True)
    logo_subtitle = models.CharField(
        max_length=100, blank=True, help_text='e.g. "IT · AUTOMATION · BPO", shown next to the logo in the header.'
    )
    tagline = models.CharField(max_length=200, blank=True)
    header_cta_label = models.CharField(max_length=50, blank=True, default="Get a quote")
    header_cta_url = models.CharField(max_length=200, blank=True, default="#contact")
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=255, blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)

    footer_description = models.TextField(
        blank=True, help_text='e.g. "IT infrastructure, automation and business process operations — delivered from Dubai and Chennai."'
    )
    footer_tagline = models.CharField(max_length=100, blank=True, default="24/7 monitoring and service desk")

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def clean(self):
        if not self.pk and SiteSettings.objects.exists():
            raise ValidationError("Site Settings already exists — edit the existing row instead of adding a new one.")

    def __str__(self):
        return self.site_name


class NavLink(models.Model):
    """One item in the header navigation bar (Home, Services, Why us, ...)."""

    label = models.CharField(max_length=50)
    url = models.CharField(max_length=200, default="#", help_text='e.g. "#services" or "/services/".')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Navigation Link"

    def __str__(self):
        return self.label


class HeroSection(models.Model):
    """The landing page's top/hero block. Add more sections the same way as you convert each Figma screen."""

    eyebrow_text = models.CharField(
        max_length=100, blank=True, help_text='Small label above the heading, e.g. "IT INFRASTRUCTURE SUPPORT".'
    )
    heading = models.CharField(max_length=200, help_text='Main heading text, e.g. "Keep your systems running".')
    heading_highlight = models.CharField(
        max_length=200, blank=True, help_text='Second line shown in the accent color, e.g. "day and night."'
    )
    description = models.TextField(blank=True)

    primary_cta_label = models.CharField(max_length=50, blank=True, default="Get a quote")
    primary_cta_url = models.CharField(max_length=200, blank=True, default="#contact")
    secondary_cta_label = models.CharField(max_length=50, blank=True, default="View services")
    secondary_cta_url = models.CharField(max_length=200, blank=True, default="#services")

    background_image = models.ImageField(upload_to="hero/", blank=True, null=True)

    stat_value = models.CharField(
        max_length=20, blank=True, help_text='Small stat badge shown over the hero image, e.g. "99.97%".'
    )
    stat_caption = models.CharField(max_length=100, blank=True)

    is_active = models.BooleanField(default=True, help_text="Only the active hero is shown on the site.")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Sections"

    def __str__(self):
        return self.heading


class HeroFeature(models.Model):
    """One pill badge shown at the bottom of the hero, e.g. "24/7 NOC", "Cloud & M365"."""

    icon = models.ImageField(upload_to="hero_features/", blank=True, null=True)
    label = models.CharField(max_length=50)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Hero Feature Pill"

    def __str__(self):
        return self.label


class AutomationSection(models.Model):
    """The "AI & Automation" block: eyebrow/heading/description + the image with its floating badge."""

    eyebrow_text = models.CharField(max_length=100, blank=True, help_text='e.g. "AI & AUTOMATION".')
    heading = models.CharField(max_length=200, help_text='e.g. "Put the repetitive work on autopilot."')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="automation/", blank=True, null=True)

    badge_label = models.CharField(
        max_length=100, blank=True, default="Live automation running",
        help_text="Small floating label shown over the image's top-left corner.",
    )
    badge_tags = models.CharField(
        max_length=200, blank=True, help_text='Comma-separated short tags shown under the badge label, e.g. "AI, RPA, DOC, CRM".'
    )

    badge2_title = models.CharField(
        max_length=100, blank=True, default="Workflows automated",
        help_text="Second floating badge, shown over the image's bottom-right corner. Leave blank to hide it.",
    )
    badge2_subtitle = models.CharField(max_length=150, blank=True, default="Across 4 service lines")

    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Automation Section"
        verbose_name_plural = "Automation Sections"

    def __str__(self):
        return self.heading

    def tag_list(self):
        return [t.strip() for t in self.badge_tags.split(",") if t.strip()]


class CtaBanner(models.Model):
    """A full-width call-to-action banner, e.g. "Ready to automate?" below the services grid."""

    heading = models.CharField(max_length=150)
    subheading = models.CharField(max_length=200, blank=True)
    button_label = models.CharField(max_length=50, blank=True, default="Get started")
    button_url = models.CharField(max_length=200, blank=True, default="#contact")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "CTA Banner"

    def __str__(self):
        return self.heading


class Service(models.Model):
    """A repeatable feature/service card — used in the AI & Automation grid and any similar section."""

    ICON_CHOICES = [
        ("monitor", "Monitor"),
        ("refresh", "Refresh / RPA"),
        ("document", "Document"),
        ("grid", "Dashboard / CRM"),
    ]
    COLOR_CHOICES = [
        ("blue", "Blue"),
        ("orange", "Orange"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon_key = models.CharField(
        max_length=20, choices=ICON_CHOICES, default="monitor",
        help_text="Built-in icon shown in the colored square — no image upload needed.",
    )
    icon_color = models.CharField(max_length=10, choices=COLOR_CHOICES, default="blue")
    icon = models.ImageField(
        upload_to="services/", blank=True, null=True,
        help_text="Optional: upload a custom icon image to override the built-in one above.",
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class BpoSection(models.Model):
    """The "Business Process Outsourcing" block: eyebrow/heading/description + image with its two badges."""

    eyebrow_text = models.CharField(max_length=100, blank=True, help_text='e.g. "BUSINESS PROCESS OUTSOURCING".')
    heading = models.CharField(max_length=200, help_text='First part of the heading, e.g. "Give your customers a".')
    heading_highlight = models.CharField(
        max_length=200, blank=True, help_text='Second part, e.g. "team that answers." (shown in the ink color, bold).'
    )
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="bpo/", blank=True, null=True)

    stat_value = models.CharField(max_length=20, blank=True, default="24/7", help_text="Top-left floating stat badge.")
    stat_caption = models.CharField(max_length=100, blank=True, default="Support coverage")

    badge_label = models.CharField(
        max_length=100, blank=True, default="ACTIVE CHANNELS",
        help_text="Small uppercase label in the bottom-right solid badge.",
    )
    badge_value = models.CharField(max_length=150, blank=True, default="Voice · Chat · Email")

    tags = models.CharField(
        max_length=200, blank=True, help_text='Comma-separated pill row below the cards, e.g. "Voice, Email, Chat, WhatsApp, 24/7".'
    )

    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "BPO Section"
        verbose_name_plural = "BPO Sections"

    def __str__(self):
        return self.heading

    def tag_list(self):
        return [t.strip() for t in self.tags.split(",") if t.strip()]


class BpoFeature(models.Model):
    """One numbered card in the BPO grid, e.g. "01 Customer support"."""

    ICON_CHOICES = [
        ("mic", "Microphone"),
        ("briefcase", "Briefcase"),
        ("document", "Document"),
        ("user-plus", "User Plus"),
    ]

    number = models.CharField(max_length=10, blank=True, help_text='e.g. "01".')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon_key = models.CharField(max_length=20, choices=ICON_CHOICES, default="mic")
    icon = models.ImageField(
        upload_to="bpo_features/", blank=True, null=True,
        help_text="Optional: upload a custom icon image to override the built-in one above.",
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "BPO Feature Card"

    def __str__(self):
        return self.title


class OfficesSection(models.Model):
    """Heading for the offices block, plus the "Around the clock" highlight bar under the cards."""

    eyebrow_text = models.CharField(max_length=100, blank=True, default="WHERE WE WORK FROM")
    heading = models.CharField(max_length=200, help_text='e.g. "Dubai for the relationship, Chennai for the engineering."')
    description = models.TextField(blank=True)

    highlight_title = models.CharField(max_length=100, blank=True, default="Around the clock")
    highlight_description = models.CharField(max_length=250, blank=True)
    highlight_channels = models.CharField(
        max_length=200, blank=True, help_text='Comma-separated pill list, e.g. "Voice, Chat, Email". Leave blank to hide.'
    )

    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Offices Section"
        verbose_name_plural = "Offices Sections"

    def __str__(self):
        return self.heading

    def channel_list(self):
        return [c.strip() for c in self.highlight_channels.split(",") if c.strip()]


class Office(models.Model):
    """One office card, e.g. "Dubai, UAE — Head Office"."""

    COLOR_CHOICES = [("orange", "Orange"), ("blue", "Blue")]

    label = models.CharField(max_length=50, help_text='Small pin label, e.g. "HEAD OFFICE".')
    label_color = models.CharField(max_length=10, choices=COLOR_CHOICES, default="orange")
    city = models.CharField(max_length=100, help_text='e.g. "Dubai, UAE".')
    address = models.CharField(max_length=255, blank=True)
    caption = models.CharField(max_length=150, blank=True, help_text='e.g. "Commercial relationship".')
    timezone_label = models.CharField(max_length=50, blank=True, help_text='e.g. "GST · UTC+4".')
    phone = models.CharField(max_length=30, blank=True)
    toggle_label = models.CharField(max_length=30, blank=True, help_text='Short label for the toggle pill, e.g. "DUBAI".')
    image = models.ImageField(upload_to="offices/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.city


class WhyUsSection(models.Model):
    """The "Why work with us" block: eyebrow/heading/description + the center image with its badge."""

    eyebrow_text = models.CharField(max_length=100, blank=True, default="WHY WORK WITH US")
    heading = models.CharField(max_length=200, help_text='e.g. "Support measured by what it changes in your operation."')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="whyus/", blank=True, null=True)
    badge_label = models.CharField(max_length=100, blank=True, default="One partner")
    badge_value = models.CharField(max_length=100, blank=True, default="8 service lines")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Why Us Section"
        verbose_name_plural = "Why Us Sections"

    def __str__(self):
        return self.heading


class WhyUsFeature(models.Model):
    """One card in the Why Us grid, placed in the left or right column around the center image."""

    ICON_CHOICES = [
        ("shield", "Shield"),
        ("dollar", "Dollar"),
        ("bolt", "Bolt"),
        ("clock", "Clock"),
        ("trending-up", "Trending Up"),
        ("users", "Users"),
    ]
    COLUMN_CHOICES = [("left", "Left"), ("right", "Right")]
    COLOR_CHOICES = [("blue", "Blue"), ("orange", "Orange")]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon_key = models.CharField(max_length=20, choices=ICON_CHOICES, default="shield")
    icon_color = models.CharField(max_length=10, choices=COLOR_CHOICES, default="blue")
    icon = models.ImageField(
        upload_to="whyus_features/", blank=True, null=True,
        help_text="Optional: upload a custom icon image to override the built-in one above.",
    )
    column = models.CharField(max_length=10, choices=COLUMN_CHOICES, default="left")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Why Us Feature Card"

    def __str__(self):
        return self.title


class CommitmentsSection(models.Model):
    """Heading for the "How we work" trust block. The cards themselves are the CommitmentStep model below."""

    eyebrow_text = models.CharField(max_length=100, blank=True, default="HOW WE WORK")
    heading = models.CharField(max_length=200, help_text='e.g. "Three commitments we hold to on every engagement."')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Commitments Section"
        verbose_name_plural = "Commitments Sections"

    def __str__(self):
        return self.heading


class CommitmentStep(models.Model):
    """One numbered image card in the commitments grid, e.g. "01 Scoped, not templated"."""

    number = models.CharField(max_length=10, blank=True, help_text='e.g. "01".')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="commitments/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Commitment Step"

    def __str__(self):
        return self.title


class ProcessSection(models.Model):
    """The "Our Process" blue timeline block: eyebrow/heading/description. Steps are ProcessStep below."""

    eyebrow_text = models.CharField(max_length=100, blank=True, default="OUR PROCESS")
    heading = models.CharField(max_length=200, help_text='e.g. "From first assessment to steady state."')
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Process Section"
        verbose_name_plural = "Process Sections"

    def __str__(self):
        return self.heading


class ProcessStep(models.Model):
    """One step icon in the "Our Process" timeline, e.g. "01 Assess"."""

    ICON_CHOICES = [
        ("target", "Target"),
        ("nodes", "Nodes / Plan"),
        ("link", "Link / Implement"),
        ("grid", "Dashboard / Monitor"),
        ("headset", "Headset / Support"),
        ("sparkles", "Sparkles / Optimise"),
    ]

    number = models.CharField(max_length=10, blank=True, help_text='e.g. "01".')
    icon_key = models.CharField(max_length=20, choices=ICON_CHOICES, default="target")
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Process Step"

    def __str__(self):
        return self.title


class ServiceLinesSection(models.Model):
    """Heading for the "Eight service lines" block. The rows themselves are the ServiceLine model below."""

    eyebrow_text = models.CharField(max_length=100, blank=True, default="WHAT WE DO")
    heading = models.CharField(max_length=200, help_text='e.g. "Eight service lines, one point of contact."')
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Service Lines Section"
        verbose_name_plural = "Service Lines Sections"

    def __str__(self):
        return self.heading


class ServiceLine(models.Model):
    """One entry in the interactive "Eight service lines" tabbed panel — click a row to switch the detail panel."""

    ICON_CHOICES = [
        ("monitor", "Monitor"), ("refresh", "Refresh"), ("document", "Document"), ("grid", "Grid"),
        ("shield", "Shield"), ("dollar", "Dollar"), ("clock", "Clock"), ("trending-up", "Trending Up"),
        ("users", "Users"), ("bolt", "Bolt"), ("mic", "Mic"), ("briefcase", "Briefcase"),
    ]

    number = models.CharField(max_length=10, blank=True, help_text='e.g. "01".')
    title = models.CharField(max_length=100, help_text='e.g. "24/7 IT Infrastructure Support".')
    icon_key = models.CharField(max_length=20, choices=ICON_CHOICES, default="grid")
    image = models.ImageField(upload_to="service_lines/", blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, help_text="Short summary shown under the title in the detail panel.")
    bullets = models.TextField(blank=True, help_text="One checklist bullet per line.")
    button_label = models.CharField(max_length=50, blank=True, default="Enquire About This Service")
    button_url = models.CharField(max_length=200, blank=True, default="#contact")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Service Line"

    def __str__(self):
        return self.title

    def bullet_list(self):
        return [b.strip() for b in self.bullets.splitlines() if b.strip()]


class InfoStripItem(models.Model):
    """One of the 4 columns in the info strip between the contact form and the footer (Dubai, Chennai, Email, Hours)."""

    ICON_CHOICES = [
        ("map-pin", "Map Pin"), ("mail", "Mail"), ("clock", "Clock"), ("bolt", "Bolt"),
    ]
    COLOR_CHOICES = [("orange", "Orange"), ("blue", "Blue")]

    icon_key = models.CharField(max_length=20, choices=ICON_CHOICES, default="map-pin")
    icon_color = models.CharField(max_length=10, choices=COLOR_CHOICES, default="orange")
    title = models.CharField(max_length=100, help_text='e.g. "Dubai — Head Office".')
    description = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Info Strip Item"

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    """One link in a footer column (Quick Links or Services)."""

    COLUMN_CHOICES = [("quick_links", "Quick Links"), ("services", "Services")]

    column = models.CharField(max_length=20, choices=COLUMN_CHOICES, default="quick_links")
    label = models.CharField(max_length=100)
    url = models.CharField(max_length=200, default="#")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Footer Link"

    def __str__(self):
        return self.label


class FaqSection(models.Model):
    """The FAQ block: eyebrow/heading + the image/quote card. Questions are the FaqItem model below."""

    eyebrow_text = models.CharField(max_length=100, blank=True, default="QUESTIONS")
    heading = models.CharField(max_length=200, help_text='e.g. "What clients ask before they start."')
    image = models.ImageField(upload_to="faq/", blank=True, null=True)
    quote_text = models.CharField(max_length=300, blank=True)
    quote_author = models.CharField(max_length=100, blank=True, default="TrueTechs")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "FAQ Section"
        verbose_name_plural = "FAQ Sections"

    def __str__(self):
        return self.heading


class FaqItem(models.Model):
    """One question in the FAQ accordion. Click the question to expand/collapse the answer."""

    question = models.CharField(max_length=200)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "FAQ Item"

    def __str__(self):
        return self.question


class ContactSection(models.Model):
    """The "Tell us what your operation needs" block: heading/description/background + the checklist bullets."""

    eyebrow_text = models.CharField(max_length=100, blank=True, default="GET IN TOUCH")
    heading = models.CharField(max_length=200, help_text='e.g. "Tell us what your operation needs."')
    description = models.TextField(blank=True)
    background_image = models.ImageField(upload_to="contact/", blank=True, null=True)
    bullets = models.TextField(blank=True, help_text="One checklist bullet per line.")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Contact Section"
        verbose_name_plural = "Contact Sections"

    def __str__(self):
        return self.heading

    def bullet_list(self):
        return [b.strip() for b in self.bullets.splitlines() if b.strip()]


class Enquiry(models.Model):
    """A submitted contact-form enquiry. View these at /admin/ → Enquiries."""

    full_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    service = models.CharField(max_length=150, blank=True)
    requirement = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-submitted_at"]
        verbose_name_plural = "Enquiries"

    def __str__(self):
        return f"{self.full_name} — {self.company}"
