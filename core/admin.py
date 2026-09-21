from django.contrib import admin

from .models import (
    AutomationSection,
    BpoFeature,
    BpoSection,
    CommitmentStep,
    CommitmentsSection,
    ContactSection,
    CtaBanner,
    Enquiry,
    FaqItem,
    FaqSection,
    FooterLink,
    HeroFeature,
    HeroSection,
    InfoStripItem,
    NavLink,
    Office,
    OfficesSection,
    ProcessSection,
    ProcessStep,
    Service,
    ServiceLine,
    ServiceLinesSection,
    SiteSettings,
    WhyUsFeature,
    WhyUsSection,
)


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


@admin.register(AutomationSection)
class AutomationSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("is_active",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "icon_key", "icon_color", "is_active", "order")
    list_editable = ("icon_key", "icon_color", "is_active", "order")
    list_filter = ("is_active", "icon_color")


@admin.register(CtaBanner)
class CtaBannerAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("is_active",)


@admin.register(BpoSection)
class BpoSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("is_active",)


@admin.register(BpoFeature)
class BpoFeatureAdmin(admin.ModelAdmin):
    list_display = ("number", "title", "icon_key", "is_active", "order")
    list_display_links = ("title",)
    list_editable = ("number", "icon_key", "is_active", "order")
    list_filter = ("is_active",)


@admin.register(OfficesSection)
class OfficesSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("is_active",)


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ("city", "label", "label_color", "phone", "is_active", "order")
    list_editable = ("label", "label_color", "phone", "is_active", "order")
    list_filter = ("is_active", "label_color")


@admin.register(WhyUsSection)
class WhyUsSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("is_active",)


@admin.register(WhyUsFeature)
class WhyUsFeatureAdmin(admin.ModelAdmin):
    list_display = ("title", "column", "icon_key", "icon_color", "is_active", "order")
    list_editable = ("column", "icon_key", "icon_color", "is_active", "order")
    list_filter = ("column", "is_active", "icon_color")


@admin.register(CommitmentsSection)
class CommitmentsSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("is_active",)


@admin.register(CommitmentStep)
class CommitmentStepAdmin(admin.ModelAdmin):
    list_display = ("number", "title", "is_active", "order")
    list_display_links = ("title",)
    list_editable = ("number", "is_active", "order")
    list_filter = ("is_active",)


@admin.register(ProcessSection)
class ProcessSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("is_active",)


@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ("number", "title", "icon_key", "is_active", "order")
    list_display_links = ("title",)
    list_editable = ("number", "icon_key", "is_active", "order")
    list_filter = ("is_active",)


@admin.register(ServiceLinesSection)
class ServiceLinesSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("is_active",)


@admin.register(ServiceLine)
class ServiceLineAdmin(admin.ModelAdmin):
    list_display = ("number", "title", "icon_key", "is_active", "order")
    list_display_links = ("title",)
    list_editable = ("number", "icon_key", "is_active", "order")
    list_filter = ("is_active",)
    fieldsets = (
        ("Sidebar", {"fields": ("number", "title", "icon_key", "order", "is_active")}),
        ("Detail panel", {"fields": ("image", "description", "bullets", "button_label", "button_url")}),
    )


@admin.register(InfoStripItem)
class InfoStripItemAdmin(admin.ModelAdmin):
    list_display = ("title", "icon_key", "icon_color", "is_active", "order")
    list_editable = ("icon_key", "icon_color", "is_active", "order")
    list_filter = ("is_active",)


@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ("label", "column", "url", "is_active", "order")
    list_editable = ("column", "url", "is_active", "order")
    list_filter = ("column", "is_active")


@admin.register(FaqSection)
class FaqSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("is_active",)


@admin.register(FaqItem)
class FaqItemAdmin(admin.ModelAdmin):
    list_display = ("question", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("is_active",)


@admin.register(ContactSection)
class ContactSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("is_active",)


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("full_name", "company", "email", "service", "submitted_at")
    list_filter = ("service", "submitted_at")
    readonly_fields = ("submitted_at",)
