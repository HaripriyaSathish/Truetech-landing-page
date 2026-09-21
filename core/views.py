from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import EnquiryForm
from .models import (
    AutomationSection,
    BpoFeature,
    BpoSection,
    CommitmentStep,
    CommitmentsSection,
    ContactSection,
    CtaBanner,
    FaqItem,
    FaqSection,
    FooterLink,
    HeroFeature,
    HeroSection,
    InfoStripItem,
    Office,
    OfficesSection,
    ProcessSection,
    ProcessStep,
    Service,
    ServiceLine,
    ServiceLinesSection,
    WhyUsFeature,
    WhyUsSection,
)


def index(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks — we've received your enquiry and will be in touch shortly.")
            return redirect("/#contact")
    else:
        form = EnquiryForm()

    context = {
        "hero": HeroSection.objects.filter(is_active=True).first(),
        "hero_features": HeroFeature.objects.filter(is_active=True),
        "automation": AutomationSection.objects.filter(is_active=True).first(),
        "services": Service.objects.filter(is_active=True),
        "cta_banner": CtaBanner.objects.filter(is_active=True).first(),
        "bpo": BpoSection.objects.filter(is_active=True).first(),
        "bpo_features": BpoFeature.objects.filter(is_active=True),
        "offices_section": OfficesSection.objects.filter(is_active=True).first(),
        "offices": Office.objects.filter(is_active=True),
        "whyus": WhyUsSection.objects.filter(is_active=True).first(),
        "whyus_left": WhyUsFeature.objects.filter(is_active=True, column="left"),
        "whyus_right": WhyUsFeature.objects.filter(is_active=True, column="right"),
        "commitments_section": CommitmentsSection.objects.filter(is_active=True).first(),
        "commitment_steps": CommitmentStep.objects.filter(is_active=True),
        "process_section": ProcessSection.objects.filter(is_active=True).first(),
        "process_steps": ProcessStep.objects.filter(is_active=True),
        "service_lines_section": ServiceLinesSection.objects.filter(is_active=True).first(),
        "service_lines": ServiceLine.objects.filter(is_active=True),
        "info_strip_items": InfoStripItem.objects.filter(is_active=True),
        "footer_quick_links": FooterLink.objects.filter(is_active=True, column="quick_links"),
        "footer_service_links": FooterLink.objects.filter(is_active=True, column="services"),
        "faq_section": FaqSection.objects.filter(is_active=True).first(),
        "faq_items": FaqItem.objects.filter(is_active=True),
        "contact_section": ContactSection.objects.filter(is_active=True).first(),
        "enquiry_form": form,
    }
    return render(request, "core/index.html", context)
