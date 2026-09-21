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
