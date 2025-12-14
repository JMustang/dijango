from django import forms

from .models import Todo


class PersonForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Nome")
    age = forms.IntegerField(label="Idade")
    job = forms.CharField(max_length=100, required=True, label="trabalho")


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ["title", "description", "done", "deadline", "priority"]

        widgets = {"deadline": forms.DateInput(attrs={"type": "date"})}
