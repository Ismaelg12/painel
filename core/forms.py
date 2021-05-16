from django import forms
from django.forms import ModelForm
from core.models import Caso, Bairro, Comorbidade, Diario, Ubs, Teste, Media, Obitos_mes, Conf_mes
from django.core.exceptions import ValidationError
from controle_usuarios.models import Usuario

OP_CHOICES = (
    ('', 'Selecione . . .'),
    (True, 'Sim'),
    (False, 'Não')
)

class CasoForm(forms.ModelForm):
    class Meta:
        model =  Caso
        fields = '__all__'
        widgets = {
            'nome'              : forms.TextInput(attrs={'class': 'form-control','required': 'true' }),
            'data_nascimento'   : forms.DateInput(attrs={'class': 'form-control','required': 'true'}),
			'sexo'              : forms.Select(attrs={'class': 'form-control','required': 'true'}),
            'residente'         : forms.Select(choices=OP_CHOICES,attrs={'class': 'form-control','required': 'true'}),
            'cpf'              : forms.TextInput(attrs={'class': 'form-control'}),
            #endereço
            'bairro'            : forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,
                'data-live-search':'true','required': 'true','onchange':'showDiv(this)','id':'id_bairro',}),
            #informações clinicas do paciente
            'data_notificacao'  : forms.DateInput(attrs={'class': 'form-control'}),
            'comorbidade'       : forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,
                'data-live-search':'true','onchange':'showDiv(this)','id':'id_comorbidade',}),
            'recuperado'        : forms.Select(choices=OP_CHOICES,attrs={'class': 'form-control'}),
            'obito'             : forms.Select(choices=OP_CHOICES,attrs={'class': 'form-control'}),
            'isolado'           : forms.Select(choices=OP_CHOICES,attrs={'class': 'form-control'}),
            'internado'         : forms.Select(choices=OP_CHOICES,attrs={'class': 'form-control'}),
            'uti'               : forms.Select(choices=OP_CHOICES,attrs={'class': 'form-control'}),
            'confirmado'               : forms.Select(choices=OP_CHOICES,attrs={'class': 'form-control'}),
            'observacao'        : forms.Textarea(attrs={'class': 'form-control','cols' : "10", 'rows': "3",}),
            'ubs'            : forms.Select(attrs={'class':'selectpicker',
                'data-style':'select-with-transition','data-size':7,
                'data-live-search':'true','onchange':'showDiv(this)','id':'id_ubs',}),
        }


class BairroForm(forms.ModelForm):
    class Meta:
        model =  Bairro
        fields = '__all__'
        widgets = {
            'nome'      : forms.TextInput(attrs={'class': 'form-control','required': 'true' }),
            'cidade'    : forms.TextInput(attrs={'class': 'form-control','required': 'true' }), 
            'latitude'    : forms.TextInput(attrs={'class': 'form-control' }), 
            'longitude'    : forms.TextInput(attrs={'class': 'form-control' }), 
        }

class TesteForm(forms.ModelForm):
    class Meta:
        model =  Teste
        fields = '__all__'
        widgets = {
            'total'      : forms.TextInput(attrs={'class': 'form-control','required': 'true' }),
            'descartado' : forms.TextInput(attrs={'class': 'form-control','required': 'true' }),  
        }

class ComorbidadeForm(forms.ModelForm):
    class Meta:
        model =  Comorbidade
        fields = '__all__'
        widgets = {
            'tipo'      : forms.TextInput(attrs={'class': 'form-control','required': 'true' }),
        }

class DiarioForm(forms.ModelForm):
    class Meta:
        model =  Diario
        fields = '__all__'
        widgets = {
            'confirmado'        : forms.TextInput(attrs={'class': 'form-control','required': 'true' }),
            'recuperado'        : forms.TextInput(attrs={'class': 'form-control','required': 'true' }), 
            'obito'             : forms.TextInput(attrs={'class': 'form-control','required': 'true' }), 
            'criado_em'         : forms.DateInput(attrs={'class': 'form-control','required': 'true'}), 
            'conf_por_dia'      : forms.TextInput(attrs={'class': 'form-control','required': 'true'}), 
            'obt_por_dia'       : forms.TextInput(attrs={'class': 'form-control','required': 'true'}), 
        }

class MediaForm(forms.ModelForm):
    class Meta:
        model =  Media
        fields = '__all__'
        widgets = {
            'media_conf'        : forms.TextInput(attrs={'class': 'form-control','required': 'true' }),
            'tx_conf'           : forms.TextInput(attrs={'class': 'form-control','required': 'true' }), 
            'media_obt'         : forms.TextInput(attrs={'class': 'form-control','required': 'true' }), 
            'tx_obt'            : forms.TextInput(attrs={'class': 'form-control','required': 'true'}), 
            'media_dia'         : forms.DateInput(attrs={'class': 'form-control','required': 'true'}), 
        }

class ObitosmesForm(forms.ModelForm):
    class Meta:
        model =  Obitos_mes
        fields = '__all__'
        widgets = {
            'obitos_mes'        	: forms.TextInput(attrs={'class': 'form-control','required': 'true' }),
            'total_obitos_mes'    : forms.TextInput(attrs={'class': 'form-control','required': 'true' }), 
            'media_obitos_mes'    : forms.TextInput(attrs={'class': 'form-control','required': 'true' }), 
            'status_obitos_mes'   : forms.TextInput(attrs={'class': 'form-control','required': 'true'}), 
        }

class ConfmesForm(forms.ModelForm):
    class Meta:
        model =  Conf_mes
        fields = '__all__'
        widgets = {
            'conf_mes'        	: forms.TextInput(attrs={'class': 'form-control','required': 'true' }),
            'total_conf_mes'    : forms.TextInput(attrs={'class': 'form-control','required': 'true' }), 
            'media_conf_mes'    : forms.TextInput(attrs={'class': 'form-control','required': 'true' }), 
            'status_conf_mes'   : forms.TextInput(attrs={'class': 'form-control','required': 'true'}), 
        }