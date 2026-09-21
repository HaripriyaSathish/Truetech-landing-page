from django.contrib import admin

from .models import HeroFeature, HeroSection, NavLink, Service, SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_name", "contact_email", "contact_phone")

    def has_add_permission(self, request):
        # Enforce the singleton: block "Add" once a row exists.
        return not SiteSettings.objects.exists()


@admin.register(NavLink)
class NavLinkAdmin(admin.ModelAdmin):
    list_display = ("label", "url", "is_active", "order")
    list_editable = ("url", "is_active", "order")
    list_filter = ("is_active",)


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("is_active",)
    fieldsets = (
        ("Text", {"fields": ("eyebrow_text", "heading", "heading_highlight", "description")}),
        ("Buttons", {"fields": (
            ("primary_cta_label", "primary_cta_url"),
            ("secondary_cta_label", "secondary_cta_url"),
        )}),
        ("Image & stat badge", {"fields": ("background_image", "stat_value", "stat_caption")}),
        ("Visibility", {"fields": ("is_active", "order")}),
    )


@admin.register(HeroFeature)
class HeroFeatureAdmin(admin.ModelAdmin):
    list_display = ("label", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("is_active",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("is_active",)
