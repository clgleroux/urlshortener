from django import forms
from django.utils.translation import gettext_lazy as _


class UrlForm(forms.Form):
    your_url = forms.URLField(
        label='',
        max_length=2000,
        widget=forms.URLInput(attrs={
            'class': 'input-group-field',
            'placeholder': _('Insert your URL here'),
            }))
