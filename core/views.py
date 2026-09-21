from django.shortcuts import render

from .models import AutomationSection, HeroFeature, HeroSection, Service


def index(request):
    context = {
        "hero": HeroSection.objects.filter(is_active=True).first(),
        "hero_features": HeroFeature.objects.filter(is_active=True),
        "automation": AutomationSection.objects.filter(is_active=True).first(),
        "services": Service.objects.filter(is_active=True),
    }
    return render(request, "core/index.html", context)
