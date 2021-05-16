# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

# First, define the Manager subclass.
class UsuarioManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(ativo=True).exclude(user__username="admin")

#Modelo para a area de atuação de cada Usuario
# class Perfil(models.Model):
# 	id = models.PositiveSmallIntegerField(choices=AREA,primary_key=True)

# 	def __str__(self): 
# 		return self.get_id_display()

class Usuario(models.Model):
	BASICO = 1
	USUARIO = 2
	ROLE_CHOICES = (
		(1, 'Basico'),
		(2, 'Usuario'),
	)
	nome            = models.CharField(max_length=50)
	sobrenome       = models.CharField(max_length=50)
	user            = models.OneToOneField(User, on_delete=models.CASCADE)
	email           = models.EmailField(max_length=50,blank=True,null=True)
	telefone        = models.CharField(max_length=15,blank=True)
	cpf             = models.CharField(max_length=14,unique=True,null=True)
	data_nascimento = models.DateField(null=True,blank=True)
	data_cadastro   = models.DateField(auto_now_add = True)
	ativo           = models.BooleanField(default=True)
	tipo            = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,verbose_name='Tipo (Permissão)',null=True)
	atualizado_em   = models.DateTimeField('Atualizado em', auto_now=True)
	
	
	objects = models.Manager() # The default manager.
	#manage Sobrescrito
	prof_objects = UsuarioManager() 

	class Meta:
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'

	def __str__(self):
		return self.nome + ' ' + self.sobrenome

#signals para atualizar o email nos dois modelos
@receiver(post_save, sender=Usuario)
def update_usuario_user(sender, instance, created, **kwargs):
	if not created:
		if instance.email != None:
			User.objects.filter(id=instance.id).update(email=instance.email)
		
#signals para criar o usuario junto ao user
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
	if created:
		Usuario.objects.create(
			user=instance)
	instance.usuario.save()

@receiver(post_delete, sender=Usuario)
def auto_delete(sender, instance, **kwargs):
	instance.user.delete()