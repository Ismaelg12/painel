from django.db import models
from core.utils import UF, SEXO, PERGUNTA
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from django.db import models
from django.utils import timezone

class Prefeitura(models.Model):
	orgao   	= models.CharField(max_length=100,blank=True)
	cnpj       	= models.CharField(max_length=18,blank=True)
	logo  		= models.ImageField(upload_to='media')
	secretaria  = models.CharField(max_length=100,blank=True)
	coordenacao	= models.CharField(max_length=100,blank=True)		
	cep   		= models.CharField(max_length=10,blank=True)
	uf          = models.CharField(max_length=2,choices=UF,default='PI')	
	cidade   	= models.CharField(max_length=100,blank=True)
	rua   		= models.CharField(max_length=100,blank=True)
	numero   	= models.CharField(max_length=100,blank=True)
	bairro   	= models.CharField(max_length=100,blank=True)
	fonte		= models.CharField(max_length=100,blank=True)
	populacao	= models.IntegerField()


	class Meta:
		verbose_name = 'Município'
		verbose_name_plural = 'Municípios'
		
	def __str__(self):
		return self.orgao

class Bairro(models.Model):
	nome   	= models.CharField(max_length=100,blank=True,unique=True)
	cidade 	= models.CharField(max_length=100,blank=True)
	latitude 	= models.CharField(max_length=15,blank=True)
	longitude 	= models.CharField(max_length=15,blank=True)

	class Meta:
		verbose_name = 'Bairro'
		verbose_name_plural = 'Bairros'
		
	def __str__(self):
		return self.nome

class Comorbidade(models.Model):
	tipo   	= models.CharField(max_length=100,blank=True,unique=True)

	class Meta:
		verbose_name = 'Comorbidade'
		verbose_name_plural = 'Comorbidades'
		
	def __str__(self):
		return self.tipo

class Ubs(models.Model):
	nome   	= models.CharField(max_length=100,blank=True,unique=True)

	class Meta:
		verbose_name = 'Ubs'
		verbose_name_plural = 'Ubs'
		
	def __str__(self):
		return self.nome

class Teste(models.Model):
	total   	= models.CharField(max_length=10,blank=True,unique=True)
	descartado 	= models.CharField(max_length=10,blank=True,unique=True)

	class Meta:
		verbose_name = 'Teste'
		verbose_name_plural = 'Teste_rápido'
		
	def __str__(self):
		return self.total

class Caso(models.Model):
	#informações basicas do paciente
	nome   				= models.CharField(max_length=100,blank=True,unique=True)
	data_nascimento   	= models.DateField(blank=True,null=True)
	sexo              	= models.CharField('Sexo', max_length=1, choices=SEXO, blank=True)
	residente			= models.BooleanField('Residente',max_length=1, blank=True, default=True)
	cpf 				= models.CharField(max_length=14,blank=True)
	#bairro
	bairro      		= models.ForeignKey(Bairro,on_delete=models.PROTECT,null=True,blank=True)
	#informações clinicas do paciente
	data_notificacao	= models.DateField(blank=True,null=True)
	confirmado			= models.BooleanField('Confirmado', blank=True, default=True)
	comorbidade    		= models.ForeignKey(Comorbidade,on_delete=models.PROTECT,null=True,blank=True)
	recuperado			= models.BooleanField('Recuperado', blank=True)
	obito				= models.BooleanField('Óbito', blank=True)
	internado			= models.BooleanField('Internado', blank=True)
	uti       			= models.BooleanField('UTI', blank=True)
	observacao			= models.TextField('Observação',blank=True)
	ubs		      		= models.ForeignKey(Ubs,on_delete=models.PROTECT,null=True,blank=True)
	#outros
	atualizado_em     = models.DateField('Atualizado em', auto_now=True)
	criado_em         = models.DateField('Criado em', auto_now_add=True)

	def get_idade(self):
		return int((datetime.now().date()-self.data_nascimento).days/365.25)
	
	class Meta:
		verbose_name = 'Caso'
		verbose_name_plural = 'Casos'
		ordering = ('criado_em',)
		
	def __str__(self):
		return self.nome

class Diario(models.Model):
	confirmado   	= models.IntegerField() #Fazer um count da tabela casos
	conf_por_dia   	= models.IntegerField()	#Fazer uma agreggation da tabela casos com os casos novos do dia (criado_em)
	obito   		= models.IntegerField()	#Fazer um count da tabela casos
	recuperado   	= models.IntegerField()	#Fazer um count da tabela casos
	criado_em       = models.DateField('Criado em',default= timezone.now())
	status			= models.BooleanField('Status', blank=True, default=True)

	class Meta:
		verbose_name = 'Diario'
		verbose_name_plural = 'Informe_diário'
		
	def __str__(self):
		return str(self.confirmado)

class Semana(models.Model):
	semana 	  		= models.CharField(max_length=100,blank=True)
	conf_sm   		= models.IntegerField()
	obt_sm		   	= models.IntegerField()
	trans_sm		= models.FloatField()
	status			= models.BooleanField('Status', blank=True, default=True)

	class Meta:
		verbose_name = 'Semana_Epidemiologica'
		verbose_name_plural = 'Semana_epidemiológica'
		
	def __str__(self):
		return self.semana

class Media(models.Model):
	media_dia 	  	= models.DateField(blank=True,null=True)
	media_conf 	  	= models.IntegerField()
	tx_conf   		= models.FloatField()
	media_obt	  	= models.IntegerField()
	tx_obt   		= models.FloatField()
	status			= models.BooleanField('Status', blank=True, default=True)

	class Meta:
		verbose_name = 'Media_dia'
		verbose_name_plural = 'Media_móvel'
		
class Obitos_mes(models.Model):
	obitos_mes 	  		= models.CharField(max_length=100,blank=True,unique=True)
	total_obitos_mes 	= models.IntegerField()
	media_obitos_mes		= models.FloatField()
	status_obitos_mes	= models.BooleanField('Status', blank=True, default=True)
	criado_em       = models.DateField('Criado em',default= timezone.now())

	class Meta:
		verbose_name = 'obitos_mes'
		verbose_name_plural = 'Obitos_mes'

class Conf_mes(models.Model):
	conf_mes 	  		= models.CharField(max_length=100,blank=True,unique=True)
	total_conf_mes 		= models.IntegerField()
	media_conf_mes		= models.FloatField()
	status_conf_mes		= models.BooleanField('Status', blank=True, default=True)
	criado_em       = models.DateField('Criado em',default= timezone.now())

	class Meta:
		verbose_name = 'conf_mes'
		verbose_name_plural = 'Conf_mes'