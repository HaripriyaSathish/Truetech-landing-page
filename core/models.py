from django.core.exceptions import ValidationError
from django.db import models


class SiteSettings(models.Model):
    """Global site config, edited from the admin. Only one row should ever exist."""

    site_name = models.CharField(max_length=100, default="Truetechs")
    logo = models.ImageField(upload_to="site/", blank=True, null=True)
    tagline = models.CharField(max_length=200, blank=True)
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


class HeroSection(models.Model):
    """The landing page's top/hero block. Add more sections the same way as you convert each Figma screen."""

    heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    cta_label = models.CharField(max_length=50, blank=True)
    cta_url = models.CharField(max_length=200, blank=True)
    background_image = models.ImageField(upload_to="hero/", blank=True, null=True)
    is_active = models.BooleanField(default=True, help_text="Only the active hero is shown on the site.")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Sections"

    def __str__(self):
        return self.heading


class Service(models.Model):
    """Example repeatable content block (services/features grid) — a template for other repeatable sections."""

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to="services/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
