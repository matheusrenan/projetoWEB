from django.shortcuts import render
from .forms import contatosForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def contatos(request):
	titulo = 'Contato'
	form = contatosForm(request.POST or None)
	confirm_message = None

	if form.is_valid():
		nome = form.cleaned_data['nome']
		comentario = form.cleaned_data['comentario']
		assunto = 'Mensagem do meu site'
		mensagem = '%s %s' %(comentario, nome)
		emailRemetente = form.cleaned_data['email']
		emailDestinatario = [settings.EMAIL_HOST_USER]
		send_mail(assunto, mensagem, emailRemetente, emailDestinatario, fail_silently=True)
		titulo = 'Obrigado !!'
		confirm_message = 'Obrigado pela mensagem, logo responderemos você'
		form = None
		
	context = {'titulo': titulo, 'form': form, 'confirm_message': confirm_message, }
	template = 'contatos.html'
	return render(request, template, context)
