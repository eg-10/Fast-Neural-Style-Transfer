from django import forms

class UploadContentForm(forms.Form):
    file = forms.ImageField()