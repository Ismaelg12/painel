from controle_usuarios.models import Usuario

#verificar se basico estA LOGADO para mostrar opções no menu
def verificar_basico_logado(request):
	usuario = ""
	if request.user.is_authenticated:
		usuario = Usuario.objects.filter(
			user=request.user,tipo=1)
		
	context = {'basico':usuario}
	return context

#verificar se profissional estA LOGADO para mostrar opções no menu
def verificar_usuario_logado(request):
	usuario = ""
	if request.user.is_authenticated:
		usuario = Usuario.objects.filter(
			user=request.user,tipo=2)
		
	context = {'usuario_logado':usuario}
	return context