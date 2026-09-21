from django import forms

from .models import Enquiry, ServiceLine


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ["full_name", "company", "email", "phone", "service", "requirement"]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "company": forms.TextInput(attrs={"placeholder": "Company name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@company.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "With country code"}),
            "requirement": forms.Textarea(attrs={"placeholder": "Volumes, hours of cover, systems involved, timelines", "rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        service_titles = ServiceLine.objects.filter(is_active=True).values_list("title", flat=True)
        choices = [("", "Select a service")] + [(title, title) for title in service_titles]
        self.fields["service"] = forms.ChoiceField(choices=choices, required=False)
