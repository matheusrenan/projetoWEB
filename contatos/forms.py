from django import forms

class contatosForm(forms.Form):
	nome = forms.CharField(required=False, max_length=100, help_text='Máximo de 100 caracteres')
	email = forms.EmailField(required=True)
	comentario = forms.CharField(required=True, widget=forms.Textarea)