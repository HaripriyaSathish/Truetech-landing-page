from .models import NavLink, SiteSettings


def site_context(request):
    """Makes site_settings and nav_links available in every template without
    every view having to fetch them manually."""
    return {
        "site_settings": SiteSettings.objects.first(),
        "nav_links": NavLink.objects.filter(is_active=True),
    }
