from django import forms

class UploadFileForm(forms.Form):
    Archivo = forms.FileField()