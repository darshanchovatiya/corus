from django.db import models
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save

from django.contrib.auth.models import User
# Create your models here.
# Product Table
class item(models.Model):
    p_id=models.AutoField(primary_key=True)
    p_name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    stock=models.IntegerField(default=0)
    rating=models.FloatField(default=0)
    desc=models.CharField(max_length=300)
    image=models.ImageField(upload_to="image",default="")
    def __str__(self):
        return self.p_name
    
#Register table For User
class Uregiser(models.Model):
    u_id     = models.AutoField(primary_key=True)
    u_name   = models.CharField(max_length=50)
    city     = models.CharField(max_length=50)
    area     = models.CharField(max_length=50)
    contect  = models.CharField(max_length=13)
    pincode  = models.IntegerField(default=0)
    email    = models.CharField(max_length=30,unique = True)
    password = models.CharField(max_length=15)
    def __str__(self):
        return self.u_name

#def create_profile(sender, **kwargs):
 #   if kwargs['created']:
 #       user_profile = Uregiser.objects.create(user=kwargs['instance'])
#post_save.connect(create_profile, sender=Uregiser)
#for Dropdown Purpose
engtype = [('Os','Os'),('Cameras','Cameras'),('Hardware','Hardware')]
#engineer Register Tabel
class eregiser(models.Model):
    e_id     = models.AutoField(primary_key=True)
    e_name   = models.CharField(max_length=50)
    contect  = models.CharField(max_length=10)
    e_type   = models.CharField(max_length=30,choices=engtype)
    city     = models.CharField(max_length=30)
    email    = models.CharField(max_length=30,unique = True)
    password = models.CharField(max_length=15)
    feedback = models.FloatField(default=0.0)
    status   = models.IntegerField(default=0)
    def __str__(self):
        return self.e_name



#def eng_profile(sender, **kwargs):
#    if kwargs['created']:
#        user_profile = eregiser.objects.create(user=kwargs['instance'])
#post_save.connect(create_profile, sender=eregiser)

#For Server Order Tabel
class server(models.Model):
    s_id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=30)
    switch = models.IntegerField(default=8)
    contact = models.CharField(max_length=13)
    def __str__(self):
        return self.company
  
#tabel for admin
class head(models.Model):
    a_id = models.AutoField(primary_key=True)
    a_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30,unique = True)
    password = models.CharField(max_length=15)  
    def __str__(self):
        return self.a_name

#complain table for complain
class complain(models.Model):
    c_id = models.AutoField(primary_key=True)
    u_id = models.ForeignKey(Uregiser, on_delete=models.CASCADE)
    u_name = models.CharField(max_length=30)
    c_type = models.CharField(max_length=30)
    c_desc = models.CharField(max_length=200)
    status = models.IntegerField(default=0)
    image = models.ImageField(upload_to="image",default="")
    def __str__(self):
        return self.u_name
   
#transection tabel for report and bills
class transection(models.Model):
    b_id = models.AutoField(primary_key=True)
    u_id = models.ForeignKey(Uregiser, on_delete=models.CASCADE)
    c_id = models.ForeignKey(complain, on_delete=models.CASCADE)
    e_id = models.ForeignKey(eregiser, on_delete=models.CASCADE)
    u_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    c_desc = models.CharField(max_length=200)
    status = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    def __str__(self):
        return self.u_name
   
#order table for store order data
class order(models.Model):
    o_id = models.AutoField(primary_key=True)
    u_id = models.ForeignKey(Uregiser, on_delete=models.CASCADE)
    p_id = models.ForeignKey(item, on_delete=models.CASCADE)
    p_name = models.CharField(max_length=30)
    u_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.u_name
   
class video(models.Model):
    v_id = models.AutoField(primary_key=True)
    v_name = models.CharField(max_length=30)
    video = models.FileField(upload_to='videos', null=True, verbose_name="")
    discr = models.CharField(max_length=200)
    def __str__(self):
        return self.v_name
       


