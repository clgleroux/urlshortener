from django import forms
from django.utils.translation import ugettext_lazy


class UrlForm(forms.Form):
    your_url = forms.URLField(label=ugettext_lazy('Your URL'), max_length=2000)
