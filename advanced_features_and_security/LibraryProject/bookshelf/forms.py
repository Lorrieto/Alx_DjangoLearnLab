rom django import forms
from .models import Book  # or any model you want to use with the form

# Example form using Django's Form class
class ExampleForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')
