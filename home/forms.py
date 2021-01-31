from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model= image
        fields = [
            # 'img',
            'name',
            'pro_type',
            'pro_con',
            'pro_Loc',
            'pro_price',
            'latitude',
            'logitude',
            'auther'
            
            
        ]
       
        widgets={
              'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Name of the Product'}),
              'pro_type': forms.TextInput(attrs={'class':'form-control','placeholder':'Product Type'}),
              'pro_con': forms.TextInput(attrs={'class':'form-control','placeholder':'Contact Number'}),
              'pro_Loc': forms.TextInput(attrs={'class':'form-control','placeholder':'Seller Location'}),
              'pro_price': forms.TextInput(attrs={'class':'form-control','placeholder':'Product Price'}),
              'latitude': forms.TextInput(attrs={'class':'form-control','id':'lat','type':'hidden','value':'','placeholder':'Name of the Product'}),
              'logitude': forms.TextInput(attrs={'class':'form-control','id':'log','type':'hidden','value':'','placeholder':'Name of the Product'}),
              'auther': forms.TextInput(attrs={'class':'form-control','id':'user','type':'hidden','value':'{{request.user.id}}','name':'user_id'}),
              

             }

class customerForm(forms.ModelForm):


    class Meta:
        model=userprofile
        fields = [
            'pic',
            
        ]

class PhoneForm(forms.ModelForm):


    class Meta:
        model=userphone
        fields = [
            'phone',
            
        ]

        widgets={
            'phone':forms.TextInput(attrs={'class':'form-control','row':1,'col':40,'style':'width:10rem','placeholder':'Phone no'})
        }
