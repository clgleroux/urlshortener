from django import forms
from django.utils.translation import gettext_lazy as _

from .models import URL


class URLForm(forms.Form):
    your_url = forms.URLField(
        label='',
        max_length=2000,
        widget=forms.URLInput(attrs={
            'class': 'input-group-field',
            'placeholder': _('Insert your URL here'),
            }))

    def save(self, *args, **kwargs):
        return URL.get_or_create(self.cleaned_data['your_url'])
