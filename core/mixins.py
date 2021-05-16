# -*- coding: utf-8 -*-
from django.db.models import Count,Q,Sum
from django.http import JsonResponse
from core.models import Caso,Bairro, Comorbidade, Prefeitura
from django.utils import timezone
from controle_usuarios.models import Usuario
import json
import random 

class DashboardMixin(object):
    def estatistica_bairro(self):
        c = Bairro.objects.all().annotate(conf=Count('caso',filter=Q(caso__confirmado=True,caso__residente=True)),
            cur=Count('caso',filter=Q(caso__recuperado=True,caso__residente=True)),
            obit=Count('caso',filter=Q(caso__obito=True,caso__residente=True)),isol=Count('caso',filter=Q(caso__isolado=True,caso__residente=True)),
            int=Count('caso',filter=Q(caso__internado=True,caso__residente=True)),
            uti=Count('caso',filter=Q(caso__uti=True,caso__residente=True)))
        return c 

    def cidade(self):
        city         = Prefeitura.objects.all()[0]  
        return city

    def confirmados(self):
        confirmado_count = Caso.objects.filter(confirmado=True,residente=True).count()
        return confirmado_count

    def recuperados(self):
        recuperado_count = Caso.objects.filter(recuperado=True,residente=True).count()
        return recuperado_count

    def obitos(self):
        obito_count = Caso.objects.filter(obito=True,residente=True).count()
        return obito_count

    def isolados(self):
        isolado_count = Caso.objects.filter(isolado=True,residente=True).count()
        return isolado_count

    def internados(self):
        internado_count = Caso.objects.filter(internado=True,residente=True).count()
        return internado_count

    def utis(self):
        uti_count = Caso.objects.filter(uti=True,residente=True).count()
        return uti_count

class ChartMixin(object):
    #listagem de casos por bairro
    colors = ['#FCD202','#FF9E01','#B0DE09','#FF0F00']

    def drag_chart(self):
       
        q = Bairro.objects.values('nome').annotate(
            confirmaded=Count('caso',filter=Q(caso__confirmado=True)))
        cases_list = [obj for obj in q]
        
        for i in range(0,len(cases_list)):
            color_ramdom = random.randint(0, len(cases_list))#sortea um numero aleatorio
            cases_list[i].update({'color': self.colors[color_ramdom],})
     
        return json.dumps(cases_list)

    def donut_chart(self):
        #porcentagem de casos por sexo
        cases = Caso.objects.values('sexo').annotate(cnt=Count('sexo')).order_by('sexo')
        total_items = Caso.objects.count()
        cases_list = [
            {'sexo': g['sexo'], 'porcentagem': g['cnt'] * 100 / total_items} for g in cases
        ]
        return json.dumps(cases_list)