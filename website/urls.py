from django.urls import path
from website import views

urlpatterns = [
##############################HOME############################################
	path('',views.site,name="site"),
	path('nota/',views.nota,name="nota"),

]