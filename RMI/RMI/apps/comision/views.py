from django.shortcuts import render
from .forms import *
# Create your views here.
def comision_view (request):

	if request.method == "POST":
		form_Com= Comision_form(request.POST, request.FILES)
		
		if form_Com.is_valid():
			try:
				i = form_Com.save(commit = False)
				i.save()
				info = "Informacion Guardada con Exito!" 
				
			except:
				info = "Debe completar todos los campos" 
	if request.method == "GET":
		form_Com = Comision_form()
		

	return render (request,'comision/comision.html',locals())

def resultados_comision_view (request):
	pass