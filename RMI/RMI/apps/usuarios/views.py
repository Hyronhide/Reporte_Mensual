from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from RMI.apps.usuarios.forms import *
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User ##
from RMI.apps.usuarios.models import *



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

def edit_user_view(request):
	info = ""	
	us = User.objects.get(id = request.user.id)
	if request.method == "POST":
		formulario = UserForm(request.POST, request.FILES, instance = us)		
		if formulario.is_valid():
			clave = formulario.cleaned_data['password']
			formulario.password = us.set_password(clave)
			edit_user = formulario.save(commit = False)
			formulario.save_m2m()
			edit_user.status = True
			edit_user.save()
			info = "Guardado Satisfactoriamente"
			#return HttpResponseRedirect ('/')
			return HttpResponseRedirect ('/')
	else:
		formulario = UserForm(instance = us)
	ctx = {'form':formulario, 'informacion':info}	
	return render_to_response('usuarios/edit_user.html',ctx,context_instance = RequestContext(request))	

def index_view(request):
	usuario = User.objects.get(id= request.user.id)
	ctx={'usuario':usuario}
	return render(request, 'usuarios/index.html',ctx) 	 

def administrador_view(request):	
	usuario = User.objects.get(id= request.user.id)
	ctx={'usuario':usuario}
	return render(request, 'usuarios/administrador.html',ctx) 	

def register_view(request):
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			nombres = form.cleaned_data['first_name']
			apellidos = form.cleaned_data['last_name']
			usuario = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			u = User.objects.create_user(first_name=nombres,last_name=apellidos,username=usuario,email=email,password=password_one)
			u.save()# Guarda el objeto
			return render_to_response('usuarios/thanks_register.html',context_instance=RequestContext(request))
		else:		
			ctx = {'form':form}
			return render_to_response('usuarios/register.html',ctx,context_instance=RequestContext(request))
	ctx = {'form':form}
	return render_to_response('usuarios/register.html',ctx,context_instance=RequestContext(request))	 	

########################### SUBIR REPORTES POR MESES ##################################################

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


############################################### 	BORRAR REPORTES MESES    ############################################
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

#################################################################################################################
def consultar_enero_view(request):
	consultar_enero = Reporte_Mensual.objects.filter(mes='Enero')
	tolal_reportes = consultar_enero.count
	#tolal_reportes = 0
	#for c in consultar_enero:
	#	tolal_reportes=tolal_reportes+1

	ctx = {'consultar_enero':consultar_enero, 'total_reportes':tolal_reportes}
	return render(request, 'usuarios/consultar_enero.html',ctx) 