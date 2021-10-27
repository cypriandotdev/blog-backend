from django import forms


class ContentForm(forms.Form):
    content = forms.Textarea()
