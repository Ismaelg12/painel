from django.urls import path
from core import views
from django.views.generic.base import TemplateView

urlpatterns = [
	path('dashboard/',views.DashboardView.as_view(),name='home'),
	# path('acesso/negado/',TemplateView.as_view(template_name="erros/403.html"),name='erro_403'),
	# #######################CASOS##################################################
	path('isolados',views.list_iso,name='isolados'),
	path('confirmados',views.list_conf,name='confirmados'),
	path('recuperados',views.list_rec,name='recuperados'),
	path('obitos',views.list_obt,name='obitos'),
	path('uti',views.list_uti,name='uti'),
	path('leitos',views.list_leito,name='leitos'),
	path('casos/',views.CasoListView.as_view(),name='casos'),
	path('adicionar/caso/',views.CasoCreateView.as_view(),name='add_caso'),
	path('atualizar/caso/<int:pk>/',views.CasoUpdateView.as_view(),name='update_caso'),
	path('deletar/caso/<int:pk>/',views.CasoDeleteView.as_view(),name='deletar_caso'),
	path('casos/detalhe/<int:pk>/detalhe/',views.Caso_detalhe,name="caso_detalhe"),
		#######################TESTES##################################################
	# path('testes/',views.TesteListView.as_view(),name='testes'),
	# path('adicionar/teste/',views.TesteCreateView.as_view(),name='add_teste'),
	# path('atualizar/teste/<int:pk>/',views.TesteUpdateView.as_view(),name='update_teste'),
	# path('deletar/teste/<int:pk>/',views.TesteDeleteView.as_view(),name='deletar_teste'),
		#######################BAIRROS##################################################
	path('bairros/',views.BairroListView.as_view(),name='bairros'),
	path('adicionar/bairro/',views.BairroCreateView.as_view(),name='add_bairro'),
	path('atualizar/bairro/<int:pk>/',views.BairroUpdateView.as_view(),name='update_bairro'),
	path('deletar/bairro/<int:pk>/',views.BairroDeleteView.as_view(),name='deletar_bairro'),
	path('bairros/detalhe/<int:pk>/detalhe/',views.Bairro_detalhe,name="bairro_detalhe"),
	 		#######################COMORBIDADES##################################################
	path('comorbidades/',views.ComorbidadeListView.as_view(),name='comorbidades'),
	path('adicionar/comorbidade/',views.ComorbidadeCreateView.as_view(),name='add_comorbidade'),
	path('atualizar/comorbidade/<int:pk>/',views.ComorbidadeUpdateView.as_view(),name='update_comorbidade'),
	path('deletar/comorbidade/<int:pk>/',views.ComorbidadeDeleteView.as_view(),name='deletar_comorbidade'),
	path('comorbidades/detalhe/<int:pk>/detalhe/',views.Comorbidade_detalhe,name="comorbidade_detalhe"),
	
	path('conf_pdf/',views.conf_pdf,name='conf_pdf'),
	path('rec_pdf/',views.rec_pdf,name='rec_pdf'),
	path('iso_pdf/',views.iso_pdf,name='iso_pdf'),
	path('leito_pdf/',views.leito_pdf,name='leito_pdf'),
	path('uti_pdf/',views.uti_pdf,name='uti_pdf'),
	path('obt_pdf/',views.obt_pdf,name='obt_pdf'),
	path('total_pdf/',views.total_pdf,name='total_pdf'),

	path('boletim/',views.Gerar_boletin,name='boletim'),
	path('diario/',views.Boletim_diario,name='diario'),
	path('grafico/',views.Graficosview,name='graficos'),
	path('deletar/grafico/<int:pk>/',views.GraficoDeleteView.as_view(),name='deletar_grafico'),
	path('atualizar/grafico/<int:pk>/',views.GraficoUpdateView.as_view(),name='update_grafico'),
	# ##############MEDIA MOVEL######################
	path('medias/',views.MediaListView,name='medias'),
	path('adicionar/media/',views.MediaCreateView.as_view(),name='add_media'),
	path('atualizar/media/<int:pk>/',views.MediaUpdateView.as_view(),name='update_media'),
	path('deletar/media/<int:pk>/',views.MediaDeleteView.as_view(),name='deletar_media'),
	]