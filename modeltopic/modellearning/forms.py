from django import forms

class Formname(forms.Form):
    name= forms.CharField()
    email = forms.EmailField()
    text = forms.EmailField(widget=forms.Textarea)
    botcather = forms.CharField(required=False,widget=forms.HiddenInput)
