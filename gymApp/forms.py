from django.forms import ModelForm
from .models import Client,Class
from django import forms

# Create the form class.
class CreateClientForm(ModelForm):
	class Meta:
		model = Client
		fields = [ 'Client_name' ,  'Client_pass' , 'Client_email','Client_phone'  , 'Client_address','Client_gender','Client_age']
class CreateClassForm(ModelForm):
	class Meta:
		model = Class
		fields = [ "Class_id","Class_name","Class_instructor","Class_capacity"]