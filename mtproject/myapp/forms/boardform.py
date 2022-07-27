from django import forms

#boardform
class BoardForm(forms.Form):
    title = forms.CharField(max_length=20)
    body = forms.Textarea()