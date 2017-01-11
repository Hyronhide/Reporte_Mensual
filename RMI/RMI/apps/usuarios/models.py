from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

#class user_profile(models.Model):	

#	user     = models.OneToOneField(User)	
	

#	def __unicode__(self):
#		return self.user.username
#		
class Reporte_Mensual(models.Model):

	mes = models.CharField(max_length= 30)
	nombre_adjunto = models.CharField(max_length= 50)
	adjunto_exel = models.FileField(upload_to='Reporte/')	
	usuario = models.ForeignKey(User)
	fecha = models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return "MES: %s; NOMBRE ADJUNTO: %s; USUARIO: %s %s"  % (self.mes, self.nombre_adjunto, self.usuario.first_name , self.usuario.last_name)