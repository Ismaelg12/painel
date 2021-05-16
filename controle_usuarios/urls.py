from django.urls import path
from controle_usuarios import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (PasswordResetView,
 PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView)

urlpatterns = [
	path('login/',auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
	path('bemvindo/',views.login_success,name="login_success"),
	path('sair',auth_views.LogoutView.as_view(), name='logout'),
	path('atualizar/usuario/<int:pk>/',views.update_usuario,name="atualizar_usuario"),
	path('usuario/detalhe/<int:pk>/detalhe/',views.usuario_detalhe,name="usuario_detalhe"),
	path('deletar/usuario/<int:pk>/',views.excluir_usuario,name="deletar_usuario"),
	path('usuarios/',views.usuarios,name="usuarios"),
	path('adicionar/usuario/',views.add_usuario,name='add_usuario'),
	#change Password
	path(r'accounts/password/',views.change_password_user, name='change_password'),
	#reset Password 
	path('password/reset/', PasswordResetView.as_view(
		template_name='registration/password_reset_form.html'), name='password_reset'),
    path('accounts/password/reset/done', PasswordResetDoneView.as_view(
    	template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset_password_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
    	template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/password/reset/complete', PasswordResetCompleteView.as_view(
    	template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
