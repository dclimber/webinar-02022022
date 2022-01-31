from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    message = forms.CharField(
        required=False,
        widget=forms.Textarea()
    )
