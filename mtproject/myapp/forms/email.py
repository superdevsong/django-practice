from django import forms

#email form
class Email(forms.Form):
    email = forms.EmailField()
    
    
    

