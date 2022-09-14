from dataclasses import field
from django import forms
from .models import *
class clientForm(forms.ModelForm):
    class Meta:
        model=clients
        fields = '__all__'
        labels = {'name':'Name', 'photo':'', 'type':'Type', 'description':'Description', 'bill':'Bill'}
class staffForm(forms.ModelForm):
    class Meta:
        model = staff
        fields='__all__'
        labels = {'name':'Name', 'phone':'Phone', 'address':'Address', 'category':'Category', 'gender':'Gender', 'branchName':'BranchName'}
class foodForm(forms.ModelForm):
    class Meta:
        model=food
        fields='__all__'
        labels = {'name':'Name', 'description':'Description','price':'Price'}
class branchForm(forms.ModelForm):
    class Meta:
        model = branch
        fields = '__all__'
        labels = {'name':'Name', 'location':'Location', 'phone':'Phone'}