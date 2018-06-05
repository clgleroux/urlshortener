from django import forms

class UrlForm(forms.Form):
	your_url = forms.URLField(label='Your URL', max_length=200)

class AliasForm(forms.Form):
	your_alias = forms.CharField(label='Your Alias', max_length=4)

class NameForm(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100)
	

