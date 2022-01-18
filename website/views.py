from django.db.models import Count,Q,Sum
from django.shortcuts import render, redirect
from core.models import Prefeitura, Diario, Boletim
from datetime import date
from django.utils import timezone	

def nota(request):
	prefeitura          = Prefeitura.objects.all()[0]
	context = {
			'cidade':prefeitura,
			}
	return render(request, 'nota.html', context)

def site(request):
	prefeitura          = Prefeitura.objects.all()[0]
	dados     = Diario.objects.all().order_by('criado_em').last()
	boletins  = Boletim.objects.filter(status=True).order_by('-id')
	criacao = timezone.now()


	##################GRÁFICO DIÁRIO#########################
	conf_dia          = Diario.objects.filter(status=True).order_by('criado_em')
	last_update       = Diario.objects.filter(status=True).order_by('criado_em').last()
	diario_conf_lista = []
	diario_obt_lista = []
	diario_rec_lista = []
	diario_conf_dia_lista = []

	atl_list = []
	for c in conf_dia:
		diario_conf_lista.append(c.confirmado)
		diario_obt_lista.append(c.obito)
		diario_rec_lista.append(c.recuperado)		
		atl_list.append(c.criado_em.strftime('%d/%m'))
	
	for y in conf_dia:
		linha1 = []
		linha2 = []
		linha1.append(y.criado_em.strftime('%d/%m'))
		for x in range(1):
			linha1.append(y.conf_por_dia)
			linha2.append(y.conf_por_dia)
		diario_conf_dia_lista.append(linha1+linha2)
	diario_conf_dia_lista.insert(0,['','Confirmados','Confirmados'])


	context = {
		'boletins':boletins,
        'cidade':prefeitura,
        'dados':dados,
		'incidencia':(dados.confirmado/prefeitura.populacao)*10000,
		'mortalidade':(dados.obito/prefeitura.populacao)*100000,
		'tx_letalidade':(dados.obito/dados.confirmado)*100,
		'tx_recuperados': (dados.recuperado/dados.confirmado)*100,
		'tx_isolados': (dados.isolado/dados.confirmado)*100,
        'criacao':criacao.strftime('%d/%m/%y'),  
        ############VARIAVEIS GRÁFICO DIA#################
     	'conf_dia':diario_conf_lista,
		'atl_dia':atl_list,
		'rec_dia':diario_rec_lista,
		'obt_dia':diario_obt_lista,
		'conf_por_dia':diario_conf_dia_lista,
		'last_update':last_update,      
    }
	return render(request, 'index.html', context)


