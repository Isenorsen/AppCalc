from django import forms

class ContactForm(forms.Form):

    # from_email = forms.EmailField(required=True)
    emailto = forms.EmailField(required=True)
    subjectt = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)