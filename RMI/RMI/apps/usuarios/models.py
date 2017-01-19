#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver
from django.conf import settings
import os

from django.db import models

class User_profile(models.Model):	

	user     = models.OneToOneField(User)	
	telefono = models.CharField(max_length=13)
	#imagen   = models.ImageField(upload_to='Perfil/',default='Perfil/perfil.jpg')
	
	def __unicode__(self):
		return self.user.username
#		
class Reporte_Mensual(models.Model):

	mes = models.CharField(max_length= 30)
	nombre_adjunto = models.CharField(max_length= 50)
	adjunto_exel = models.FileField(upload_to='Reporte/')	
	usuario = models.ForeignKey(User)
	fecha = models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return "MES: %s; NOMBRE ADJUNTO: %s; USUARIO: %s %s"  % (self.mes, self.nombre_adjunto, self.usuario.first_name , self.usuario.last_name)

@receiver(pre_delete, sender=Reporte_Mensual)
def _Reporte_Mensual_delete(sender, instance, using, **kwargs):
    file_path = settings.MEDIA_ROOT + str(instance.adjunto_exel)
    #print(file_path)

    if os.path.isfile(file_path):
        os.remove(file_path)	
'''
@receiver(pre_delete, sender=User_profile)
def _User_Profile_delete(sender, instance, using, **kwargs):
    file_path = settings.MEDIA_ROOT + str(instance.imagen)
    #print(file_path)

    if os.path.isfile(file_path):
        os.remove(file_path)	        	
'''        