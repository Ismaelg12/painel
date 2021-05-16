from django.contrib import admin
from controle_usuarios.models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
	list_display = ['user','nome','sobrenome','tipo','data_cadastro','email', 'ativo'] 
	search_fields = ['nome']
admin.site.register(Usuario,UsuarioAdmin)
