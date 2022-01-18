from django.contrib import admin
from core.models import Prefeitura, Diario, Boletim

class PrefeituraAdmin(admin.ModelAdmin):
	list_display = ['orgao','cidade','secretaria','coordenacao'] 


class BoletimAdmin(admin.ModelAdmin):
	list_display = ['upload_em','boletim','status'] 

# class CasoAdmin(admin.ModelAdmin):
# 	list_display = ['nome','bairro','confirmado','recuperado','isolado',
# 	'obito','comorbidade','sexo'] 
# 	search_fields  = ['nome','bairro',]

# class BairroAdmin(admin.ModelAdmin):
# 	list_display = ['nome','cidade','latitude', 'longitude'] 
# 	search_fields  = ['nome']

# class ComorbidadeAdmin(admin.ModelAdmin):
# 	list_display = ['id','tipo'] 
# 	search_fields  = ['tipo']

class DiarioAdmin(admin.ModelAdmin):
	list_display = ['criado_em','realizado','descartado','isolado','confirmado','conf_por_dia','recuperado','leito_suspeito','leito_positivo','uti_suspeito','uti_positivo','obito','obt_por_dia'] 
	
# class UbsAdmin(admin.ModelAdmin):
# 	list_display = ['id','nome']
# 	search_fields  = ['nome'] 

# class TesteAdmin(admin.ModelAdmin):
# 	list_display = ['id','total','descartado']

# class SemanaAdmin(admin.ModelAdmin):
# 	list_display = ['id','semana','conf_sm','obt_sm','trans_sm']

# class MediaAdmin(admin.ModelAdmin):
# 	list_display = ['id','media_dia','media_conf','tx_conf','media_obt', 'tx_obt']

# class Conf_mesAdmin(admin.ModelAdmin):
# 	list_display = ['id','conf_mes','total_conf_mes','media_conf_mes','status_conf_mes','criado_em']

# class Obitos_mesAdmin(admin.ModelAdmin):
# 	list_display = ['id','obitos_mes','total_obitos_mes','media_obitos_mes','status_obitos_mes','criado_em']

admin.site.register(Prefeitura,PrefeituraAdmin)
admin.site.register(Boletim,BoletimAdmin)
# admin.site.register(Caso,CasoAdmin)
# admin.site.register(Comorbidade,ComorbidadeAdmin)
admin.site.register(Diario,DiarioAdmin)
# admin.site.register(Ubs,UbsAdmin)
# admin.site.register(Teste,TesteAdmin)
# admin.site.register(Semana,SemanaAdmin)
# admin.site.register(Media,MediaAdmin)
# admin.site.register(Conf_mes,Conf_mesAdmin)
# admin.site.register(Obitos_mes,Obitos_mesAdmin)