from django.contrib import admin

from .models import HeroSection, Service, SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_name", "contact_email", "contact_phone")

    def has_add_permission(self, request):
        # Enforce the singleton: block "Add" once a row exists.
        return not SiteSettings.objects.exists()


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("is_active",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("is_active",)
