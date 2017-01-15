from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from RMI.apps.usuarios.forms import *
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User ##
from RMI.apps.usuarios.models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage#paginator
import os 


# Create your views here.
def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():#verificacmos si el usuario ya esta authenticado o logueado
		return HttpResponseRedirect('/index/')#si esta logueado lo redirigimos a la pagina principal
	else: #si no esta authenticado 
		if request.method == "POST":
			formulario = Login_form(request.POST) #creamos un objeto de Loguin_form
			if formulario.is_valid(): #si la informacion enviada es correcta		
				usu= formulario.cleaned_data['usuario'] #guarda informacion ingresada del formulario
				pas= formulario.cleaned_data['clave'] #guarda informacion ingresada del formulario
				usuario = authenticate(username = usu,password = pas)#asigna la autenticacion del usuario
				if usuario is not None and usuario.is_active:#si el usuario no es nulo y esta activo
					login(request,usuario)#se loguea al sistema con la informacion de usuario
					return HttpResponseRedirect('/index/')#redirigimos a la pagina principal
				else:
					mensaje = "usuario y/o clave incorrecta"
		formulario = Login_form() #creamos un formulario nuevo limpio
		ctx = {'form':formulario, 'mensaje':mensaje}#variable de contexto para pasar info a login.html
		return render_to_response('usuarios/login.html',ctx, context_instance = RequestContext(request))

def logout_view(request):
	logout(request)# funcion de django importda anteriormente
	return HttpResponseRedirect('/')# redirigimos a la pagina principal

def user_view(request): 
	us = User.objects.get(id= request.user.id)
	ctx={'user':us}
	return render_to_response('usuarios/user.html',ctx,context_instance = RequestContext(request))

def admin_user_view(request, id_user): 
	us = User.objects.get(id= id_user)
	ctx={'user':us}
	return render_to_response('usuarios/admin_user.html',ctx,context_instance = RequestContext(request))			

def edit_user_view(request):
	info = ""	
	info_enviado = False
	us = User.objects.get(id = request.user.id)
	user = User_profile.objects.get(user=us)
	#formulario = UserForm()
	if request.method == "POST":
		formulario = UserForm(request.POST, request.FILES, instance = us)
		form_user= User_profile_Form(request.POST, request.FILES, instance = user)		
		if formulario.is_valid():
			info_enviado = True
			#telefono = formulario.cleaned_data['telefono']
			#clave = formulario.cleaned_data['password']
			#formulario.password = us.set_password(clave)
			edit_user = formulario.save(commit = False)
			edit_user_telefono = form_user.save(commit = False)
			#edit_user_telefono.telefono= telefono
			#formulario.save_m2m()
			#edit_user.status = True
			edit_user_telefono.save()
			edit_user.save()
			info = "Guardado Satisfactoriamente"
			#return HttpResponseRedirect ('/')
			#return HttpResponseRedirect ('/user/')
	else:
		formulario = UserForm(instance = us)
		form_user = User_profile_Form(instance = user)
	ctx = {'form':formulario, 'form_user':form_user,'informacion':info, 'info_enviado':info_enviado}	
	return render_to_response('usuarios/edit_user.html',ctx,context_instance = RequestContext(request))

def admin_edit_user_view(request,id_user):
	info = ""	
	info_enviado = False
	us = User.objects.get(id = id_user)
	user = User_profile.objects.get(user=us)
	if request.method == "POST":
		formulario = AdminUserForm(request.POST, request.FILES, instance = us)	
		form_user= User_profile_Form(request.POST, request.FILES, instance = user)		
		if formulario.is_valid():
			info_enviado = True
			#clave = formulario.cleaned_data['password']
			#formulario.password = us.set_password(clave)
			edit_user = formulario.save(commit = False)	
			edit_user_telefono = form_user.save(commit = False)		
			#edit_user.status = True
			edit_user_telefono.save()
			edit_user.save()
			info = "Guardado Satisfactoriamente"
			#return HttpResponseRedirect ('/')
			#return HttpResponseRedirect ('/instructores/')
	else:
		formulario = AdminUserForm(instance = us)
		form_user = User_profile_Form(instance = user)
	ctx = {'form':formulario, 'form_user':form_user,'informacion':info, 'info_enviado':info_enviado}	
	return render_to_response('usuarios/admin_edit_user.html',ctx,context_instance = RequestContext(request))		

def edit_password_view(request):
	info = ""	
	info_enviado = False
	us = User.objects.get(id = request.user.id)
	if request.method == "POST":
		formulario = PasswordForm(request.POST, request.FILES, instance = us)		
		if formulario.is_valid():
			info_enviado = True
			clave = formulario.cleaned_data['password']
			usu= us.username #guarda informacion ingresada del formulario
			pas= clave #guarda informacion ingresada del formulario
			formulario.password = us.set_password(clave)
			edit_user = formulario.save(commit = False)			
			#formulario.save_m2m()
			#edit_user.status = True
			edit_user.save()
			info = "Guardado Satisfactoriamente"
			usuario = authenticate(username = usu,password = pas)#asigna la autenticacion del usuario
			if usuario is not None and usuario.is_active:#si el usuario no es nulo y esta activo
				login(request,usuario)#se loguea al sistema con la informacion de usuario
				return HttpResponseRedirect('/password_guardado_user/')#redirigimos a la pagina principal
			#return HttpResponseRedirect ('/')
			#return HttpResponseRedirect ('/index/')
	else:
		formulario = PasswordForm(instance = us)
	ctx = {'form':formulario, 'informacion':info, 'info_enviado':info_enviado}	
	return render_to_response('usuarios/edit_password.html',ctx,context_instance = RequestContext(request))

def admin_edit_password_view(request,id_user):
	info = ""	
	info_enviado = False
	us = User.objects.get(id = id_user)
	if request.method == "POST":
		formulario = PasswordForm(request.POST, request.FILES, instance = us)		
		if formulario.is_valid():
			info_enviado = True
			clave = formulario.cleaned_data['password']
			formulario.password = us.set_password(clave)
			edit_user = formulario.save(commit = False)
			#formulario.save_m2m()
			#edit_user.status = True
			edit_user.save()
			info = "Guardado Satisfactoriamente"
			#return HttpResponseRedirect ('/')
			return HttpResponseRedirect ('/password_guardado_admin/')
	else:
		formulario = PasswordForm(instance = us)
	ctx = {'form':formulario, 'informacion':info, 'info_enviado':info_enviado}	
	return render_to_response('usuarios/admin_edit_password.html',ctx,context_instance = RequestContext(request))				


def index_view(request):
	usuario = User.objects.get(id= request.user.id)
	ctx={'usuario':usuario}
	return render(request, 'usuarios/index.html',ctx) 

def password_guardado_user_view(request):
	
	return render(request, 'usuarios/password_guardado_user.html') 	

def password_guardado_admin_view(request):
	
	return render(request, 'usuarios/password_guardado_admin.html') 		 


def administrador_view(request):	
	usuario = User.objects.get(id= request.user.id)
	ctx={'usuario':usuario}
	return render(request, 'usuarios/administrador.html',ctx) 	

def register_view(request):
	form = RegisterForm()
	user_form = User_profile_Form()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		user_form = User_profile_Form(request.POST)
		if form.is_valid():
			nombres = form.cleaned_data['first_name']
			apellidos = form.cleaned_data['last_name']
			usuario = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			telefono = form.cleaned_data['telefono']
			u = User.objects.create_user(first_name=nombres,last_name=apellidos,username=usuario,email=email,password=password_one)
			user = user_form.save(commit=False)
			user.telefono= telefono
			user.user=u
			#user= form.save(commit=False)
			#user.user_profile.telefono=telefono
			#user.save()
			#user = u.save(commit=False)
			#user.user_profile.telefono=telefono
			user.save()			
			u.save()# Guarda el objeto
			#u.user_profile.telefono=telefono
			#u.save()
			
			return render_to_response('usuarios/thanks_register.html',context_instance=RequestContext(request))
		else:		
			ctx = {'form':form}
			return render_to_response('usuarios/register.html',ctx,context_instance=RequestContext(request))
	ctx = {'form':form}
	return render_to_response('usuarios/register.html',ctx,context_instance=RequestContext(request))

def instructores_view(request,pagina):
	lista_instructores = User.objects.filter(is_staff=False)		
	query = request.GET.get('q','')     
	if query:
		qset = (
			Q(first_name__icontains=query)|
			Q(last_name__icontains=query)|
			Q(username__icontains=query)|
			Q(email__icontains=query)
		)
		results = User.objects.filter(qset).distinct()  
		mostrar = False      
	else:
		mostrar = True
		results = []

	#lista_prod = Producto.objects.filter(status = True)#SELECT * from Producto WHERE status= True
	paginator = Paginator(lista_instructores, 15) 
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		instructores = paginator.page(page)
	except (EmptyPage,InvalidPage):
		instructores = paginator.page(paginator.num_pages)	


	return render_to_response('usuarios/instructores.html', {
		"results": results,
		"query": query,
		"mostrar": mostrar,
		"instructores":instructores,
		"lista_instructores":lista_instructores,        
	},context_instance=RequestContext(request))

	#ctx={'instructores':instructores}
	#return render(request, 'usuarios/instructores.html',ctx) 	
########################### SUBIR REPORTES POR MESES ##################################################
def reportes_view(request, id_mes):
	meses = { '1':'ENERO', '2':'FEBRERO', '3':'MARZO', '4':'ABRIL', '5':'MAYO','6':'JUNIO','7':'JULIO','8':'AGOSTO','9':'SEPTIEMBRE','10':'OCTUBRE','11':'NOVIEMBRE','12':'DICIEMBRE' }	
	mes = meses[id_mes]	
	
	reporte_validar = Reporte_Mensual.objects.filter(mes= mes,usuario__id= request.user.id )	
	nombre_adjunto = ""	
	info_enviado = False
	if request.method == "POST":		
		form = Reporte(request.POST, request.FILES)
		if form.is_valid():
			info_enviado = True
			nombre_adjunto = form.cleaned_data['nombre_adjunto']											
			reporte = form.save(commit = False)
			reporte.usuario = request.user	
			reporte.mes = mes					
			reporte.save()					
	else:
		form = Reporte()

	ctx={'reporte_validar':reporte_validar, 'form':form, 'mes':mes}

	return render(request, 'usuarios/reportes.html',ctx) 	
######################################################################################
'''
def enero_view(request):
	reporte_validar = Reporte_Mensual.objects.filter(mes= 'Enero',usuario__id= request.user.id )	
	nombre_adjunto = ""	
	info_enviado = False
	if request.method == "POST":		
		form = Reporte(request.POST, request.FILES)
		if form.is_valid():
			info_enviado = True
			nombre_adjunto = form.cleaned_data['nombre_adjunto']											
			reporte = form.save(commit = False)
			reporte.usuario = request.user	
			reporte.mes = 'Enero'					
			reporte.save()					
	else:
		form = Reporte()

	ctx={'reporte_validar':reporte_validar, 'form':form}

	return render(request, 'usuarios/enero.html',ctx) 	

def febrero_view(request):

	reporte_validar = Reporte_Mensual.objects.filter(mes= 'Febrero',usuario__id= request.user.id )	
	nombre_adjunto = ""	
	info_enviado = False
	if request.method == "POST":		
		form = Reporte(request.POST, request.FILES)
		if form.is_valid():
			info_enviado = True
			nombre_adjunto = form.cleaned_data['nombre_adjunto']								
			reporte = form.save(commit = False)			
			reporte.usuario = request.user	
			reporte.mes = 'Febrero'				
			reporte.save()	
				
	else:
		form = Reporte()

	ctx={'reporte_validar':reporte_validar, 'form':form}

	return render(request, 'usuarios/febrero.html',ctx) 	

def marzo_view(request):

	reporte_validar = Reporte_Mensual.objects.filter(mes= 'Marzo',usuario__id= request.user.id )	
	nombre_adjunto = ""	
	info_enviado = False
	if request.method == "POST":		
		form = Reporte(request.POST, request.FILES)
		if form.is_valid():
			info_enviado = True
			nombre_adjunto = form.cleaned_data['nombre_adjunto']								
			reporte = form.save(commit = False)
			reporte.usuario = request.user	
			reporte.mes = 'Marzo'				
			reporte.save()	
				
	else:
		form = Reporte()

	ctx={'reporte_validar':reporte_validar, 'form':form}

	return render(request, 'usuarios/marzo.html',ctx) 		

def abril_view(request):

	reporte_validar = Reporte_Mensual.objects.filter(mes= 'Abril',usuario__id= request.user.id )	
	nombre_adjunto = ""	
	info_enviado = False
	if request.method == "POST":		
		form = Reporte(request.POST, request.FILES)
		if form.is_valid():
			info_enviado = True
			nombre_adjunto = form.cleaned_data['nombre_adjunto']								
			reporte = form.save(commit = False)
			reporte.usuario = request.user	
			reporte.mes = 'Abril'				
			reporte.save()	
				
	else:
		form = Reporte()

	ctx={'reporte_validar':reporte_validar, 'form':form}

	return render(request, 'usuarios/abril.html',ctx) 

def mayo_view(request):

	reporte_validar = Reporte_Mensual.objects.filter(mes= 'Mayo',usuario__id= request.user.id )	
	nombre_adjunto = ""	
	info_enviado = False
	if request.method == "POST":		
		form = Reporte(request.POST, request.FILES)
		if form.is_valid():
			info_enviado = True
			nombre_adjunto = form.cleaned_data['nombre_adjunto']								
			reporte = form.save(commit = False)
			reporte.usuario = request.user	
			reporte.mes = 'Mayo'				
			reporte.save()	
				
	else:
		form = Reporte()

	ctx={'reporte_validar':reporte_validar, 'form':form}

	return render(request, 'usuarios/mayo.html',ctx) 	

def junio_view(request):

	reporte_validar = Reporte_Mensual.objects.filter(mes= 'Junio',usuario__id= request.user.id )	
	nombre_adjunto = ""	
	info_enviado = False
	if request.method == "POST":		
		form = Reporte(request.POST, request.FILES)
		if form.is_valid():
			info_enviado = True
			nombre_adjunto = form.cleaned_data['nombre_adjunto']								
			reporte = form.save(commit = False)
			reporte.usuario = request.user	
			reporte.mes = 'Junio'				
			reporte.save()	
				
	else:
		form = Reporte()

	ctx={'reporte_validar':reporte_validar, 'form':form}

	return render(request, 'usuarios/junio.html',ctx) 

def julio_view(request):

	reporte_validar = Reporte_Mensual.objects.filter(mes= 'Julio',usuario__id= request.user.id )	
	nombre_adjunto = ""	
	info_enviado = False
	if request.method == "POST":		
		form = Reporte(request.POST, request.FILES)
		if form.is_valid():
			info_enviado = True
			nombre_adjunto = form.cleaned_data['nombre_adjunto']								
			reporte = form.save(commit = False)
			reporte.usuario = request.user	
			reporte.mes = 'Julio'				
			reporte.save()	
				
	else:
		form = Reporte()

	ctx={'reporte_validar':reporte_validar, 'form':form}

	return render(request, 'usuarios/julio.html',ctx) 

def agosto_view(request):

	reporte_validar = Reporte_Mensual.objects.filter(mes= 'Agosto',usuario__id= request.user.id )	
	nombre_adjunto = ""	
	info_enviado = False
	if request.method == "POST":		
		form = Reporte(request.POST, request.FILES)
		if form.is_valid():
			info_enviado = True
			nombre_adjunto = form.cleaned_data['nombre_adjunto']								
			reporte = form.save(commit = False)
			reporte.usuario = request.user	
			reporte.mes = 'Agosto'				
			reporte.save()	
				
	else:
		form = Reporte()

	ctx={'reporte_validar':reporte_validar, 'form':form}

	return render(request, 'usuarios/agosto.html',ctx) 	

def septiembre_view(request):

	reporte_validar = Reporte_Mensual.objects.filter(mes= 'Septiembre',usuario__id= request.user.id )	
	nombre_adjunto = ""	
	info_enviado = False
	if request.method == "POST":		
		form = Reporte(request.POST, request.FILES)
		if form.is_valid():
			info_enviado = True
			nombre_adjunto = form.cleaned_data['nombre_adjunto']								
			reporte = form.save(commit = False)
			reporte.usuario = request.user	
			reporte.mes = 'Septiembre'				
			reporte.save()	
				
	else:
		form = Reporte()

	ctx={'reporte_validar':reporte_validar, 'form':form}

	return render(request, 'usuarios/septiembre.html',ctx) 	

def octubre_view(request):

	reporte_validar = Reporte_Mensual.objects.filter(mes= 'Octubre',usuario__id= request.user.id )	
	nombre_adjunto = ""	
	info_enviado = False
	if request.method == "POST":		
		form = Reporte(request.POST, request.FILES)
		if form.is_valid():
			info_enviado = True
			nombre_adjunto = form.cleaned_data['nombre_adjunto']								
			reporte = form.save(commit = False)
			reporte.usuario = request.user	
			reporte.mes = 'Octubre'				
			reporte.save()	
				
	else:
		form = Reporte()

	ctx={'reporte_validar':reporte_validar, 'form':form}

	return render(request, 'usuarios/octubre.html',ctx) 

def noviembre_view(request):

	reporte_validar = Reporte_Mensual.objects.filter(mes= 'Noviembre',usuario__id= request.user.id )	
	nombre_adjunto = ""	
	info_enviado = False
	if request.method == "POST":		
		form = Reporte(request.POST, request.FILES)
		if form.is_valid():
			info_enviado = True
			nombre_adjunto = form.cleaned_data['nombre_adjunto']								
			reporte = form.save(commit = False)
			reporte.usuario = request.user	
			reporte.mes = 'Noviembre'				
			reporte.save()	
				
	else:
		form = Reporte()

	ctx={'reporte_validar':reporte_validar, 'form':form}

	return render(request, 'usuarios/noviembre.html',ctx) 

def diciembre_view(request):

	reporte_validar = Reporte_Mensual.objects.filter(mes= 'Diciembre',usuario__id= request.user.id )	
	nombre_adjunto = ""	
	info_enviado = False
	if request.method == "POST":		
		form = Reporte(request.POST, request.FILES)
		if form.is_valid():
			info_enviado = True
			nombre_adjunto = form.cleaned_data['nombre_adjunto']								
			reporte = form.save(commit = False)
			reporte.usuario = request.user	
			reporte.mes = 'Diciembre'				
			reporte.save()	
				
	else:
		form = Reporte()

	ctx={'reporte_validar':reporte_validar, 'form':form}

	return render(request, 'usuarios/diciembre.html',ctx) 					
#########################################################################################################

'''
############################################### 	BORRAR REPORTES MESES    ############################################
def del_reporte_view(request, id_reporte):
	info = "inicializando"
	try:
		rep = Reporte_Mensual.objects.get(id = id_reporte)
		mes = rep.mes
		meses = { 'ENERO': '1', 'FEBRERO': '2', 'MARZO': '3', 'ABRIL':'4', 'MAYO':'5', 'JUNIO':'6', 'JULIO':'7', 'AGOSTO':'8', 'SEPTIEMBRE':'9', 'OCTUBRE':'10', 'NOVIEMBRE':'11', 'DICIEMBRE':'12' }	
		mes_num = meses[mes]
		print mes			
		rep.delete()

		#rep.adjunto_exel.url.delete()
		info = "El reporte ha sido eliminado correctamente"
		return HttpResponseRedirect('/reportes/%s'%(mes_num))
	except:
		info = "EL reporte no se puede eliminar"
		#return render_to_response('home/productos.html', context_instance = RequestContext(request))
		return HttpResponseRedirect('/index/')	
'''
def del_reporte_enero_view(request, id_reporte):
	info = "inicializando"
	try:
		rep = Reporte_Mensual.objects.get(id = id_reporte)
		rep.delete()
		info = "El reporte ha sido eliminado correctamente"
		return HttpResponseRedirect('/enero/')
	except:
		info = "EL reporte no se puede eliminar"
		#return render_to_response('home/productos.html', context_instance = RequestContext(request))
		return HttpResponseRedirect('/index/')	

def del_reporte_febrero_view(request, id_reporte):
	info = "inicializando"
	try:
		rep = Reporte_Mensual.objects.get(id = id_reporte)
		rep.delete()
		info = "El reporte ha sido eliminado correctamente"
		return HttpResponseRedirect('/febrero/')
	except:
		info = "EL reporte no se puede eliminar"
		#return render_to_response('home/productos.html', context_instance = RequestContext(request))
		return HttpResponseRedirect('/febrero/')	

def del_reporte_marzo_view(request, id_reporte):
	info = "inicializando"
	try:
		rep = Reporte_Mensual.objects.get(id = id_reporte)
		rep.delete()
		info = "El reporte ha sido eliminado correctamente"
		return HttpResponseRedirect('/marzo/')
	except:
		info = "EL reporte no se puede eliminar"
		#return render_to_response('home/productos.html', context_instance = RequestContext(request))
		return HttpResponseRedirect('/marzo/')	

def del_reporte_abril_view(request, id_reporte):
	info = "inicializando"
	try:
		rep = Reporte_Mensual.objects.get(id = id_reporte)
		rep.delete()
		info = "El reporte ha sido eliminado correctamente"
		return HttpResponseRedirect('/abril/')
	except:
		info = "EL reporte no se puede eliminar"
		#return render_to_response('home/productos.html', context_instance = RequestContext(request))
		return HttpResponseRedirect('/abril/')							

#############################################	CONSULTAR REPORTES POR MES #####################################################
'''
def consultar_view(request,pagina,id_mes):
	meses = { '1':'ENERO', '2':'FEBRERO', '3':'MARZO', '4':'ABRIL', '5':'MAYO','6':'JUNIO','7':'JULIO','8':'AGOSTO','9':'SEPTIEMBRE','10':'OCTUBRE','11':'NOVIEMBRE','12':'DICIEMBRE' }	
	mes = meses[id_mes]	
	num_mes = id_mes
	lista_consultar = Reporte_Mensual.objects.filter(mes=mes)
	usuarios = User.objects.filter(is_staff=False)
	instructores = usuarios.count
	tolal_reportes = lista_consultar.count
	#tolal_reportes = 0
	#for c in consultar_enero:
	#	tolal_reportes=tolal_reportes+1
	query = request.GET.get('q','')     
	if query:
		qset = (
			Q(usuario__first_name__icontains=query)|
			Q(usuario__last_name__icontains=query)|
			Q(usuario__username__icontains=query)|
			Q(usuario__email__icontains=query)
		)
		results = Reporte_Mensual.objects.filter(qset,mes=mes).distinct()  
		mostrar = False      
	else:
		mostrar = True
		results = []

	paginator = Paginator(lista_consultar, 15) 
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		consultar = paginator.page(page)
	except (EmptyPage,InvalidPage):
		consultar = paginator.page(paginator.num_pages)		
		
	return render_to_response('usuarios/consultar.html', {
		"results": results,
		"query": query,
		"mostrar": mostrar,		
		"consultar":consultar,
		"total_reportes":tolal_reportes, 
		"mes":mes,
		"instructores":instructores,
		"num_mes":num_mes,      
	},context_instance=RequestContext(request))


	#ctx = {'consultar':consultar, 'total_reportes':tolal_reportes, 'mes':mes}
	#return render(request, 'usuarios/consultar.html',ctx) 