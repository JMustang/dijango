from django import forms


class PersonForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Nome")
    age = forms.IntegerField(label="Idade")
    job = forms.CharField(max_length=100, required=True, label="trabalho")
