from django import forms
from .models import *

class product(forms.ModelForm):
        class Meta:
            model = item
            fields = ['p_name','price','stock','desc','image']
            labels  = {
                'p_name':'Product Name', 
                'price':'Price of Product', 
                'stock':'Stock Of Product', 
                'desc':'Product Discription', 
                'image':'Image Of Product'
            }
class editprofile(forms.ModelForm):
    class Meta:
        model=Uregiser
        fields=['u_name','city','area','contect','pincode','password']
        labels  = {
                'u_name':'User Name', 
                'city':'City', 
                'area':'Address', 
                'contect':'Contect', 
                'pincode':'Pincode',
                'password':'Password',
            }

class engprofile(forms.ModelForm):
    class Meta:
        model=eregiser
        fields=['e_name','contect','e_type','city','password']
        labels  = {
                'e_name':'Engineer Name', 
                'contect':'Contect', 
                'e_type':'Engineer Type', 
                'city':'City', 
                'password':'password'
            }
class VideoForm(forms.ModelForm):
    class Meta:
        model= video
        fields= ["v_name", "video","discr"]
        labels  = {
                'v_name':'Video Name', 
                'video':'Upload Video', 
                'desc':'Video Discription', 
        }