from django import forms
from .models import *
class Regional_form(forms.ModelForm):
	class Meta:
		model = Regional
		fields = '__all__'	

class Comision_form(forms.ModelForm):
	class Meta:
		model = Comision
		fields = '__all__'	
