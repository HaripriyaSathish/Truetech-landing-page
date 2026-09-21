from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# Built-in icon glyphs for Service.icon_key, so sections don't need icon
# image assets uploaded for every card — just pick a key in the admin.
_ICONS = {
    "monitor": (
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="13" rx="2"/>'
        '<path d="M8 21h8M12 17v4"/></svg>'
    ),
    "refresh": (
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-3-6.7"/>'
        '<path d="M21 4v6h-6"/></svg>'
    ),
    "document": (
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>'
        '<path d="M14 2v6h6M9 13h6M9 17h6"/></svg>'
    ),
    "grid": (
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1"/>'
        '<rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/>'
        '<rect x="14" y="14" width="7" height="7" rx="1"/></svg>'
    ),
}


@register.simple_tag
def service_icon(icon_key):
    return mark_safe(_ICONS.get(icon_key, _ICONS["monitor"]))
