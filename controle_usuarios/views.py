# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from controle_usuarios.models import Usuario
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import ProtectedError
from django.contrib import messages
from controle_usuarios.forms import UsuarioForm,SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from core.decorators import staff_member_required
'''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                           Views de Usuarios
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

#redireciona dependendo do tipo de usuario
@login_required
def login_success(request):
    if request.user.is_superuser:
        # user is an admin redirect to dashboard
        messages.success(request,"Bem Vindo ao Sistema!!")
        return redirect('home')
    else:
        usuario = request.user.pk
        basico = Usuario.objects.filter(user=usuario,tipo=1)
        #print(basico)
        p = Usuario.objects.filter(user=usuario,tipo=2)
        #print(p)
        if p:
            # user is an Usuario redirect to agendamentos
            messages.success(request,"Bem Vindo ao Sistema!!")
            return redirect('home')
        else:
            # user is an basico redirect to Home
            messages.success(request,"Bem Vindo ao Sistema!!")
            return redirect('home')
            
'''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                           Crud de Usuarios
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
@staff_member_required
@login_required
def usuarios(request):
    usu = Usuario.objects.all().exclude(user__username='admin')
    context = {
        'lista_usuarios':usu,
    }
    return render(request,'usuarios/usuarios.html',context)

@staff_member_required
@login_required
@transaction.atomic
def add_usuario(request):
    user_form = SignUpForm(request.POST or None)
    usuario_form = UsuarioForm(request.POST or None)
    if user_form.is_valid() and usuario_form.is_valid():
        user_form.email = request.POST['email']
        user = user_form.save()
        user.refresh_from_db()  # This will load the Profile created by the Signal
        usuario_form = UsuarioForm(request.POST, instance=user.usuario)  # Reload the profile form with the profile instance
        usuario_form.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
        usuario_form.save()  # Gracefully save the form
        messages.success(request,'Usuario Cadastrado com Sucesso! ')
        return redirect('home')
    return render(request, 'usuarios/add_usuario.html', {
        'user_form': user_form,
        'usuario_form': usuario_form
    })

@login_required
def usuario_detalhe(request,pk):
    usuario = Usuario.objects.get(pk=pk)
    context = {
        'usu':usuario,
    }
    return render(request,'usuarios/usuario_detalhe.html',context)
    
@login_required   
def update_usuario(request,pk):
    usuario 		= Usuario.objects.get(pk=pk)
    at              = Usuario.objects.filter(user=request.user,tipo=1)
    usuariosls      = Usuario.objects.filter(user=request.user,tipo=2)
    usuario_form	= UsuarioForm(request.POST or None, instance=usuario)
    if usuario_form.is_valid():
        usuario_form.save()
        messages.success(request, ('Dados atualizados com Sucesso!'))
        if usuariosls.exists():
            return redirect('home')
        else:
            return redirect('usuarios')
    return render(request, 'usuarios/edit_usuario.html', {
        'usuario_form': usuario_form,'bas':at,'usu':usuariosls
    })

@staff_member_required
@login_required 
def excluir_usuario(request,pk):
    try :
        usuario = Usuario.objects.get(pk=pk).delete()
        messages.error(request, 'Usuario Deletado Com Sucesso.')
    except ProtectedError:
        messages.warning(request,
         "você não pode deletar esse Usuario")
    return redirect('usuarios')

            
'''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                         Reset de senha de Usuario/Usuarios Logados
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

def change_password_user(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Sua Senha foi Atualizada com Sucesso!')
            return redirect('change_password')
        else:
            messages.error(request, 'Por Favor Verifique o Erro!.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'login/change_password.html', {
        'form': form
    })