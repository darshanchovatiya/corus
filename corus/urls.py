from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import url
from .views import *
app_name = 'corus'
urlpatterns = [
   path('',views.index,name='Index'),
   path('index',views.index,name='Index'),
   path('product',views.prod,name='Product'),
   path('checkout',views.checkout,name='checkout'),
   path('contect',views.contect,name='Contect'),
   path('about',views.about,name='About Us'),
   path('regu',views.regu,name='User Reg'),
   path('fp',views.fp,name='Forgot Password'),
   path('rege',views.rege,name='Engineer Reg'),
   path('edit_profile',views.edit_profile,name='User Login'),
   path('login',views.login,name='Engineer Login'),
   path('upload',views.prod_view,name='Product Upload'),
   path('logout',views.logout,name='Logout'),
   #path('engliste',views.engliste,name='engineer list'),
   path('englist.html',views.englist,name='engineer list'),
   path('reqe<int:e_id>',views.reqe,name='engineer list'),
   path('englist<int:e_id>',views.dele,name='engineer list'),
   path('videos',views.showvideo,name='Video Upload'),
   
]
