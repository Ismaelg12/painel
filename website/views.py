from django.db.models import Count,Q,Sum
from django.shortcuts import render, redirect
from core.models import Prefeitura, Diario, Caso, Media, Conf_mes, Obitos_mes, Comorbidade
from datetime import date
from django.utils.timezone import now

def nota(request):
	prefeitura          = Prefeitura.objects.all()[0]
	context = {
			'cidade':prefeitura,
			}
	return render(request, 'nota.html', context)

def site(request):
	prefeitura          = Prefeitura.objects.all()[0]
	conf_dia			= Diario.objects.all().last()
	obt_dia				= Media.objects.all().last()
	confirmado_count    = Caso.objects.filter(confirmado=True,residente=True).count()
	recuperado_count    = Caso.objects.filter(recuperado=True,residente=True).count()
	obito_count         = Caso.objects.filter(obito=True,residente=True).count()
	internado_count     = Caso.objects.filter(internado=True,residente=True).count()
	uti_count           = Caso.objects.filter(uti=True,residente=True).count()
	##################GRAFICO DONUT CASOS POR IDADE ########################
	etaria_zero         =  age_range_resid(0,10,False)
	etaria_um         	=  age_range_resid(10,20,False)
	etaria_dois         =  age_range_resid(20,30,False)
	etaria_tres         =  age_range_resid(30,40,False)
	etaria_quatro       =  age_range_resid(40,50,False)
	etaria_cinco        =  age_range_resid(50,60,False)
	etaria_seis         =  age_range_resid(60,70,False)
	etaria_sete         =  age_range_resid(70,80,False)
	etaria_oito         =  age_range_resid(80,120,False)

	##################GRAFICO DONUT OBITO POR IDADE ########################
	etaria_obt_zero         =  age_range_resid(0,10,True)
	etaria_obt_um         	=  age_range_resid(10,20,True)
	etaria_obt_dois         =  age_range_resid(20,30,True)
	etaria_obt_tres         =  age_range_resid(30,40,True)
	etaria_obt_quatro       =  age_range_resid(40,50,True)
	etaria_obt_cinco        =  age_range_resid(50,60,True)
	etaria_obt_seis         =  age_range_resid(60,70,True)
	etaria_obt_sete         =  age_range_resid(70,80,True)
	etaria_obt_oito         =  age_range_resid(80,120,True)

	##################GRAFICO DONUT RECUPRADOS POR IDADE ########################
	etaria_rec_zero         =  age_range_resid(0,10,None)
	etaria_rec_um         	=  age_range_resid(10,20,None)
	etaria_rec_dois         =  age_range_resid(20,30,None)
	etaria_rec_tres         =  age_range_resid(30,40,None)
	etaria_rec_quatro       =  age_range_resid(40,50,None)
	etaria_rec_cinco        =  age_range_resid(50,60,None)
	etaria_rec_seis         =  age_range_resid(60,70,None)
	etaria_rec_sete         =  age_range_resid(70,80,None)
	etaria_rec_oito         =  age_range_resid(80,120,None)

	##################GRAFICO BAR CASOS  POR SEXO ########################
	obito_sexo_m     =  Caso.objects.filter(obito=True,sexo='M',residente=True).count()
	obito_sexo_f     =  Caso.objects.filter(obito=True,sexo='F',residente=True).count()
	
	##################GRAFICO DONUT CONFIRMADOS POR SEXO ########################
	conf_sexo_m     =  Caso.objects.filter(confirmado=True,sexo='M',residente=True).count()
	conf_sexo_f     =  Caso.objects.filter(confirmado=True,sexo='F',residente=True).count()

	##################GRAFICO DONUT CONFIRMADOS POR SEXO ########################
	rec_sexo_m     =  Caso.objects.filter(recuperado=True,sexo='M',residente=True).count()
	rec_sexo_f     =  Caso.objects.filter(recuperado=True,sexo='F',residente=True).count()


	# #Gráfico casos confirmados por mes
	# casos_mes	        = Conf_mes.objects.filter(status_conf_mes=True).order_by('id')
	
	
	# conf_mes = []
	# total_conf_mes = []
	# media_conf_mes = []
	

	# for m in casos_mes:
	# 	conf_mes.append(m.conf_mes)
	# 	total_conf_mes.append(m.total_conf_mes)
	# 	media_conf_mes.append(m.media_conf_mes)

	#Gráfico óbitos confirmados por mes
	obt_mes	        = Obitos_mes.objects.filter(status_obitos_mes=True).order_by('id')
	
	
	obitos_mes = []
	total_obitos_mes = []
	media_obitos_mes = []
	

	for o in obt_mes:
		obitos_mes.append(o.obitos_mes)
		total_obitos_mes.append(o.total_obitos_mes)
		media_obitos_mes.append(o.media_obitos_mes)

	#GRÁFICO MÉDIA MOVEL
	media_dia	        = Media.objects.filter(status=True).order_by('media_dia')
	
	
	media_conf_lista = []
	tx_conf_lista = []
	media_obt_lista = []
	tx_obt_lista = []
	media_lista = []
	

	for d in media_dia:
		media_conf_lista.append(d.media_conf)
		tx_conf_lista.append(d.tx_conf)
		media_obt_lista.append(d.media_obt)
		tx_obt_lista.append(d.tx_obt)		
		media_lista.append(d.media_dia.strftime('%d/%m'))

	#GRAFICO CONFIRMADOS POR MES 
	conf_mes          = Conf_mes.objects.filter(status_conf_mes=True).order_by('criado_em')

	mes_conf_list = []
	for c in conf_mes:
		linha1 = []
		linha2 = []
		linha3 = []
		for x in range(1):
			linha1.append(c.conf_mes)
			linha2.append(c.total_conf_mes)
			linha3.append(c.media_conf_mes)
		mes_conf_list.append(linha1+linha2+linha3)		
	mes_conf_list.insert(0,['Mes','Confirmado','Média Móvel'])
	print('lista de mes',mes_conf_list)

	#GRAFICO ÓBITOS POR MES 
	obitos_mes          = Obitos_mes.objects.filter(status_obitos_mes=True).order_by('criado_em')

	mes_obt_list = []
	for ob in obitos_mes:
		linha1 = []
		linha2 = []
		linha3 = []
		for x in range(1):
			linha1.append(ob.obitos_mes)
			linha2.append(ob.total_obitos_mes)
			linha3.append(ob.media_obitos_mes)
		mes_obt_list.append(linha1+linha2+linha3)		
	mes_obt_list.insert(0,['Mes','Obitos','Média Móvel'])
	
	##################GRAFICO COMORBIDADE X ÓBITO #####################

	cm_obt                  = Comorbidade.objects.all().annotate(
		cm_obt=Count('caso',filter=Q(caso__obito=True,caso__residente=True,)))
	cm_obt_lista      = []
	for y in cm_obt:
		linha = []
		linha.append(y.tipo)
		for x in range(1):
		   linha.append(y.cm_obt)
		cm_obt_lista.append(linha)
	cm_obt_lista.insert(0,['', 'Total'])


	context = {
			'cidade':prefeitura,
			'conf_dia':conf_dia,
			'obt_dia':obt_dia,
			'confirmado':confirmado_count,
			'recuperado':recuperado_count,
			'obito':obito_count,
			'internado':internado_count,
			'uti':uti_count,
			'hospitalizacao':internado_count+uti_count,
			'incidencia':(confirmado_count/prefeitura.populacao)*10000,
			'mortalidade':(obito_count/prefeitura.populacao)*100000,
			'tx_letalidade':(obito_count/confirmado_count)*100,
			'tx_recuperados': (recuperado_count/confirmado_count)*100,
			'casos_obito_sexo_m':obito_sexo_m,
			'casos_obito_sexo_f':obito_sexo_f,
			'casos_conf_sexo_m':conf_sexo_m,
			'casos_conf_sexo_f':conf_sexo_f,
			'casos_rec_sexo_m':rec_sexo_m,
			'casos_rec_sexo_f':rec_sexo_f,
		################## VARIÁVEL GRAFICO DONUT CONFIRMADOS POR IDADE ########################
			'etaria_zero':etaria_zero,
			'etaria_um':etaria_um,
			'etaria_dois':etaria_dois,
			'etaria_tres':etaria_tres,
			'etaria_quatro':etaria_quatro,
			'etaria_cinco':etaria_cinco,
			'etaria_seis':etaria_seis,
			'etaria_sete':etaria_sete,
			'etaria_oito':etaria_oito,
		################## VARIÁVEL GRAFICO DONUT OBITOS POR IDADE ########################
			'etaria_obt_zero':etaria_obt_zero,
			'etaria_obt_um':etaria_obt_um,
			'etaria_obt_dois':etaria_obt_dois,
			'etaria_obt_tres':etaria_obt_tres,
			'etaria_obt_quatro':etaria_obt_quatro,
			'etaria_obt_cinco':etaria_obt_cinco,
			'etaria_obt_seis':etaria_obt_seis,
			'etaria_obt_sete':etaria_obt_sete,
			'etaria_obt_oito':etaria_obt_oito,
			################## VARIÁVEL GRAFICO DONUT RECUPERADOS POR IDADE ########################
			'etaria_rec_zero':etaria_rec_zero,
			'etaria_rec_um':etaria_rec_um,
			'etaria_rec_dois':etaria_rec_dois,
			'etaria_rec_tres':etaria_rec_tres,
			'etaria_rec_quatro':etaria_rec_quatro,
			'etaria_rec_cinco':etaria_rec_cinco,
			'etaria_rec_seis':etaria_rec_seis,
			'etaria_rec_sete':etaria_rec_sete,
			'etaria_rec_oito':etaria_rec_oito,
			###### VARIÁVIS MEDIA CONF/OBT
			'media_conf':media_conf_lista,
			'tx_conf':tx_conf_lista,
			'media_obt':media_obt_lista,
			'tx_obt':tx_obt_lista,
			'media_dia':media_lista,
			###### VARIÁVIS MES CONF/OBT
			'mes_conf_list':mes_conf_list,
			'mes_obt_list':mes_obt_list,
			#### VARIAVEIS ÓBITOS POR MORBIDADE
			'cm_obt_lista':cm_obt_lista
			}
	return render(request, 'index.html', context)

def age_range_resid(min_age, max_age,is_obite):
	current = now().date()
	result = ''
	min_date = date(current.year - min_age, current.month, current.day)
	max_date = date(current.year - max_age, current.month, current.day)
	if is_obite == True:
		result = Caso.objects.filter(obito=True, residente=True,data_nascimento__gte=max_date,
		data_nascimento__lte=min_date).order_by("data_nascimento").count()
	if is_obite == False:
		result = Caso.objects.filter(confirmado=True,residente=True,data_nascimento__gte=max_date,
		data_nascimento__lte=min_date).order_by("data_nascimento").count()
	if is_obite == None:
		result = Caso.objects.filter(recuperado=True,residente=True,data_nascimento__gte=max_date,
		data_nascimento__lte=min_date).order_by("data_nascimento").count()
		
	return result

