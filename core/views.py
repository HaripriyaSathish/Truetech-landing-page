from django.shortcuts import render

from .models import HeroSection, Service, SiteSettings


def index(request):
    context = {
        "site_settings": SiteSettings.objects.first(),
        "hero": HeroSection.objects.filter(is_active=True).first(),
        "services": Service.objects.filter(is_active=True),
    }
    return render(request, "core/index.html", context)
