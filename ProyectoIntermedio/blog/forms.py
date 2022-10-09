from django import forms


class AutorFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.IntegerField()