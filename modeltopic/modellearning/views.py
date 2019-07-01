from django.shortcuts import render

# Create your views here.
from . import forms

def formcall(request):
    formtag=forms.Formname()

    if request.method=='POST':
        formtag=forms.Formname(request.POST)

        if formtag.is_valid():
            print("validation success")
            print("name :" +formtag.cleaned_data['name'])
            print("text :" +formtag.cleaned_data['text'])
            print("email :" +formtag.cleaned_data['email'])

    return render(request,'modellearning/formcall.html',{'formtag':formtag})

def index(request):
    return render(request,'modellearning/index.html')
