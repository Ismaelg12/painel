from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Count
from django.views.generic import ListView,CreateView,TemplateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from core.models import Caso, Bairro, Comorbidade, Diario, Prefeitura, Teste, Media
from core.forms import CasoForm, BairroForm, ComorbidadeForm, DiarioForm, TesteForm, MediaForm
from core.mixins import DashboardMixin,ChartMixin
from django.contrib import messages
from django.views.generic import TemplateView
from controle_usuarios.models import Usuario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from core.decorators import staff_member_required
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from core.render_pdf import *
from django.core.paginator import Paginator


@method_decorator(staff_member_required, name='dispatch')
class DashboardView(TemplateView,DashboardMixin,ChartMixin):
    template_name = 'dashboard.html'
    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(*args, **kwargs)
        context['is_superuser'] = self.request.user.is_superuser
        return context


    
'''                           CRUD Casos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

@method_decorator(staff_member_required, name='dispatch')
class CasoCreateView(LoginRequiredMixin,CreateView):
    model         = Caso
    template_name = 'casos/caso_add.html'
    form_class    = CasoForm
    success_url   = reverse_lazy('casos')
    #salvar e adicionar novo
    def post(self, request, *args, **kwargs):
        save_action = None
        if "cancelar" in request.POST:
            return HttpResponseRedirect(reverse('casos'))
        else:
            save_action = super(CasoCreateView, self).post(request, *args, **kwargs)
        if "adicionar_outro" in request.POST:
            messages.success(request,'Caso Cadastrado com Sucesso! ')
            return HttpResponseRedirect(reverse('add_caso'))
        return save_action


@method_decorator(staff_member_required, name='dispatch')
class CasoListView(LoginRequiredMixin,ListView):
    paginate_by = 100
    model = Caso
    context_object_name = 'casos'
    template_name = 'casos/casos.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CasoListView, self).get_context_data(*args, **kwargs)
        context['is_superuser'] = self.request.user.is_superuser
        return context
    
    def get_queryset(self, **kwargs):
        queryset = Caso.objects.select_related(
            'bairro').prefetch_related('comorbidade').all().order_by('nome')
        if self.request.GET.get('paciente'):
            paciente_search = self.request.GET.get('paciente')
            queryset = Caso.objects.filter(
                nome__icontains=paciente_search).select_related(
            'bairro').prefetch_related('comorbidade').order_by('id')
        return queryset

@method_decorator(staff_member_required, name='dispatch')
class CasoUpdateView(LoginRequiredMixin,UpdateView):
    model         = Caso
    template_name = 'casos/caso_add.html'
    form_class    = CasoForm
    success_url   = reverse_lazy('casos')

@method_decorator(staff_member_required, name='dispatch')
class CasoDeleteView(LoginRequiredMixin,DeleteView):
    model         = Caso
    success_url   = reverse_lazy('casos')
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

@login_required
def Caso_detalhe(request,pk):
    caso = Caso.objects.get(pk=pk)
    context = {
        'caso':caso,
    }
    return render(request,'casos/caso_detalhe.html',context)

'''
+                           CRUD Comorbidades
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

@method_decorator(staff_member_required, name='dispatch')
class ComorbidadeCreateView(LoginRequiredMixin,CreateView):
    model         = Comorbidade
    template_name = 'comorbidades/comorbidade_add.html'
    form_class    = ComorbidadeForm
    success_url   = reverse_lazy('comorbidades')
    #salvar e adicionar novo
    def post(self, request, *args, **kwargs):
        save_action = None
        if "cancelar" in request.POST:
            return HttpResponseRedirect(reverse('comorbidades'))
        else:
            save_action = super(ComorbidadeCreateView, self).post(request, *args, **kwargs)
        if "adicionar_outro" in request.POST:
            messages.success(request,'Comorbidade Cadastrada com Sucesso! ')
            return HttpResponseRedirect(reverse('add_comorbidade'))
        return save_action
    def get_context_data(self, *args, **kwargs):
        context = super(ComorbidadeCreateView, self).get_context_data(*args, **kwargs)
        context['is_superuser'] = self.request.user.is_superuser
        return context


@method_decorator(staff_member_required, name='dispatch')
class ComorbidadeListView(LoginRequiredMixin,ListView):
    paginate_by = 50
    model = Comorbidade
    context_object_name = 'comorbidades'
    template_name = 'comorbidades/comorbidades.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ComorbidadeListView, self).get_context_data(*args, **kwargs)
        context['is_superuser'] = self.request.user.is_superuser
        return context

    def get_queryset(self, **kwargs):
        queryset = Comorbidade.objects.all()
        if self.request.GET.get('tipo'):
            comorbidade_search = self.request.GET.get('tipo')
            queryset = Comorbidade.objects.filter(
                nome__icontains=comorbidade_search).order_by('id')
        return queryset

@method_decorator(staff_member_required, name='dispatch')
class ComorbidadeUpdateView(LoginRequiredMixin,UpdateView):
    model         = Comorbidade
    template_name = 'comorbidades/comorbidade_add.html'
    form_class    = ComorbidadeForm
    success_url   = reverse_lazy('comorbidades')

@method_decorator(staff_member_required, name='dispatch')
class ComorbidadeDeleteView(LoginRequiredMixin,DeleteView):
    model         = Comorbidade
    success_url   = reverse_lazy('comorbidades')
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

@login_required
def Comorbidade_detalhe(request,pk):
    comorbidade = Comorbidade.objects.get(pk=pk)
    context = {
        'comorbidade':comorbidade,
    }
    return render(request,'comorbidades/comorbidade_detalhe.html',context)

'''
+                           CRUD Bairros
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

@method_decorator(staff_member_required, name='dispatch')
class BairroCreateView(LoginRequiredMixin,CreateView):
    model         = Bairro
    template_name = 'bairros/bairro_add.html'
    form_class    = BairroForm
    success_url   = reverse_lazy('bairros')
    #salvar e adicionar novo
    def post(self, request, *args, **kwargs):
        save_action = None
        if "cancelar" in request.POST:
            return HttpResponseRedirect(reverse('bairros'))
        else:
            save_action = super(BairroCreateView, self).post(request, *args, **kwargs)
        if "adicionar_outro" in request.POST:
            messages.success(request,'Bairro Cadastrado com Sucesso! ')
            return HttpResponseRedirect(reverse('add_bairro'))
        return save_action

    def get_context_data(self, *args, **kwargs):
        context = super(BairroCreateView, self).get_context_data(*args, **kwargs)
        context['is_superuser'] = self.request.user.is_superuser
        return context

@method_decorator(staff_member_required, name='dispatch')
class BairroListView(LoginRequiredMixin,ListView):
    paginate_by = 50
    model = Bairro
    context_object_name = 'bairros'
    template_name = 'bairros/bairros.html'
    
    def get_queryset(self, **kwargs):
        queryset = Bairro.objects.all()
        if self.request.GET.get('nome'):
            bairro_search = self.request.GET.get('nome')
            queryset = Bairro.objects.filter(
                nome__icontains=bairro_search).order_by('id')
        return queryset

@method_decorator(staff_member_required, name='dispatch')
class BairroUpdateView(LoginRequiredMixin,UpdateView):
    model         = Bairro
    template_name = 'bairros/bairro_add.html'
    form_class    = BairroForm
    success_url   = reverse_lazy('bairros')

@method_decorator(staff_member_required, name='dispatch')
class BairroDeleteView(LoginRequiredMixin,DeleteView):
    model         = Bairro
    success_url   = reverse_lazy('bairros')
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


@login_required
def Bairro_detalhe(request,pk):
    bairro = Bairro.objects.get(pk=pk)
    context = {
        'bairro':bairro,
    }
    return render(request,'bairros/bairro_detalhe.html',context)

'''
+                           Boletim
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''


@login_required
def Gerar_boletin(request):
    confirmado_count = Caso.objects.filter(confirmado=True, residente=True).count()
    obito_count = Caso.objects.filter(obito=True, residente=True).count()
    recuperado_count = Caso.objects.filter(recuperado=True, residente=True).count()    
    count_caso_dia = Caso.objects.filter(confirmado=True, residente=True, criado_em=timezone.now()).aggregate(data=Count('criado_em'))
    count_obt_dia = Caso.objects.filter(obito=True, residente=True, criado_em=timezone.now()).aggregate(data=Count('criado_em'))
    Diario.objects.create(confirmado=confirmado_count, recuperado=recuperado_count,
        obito=obito_count, conf_por_dia=count_caso_dia.get('data'),obt_por_dia=count_obt_dia.get('data'),)
    messages.success(request,'Site atualizado com Sucesso com Sucesso! ')
    return redirect('graficos')

@login_required  
def Graficosview(request):
    grafico = Diario.objects.all()
    context ={
        'dados':grafico, 
    }
    return render(request,'grafico/graficos.html',context)

@method_decorator(staff_member_required, name='dispatch')
class GraficoDeleteView(LoginRequiredMixin,DeleteView):
    model         = Diario
    success_url   = reverse_lazy('graficos')
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

@method_decorator(staff_member_required, name='dispatch')
class GraficoUpdateView(LoginRequiredMixin,UpdateView):
    model         = Diario
    template_name = 'grafico/grafico_update.html'
    form_class    = DiarioForm
    success_url   = reverse_lazy('graficos')

@login_required
def Boletim_diario(request):
    prefeitura          = Prefeitura.objects.all()[0]
    confirmado_count    = Caso.objects.filter(confirmado=True,residente=True).count()
    recuperado_count    = Caso.objects.filter(recuperado=True,residente=True).count()
    descartado_count    = Caso.objects.filter(descartado=True,residente=True).count()
    obito_count         = Caso.objects.filter(obito=True,residente=True).count()
    isolado_count       = Caso.objects.filter(isolado=True,residente=True).count()
    internado_count     = Caso.objects.filter(internado=True,residente=True).count()
    uti_count           = Caso.objects.filter(uti=True,residente=True).count()
    criacao = timezone.now()

    context = {
        'cidade':prefeitura,
        'confirmado':confirmado_count,
        'recuperado':recuperado_count,
        'descartado':descartado_count,
        'obito':obito_count,
        'isolado':isolado_count,
        'internado':internado_count,        
        'uti':uti_count,
        'criacao':criacao.strftime('%d/%m/%y'),        
    }
    return render(request, 'diario/boletim.html',context)

'''
+                           CRUD Media
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

@method_decorator(staff_member_required, name='dispatch')
class MediaCreateView(LoginRequiredMixin,CreateView):
    model         = Media
    template_name = 'medias/media_add.html'
    form_class    = MediaForm
    success_url   = reverse_lazy('medias')
    #salvar e adicionar novo
    def post(self, request, *args, **kwargs):
        save_action = None
        if "cancelar" in request.POST:
            return HttpResponseRedirect(reverse('medias'))
        else:
            save_action = super(MediaCreateView, self).post(request, *args, **kwargs)
        if "adicionar_outro" in request.POST:
            messages.success(request,'Média Cadastrado com Sucesso! ')
            return HttpResponseRedirect(reverse('add_media'))
        return save_action

    def get_context_data(self, *args, **kwargs):
        context = super(MediaCreateView, self).get_context_data(*args, **kwargs)
        context['is_superuser'] = self.request.user.is_superuser
        return context

@login_required  
def MediaListView(request):
    media = Media.objects.all()
    context ={
        'medias':media, 
    }
    return render(request,'media/medias.html',context)

@method_decorator(staff_member_required, name='dispatch')
class MediaUpdateView(LoginRequiredMixin,UpdateView):
    model         = Media
    template_name = 'media/media_add.html'
    form_class    = MediaForm
    success_url   = reverse_lazy('medias')

@method_decorator(staff_member_required, name='dispatch')
class MediaDeleteView(LoginRequiredMixin,DeleteView):
    model         = Media
    success_url   = reverse_lazy('medias')
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

@login_required
def list_conf(request):
    list_conf = Caso.objects.select_related(
            'bairro').prefetch_related('comorbidade').filter(confirmado=True,residente=True).order_by('nome')
    conf_count         = Caso.objects.select_related(
            'bairro').prefetch_related('comorbidade').filter(confirmado=True,residente=True).count()
    context = {
        'list_conf':list_conf,
        'conf_count':conf_count,
    }
    return render(request,'casos/list_conf.html',context)

@login_required
def list_rec(request):
    list_rec = Caso.objects.select_related(
            'bairro').prefetch_related('comorbidade').filter(recuperado=True,residente=True)
    rec_count         = Caso.objects.select_related(
            'bairro').prefetch_related('comorbidade').filter(recuperado=True,residente=True).count()
    context = {
        'list_rec':list_rec,
        'rec_count':rec_count,
    }
    return render(request,'casos/list_rec.html',context)

@login_required
def list_iso(request):
    list_iso = Caso.objects.select_related(
            'bairro').prefetch_related('comorbidade').filter(isolado=True,residente=True)
    iso_count         = Caso.objects.select_related(
            'bairro').prefetch_related('comorbidade').filter(isolado=True,residente=True).count()
    context = {
        'list_iso':list_iso,
        'iso_count':iso_count,
    }
    return render(request,'casos/list_iso.html',context)

@login_required
def list_obt(request):
    list_obt = Caso.objects.select_related(
            'bairro').prefetch_related('comorbidade').filter(obito=True,residente=True)
    obt_count         = Caso.objects.select_related(
            'bairro').prefetch_related('comorbidade').filter(obito=True,residente=True).count()
    context = {
        'list_obt':list_obt,
        'obt_count':obt_count,
    }
    return render(request,'casos/list_obt.html',context)

@login_required
def list_uti(request):
    list_uti = Caso.objects.select_related(
            'bairro').prefetch_related('comorbidade').filter(uti=True,residente=True)
    uti_count         = Caso.objects.select_related(
            'bairro').prefetch_related('comorbidade').filter(uti=True,residente=True).count()
    context = {
        'list_uti':list_uti,
        'uti_count':uti_count,
    }
    return render(request,'casos/list_uti.html',context)

@login_required
def list_leito(request):
    list_leito = Caso.objects.select_related(
            'bairro').prefetch_related('comorbidade').filter(internado=True,residente=True)
    leito_count         = Caso.objects.select_related(
            'bairro').prefetch_related('comorbidade').filter(internado=True,residente=True).count()
    context = {
        'list_leito':list_leito,
        'leito_count':leito_count,
    }
    return render(request,'casos/list_leito.html',context)

@login_required
def conf_pdf(request, *callback_args, **callback_kwargs):
    list_conf = Caso.objects.select_related('bairro').prefetch_related('comorbidade').filter(confirmado=True,residente=True).order_by('nome')
    conf_count         = Caso.objects.select_related(
        'bairro').prefetch_related('comorbidade').filter(confirmado=True,residente=True).count()
    prefeitura          = Prefeitura.objects.all()[0]
    today = timezone.now()
    context = {
        'cidade':prefeitura,
        'today': today,
        'list_conf':list_conf,
        'conf_count':conf_count,
        'request': request,
    }
    return Render.render('relatorios/list_pdf.html', context) 

@login_required
def rec_pdf(request, *callback_args, **callback_kwargs):
    list_rec = Caso.objects.select_related('bairro').prefetch_related('comorbidade').filter(recuperado=True,residente=True).order_by('nome')
    rec_count         = Caso.objects.select_related(
        'bairro').prefetch_related('comorbidade').filter(recuperado=True,residente=True).count()
    prefeitura          = Prefeitura.objects.all()[0]
    today = timezone.now()
    context = {
        'cidade':prefeitura,
        'today': today,
        'list_rec':list_rec,
        'rec_count':rec_count,
        'request': request,
    }
    return Render.render('relatorios/list_pdf.html', context) 

@login_required
def iso_pdf(request, *callback_args, **callback_kwargs):
    list_iso = Caso.objects.select_related('bairro').prefetch_related('comorbidade').filter(isolado=True,residente=True).order_by('nome')
    iso_count         = Caso.objects.select_related(
        'bairro').prefetch_related('comorbidade').filter(isolado=True,residente=True).count()
    prefeitura          = Prefeitura.objects.all()[0]
    today = timezone.now()
    context = {
        'cidade':prefeitura,
        'today': today,
        'list_iso':list_iso,
        'iso_count':iso_count,
        'request': request,
    }
    return Render.render('relatorios/list_pdf.html', context) 

@login_required
def leito_pdf(request, *callback_args, **callback_kwargs):
    list_leito = Caso.objects.select_related('bairro').prefetch_related('comorbidade').filter(internado=True,residente=True).order_by('nome')
    leito_count         = Caso.objects.select_related(
        'bairro').prefetch_related('comorbidade').filter(internado=True,residente=True).count()
    prefeitura          = Prefeitura.objects.all()[0]
    today = timezone.now()
    context = {
        'cidade':prefeitura,
        'today': today,
        'list_leito':list_leito,
        'leito_count':leito_count,
        'request': request,
    }
    return Render.render('relatorios/list_pdf.html', context) 

@login_required
def uti_pdf(request, *callback_args, **callback_kwargs):
    list_uti = Caso.objects.select_related('bairro').prefetch_related('comorbidade').filter(uti=True,residente=True).order_by('nome')
    leito_count         = Caso.objects.select_related(
        'bairro').prefetch_related('comorbidade').filter(uti=True,residente=True).count()
    prefeitura          = Prefeitura.objects.all()[0]
    today = timezone.now()
    context = {
        'cidade':prefeitura,
        'today': today,
        'list_uti':list_uti,
        'leito_count':leito_count,
        'request': request,
    }
    return Render.render('relatorios/list_pdf.html', context) 

@login_required
def obt_pdf(request, *callback_args, **callback_kwargs):
    list_obt = Caso.objects.select_related('bairro').prefetch_related('comorbidade').filter(obito=True,residente=True).order_by('nome')
    obt_count         = Caso.objects.select_related(
        'bairro').prefetch_related('comorbidade').filter(obito=True,residente=True).count()
    prefeitura          = Prefeitura.objects.all()[0]
    today = timezone.now()
    context = {
        'cidade':prefeitura,
        'today': today,
        'list_obt':list_obt,
        'obt_count':obt_count,
        'request': request,
    }
    return Render.render('relatorios/list_pdf.html', context)       

@login_required
def total_pdf(request, *callback_args, **callback_kwargs):
    list_total = Caso.objects.select_related('bairro').prefetch_related('comorbidade').filter(residente=True).order_by('nome')
    total_count         = Caso.objects.select_related(
        'bairro').prefetch_related('comorbidade').all().count()
    prefeitura          = Prefeitura.objects.all()[0]
    today = timezone.now()
    context = {
        'cidade':prefeitura,
        'today': today,
        'list_total':list_total,
        'total_count':total_count,
        'request': request,
    }
    return Render.render('relatorios/list_pdf.html', context)