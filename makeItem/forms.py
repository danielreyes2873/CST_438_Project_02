from django import forms

class CreateItemForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    price = forms.CharField(label='price', max_length=20)
    url = forms.CharField(label='url', max_length=300)
    urlimage = forms.CharField(label='urlImage', max_length=300)
