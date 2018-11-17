from django import forms


class LocalizationForm(forms.Form):
    localization = forms.CharField()