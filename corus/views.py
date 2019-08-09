from django.shortcuts import * 
from .models import item,Uregiser,eregiser
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import *
from django.template import RequestContext
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from corus.forms import *
from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your views here.

#index View
def index(request):
    items = item.objects.all()
    videos =video.objects.all()
    context = {'item' : items,
                'video':videos
    }  
    return render(request,'index.html',context)
#product view
def prod(request):
    items = item.objects.all()
    videos = video.objects.all()
    context = {'item' : items}  
    return render(request, 'product.html', context)
#view for the upload product
def prod_view(request):
    storage = messages.get_messages(request)
    storage.used = True
    if request.method == 'POST':
        form = product(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Product Upload Successfully!')
            return render(request,'upload.html')
    else:
        form = product()
        #messages.error(request,f'Somthing might be wrong!')
    return render(request,'upload.html',{'form':form})

#view for checkout
def checkout(request):
    return render(request, 'about.html')
    #return HttpResponse("This Is our checkout.")
# view for contect page
def contect(request):
    return HttpResponse("This Is contect page")

#view for about pages
def about(request):
    return render(request,'about.html')

#view for registration of user
def regu(request):
    if request.method=="POST":
        name = request.POST.get('myName','')
        City = request.POST.get('City','')
        Pincode = request.POST.get('Pincode','')
        phone = request.POST.get('phone','')
        address = request.POST.get('address','')
        email = request.POST.get('email','')
        Password = request.POST.get('Password','')
        if Uregiser.objects.filter(email = email).exists():            
            if eregiser.objects.filter(contect = phone).exists():
                messages.warning(request,f'Your Email and Phone Number Alrady Exists! Please Try Using Another')
            else:
                messages.error(request,f'Your Email Alrady Exists! Please Try Using Another')
            return render(request,'regu.html')

        elif eregiser.objects.filter(email = email).exists():
            if eregiser.objects.filter(contect = phone).exists():
                messages.warning(request,f'Your Email and Phone Number Alrady Exists as a engineer! Please Try Using Another')
            else:
               messages.error(request,f'Your Email Alrady Exists in Engineer! Please Try Using Another')
            return render(request,'regu.html')
        elif head.objects.filter(email = email).exists():
            messages.error(request,f'This email alrady reserverd for admin! Please Try Using Another')
            return render(request,'rege.html')
        elif Uregiser.objects.filter(contect = phone).exists():
            messages.error(request,f'Your Mobile Number Alrady Registered!')
            return render(request,'regu.html')
        elif eregiser.objects.filter(contect = phone).exists():
            messages.error(request,f'Your Mobile Number Alrady Registered!')
            return render(request,'regu.html')
        else:    
            reg = Uregiser(u_name=name,city=City,area=address,contect=phone,pincode=Pincode,email=email,password=Password)
            reg.save()
            messages.success(request,name +'Account Created for!')
            subject = 'IT SOLUTION HUB'
            message = ' Thanks For Registeation '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,'regu.html')
    else:
        #messages.warning(request,f'Somthing Might Be Wrong Please Tray Again Later!')
        return render(request,'regu.html')
    return render(request,'regu.html')

#view for engineer register
def rege(request):
    if request.method=="POST":
        name = request.POST.get('myName','')
        City = request.POST.get('City','')
        etype = request.POST.get('type','')
        phone = request.POST.get('phone','')
        email = request.POST.get('email','')
        Password = request.POST.get('Password','')
        if eregiser.objects.filter(email = email).exists():
            if eregiser.objects.filter(contect = phone).exists():
                messages.warning(request,f'Your Email and Phone Number Alrady Exists! Please Try Using Another')
            else:
                messages.warning(request,f'Your Email Alrady Exists! Please Try Using Another')
            return render(request,'rege.html')
        elif Uregiser.objects.filter(email = email).exists():
            if Uregiser.objects.filter(contect = phone).exists():
                messages.warning(request,f'Your Email and Phone Number Alrady Exists as a user! Please Try Using Another')
            else:
                messages.warning(request,f'Your Email Alrady Exists as a ! Please Try Using Another')
            return render(request,'rege.html')
        elif head.objects.filter(email = email).exists():
            messages.warning(request,f'This email alrady reserverd for admin! Please Try Using Another')
            return render(request,'rege.html')
        elif eregiser.objects.filter(contect = phone).exists():
            messages.warning(request,f'Your Mobile Number Alrady Registered!')
            return render(request,'rege.html')
        elif Uregiser.objects.filter(contect = phone).exists():
            messages.warning(request,f'Your Mobile Number Alrady Registered as a !')
            return render(request,'rege.html')
        else:    
            reg = eregiser(e_name=name,city=City,e_type=etype,contect=phone,email=email,password=Password)
            reg.save()            
            messages.success(request,name +'your account created is! Wait For Approval to Login')
            subject = 'IT SOLUTION HUB'
            message = ' Thanks For Registeation '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,'rege.html')
    else:
        #messages.warning(request,f'Somthing Might Be Wrong Please Tray Again Later!')
        return render(request,'rege.html')
    return render(request,'rege.html')

#view for admin login currently not in use
def logina(request):
    return HttpResponse("This is admin login page.")

#view for login. login for everyone
def login(request):
    if request.method == 'POST':
        if eregiser.objects.filter(email=request.POST['email'],password=request.POST['Password']).exists():
            loge = eregiser.objects.get(email=request.POST['email'],password=request.POST['Password'])
            if loge.status == 0:
                messages.warning(request,'Your approval is panding')
                return render(request,'login.html',{'dae':loge})
            else:
                request.session["lgne"] ='Welcome' + loge.e_name    
                request.session["prof"] = loge.email       
                return render(request,'login.html',{'dae':loge})
        elif Uregiser.objects.filter(email=request.POST['email'],password=request.POST['Password']).exists():
            loge = Uregiser.objects.get(email=request.POST['email'],password=request.POST['Password'])
            request.session["lgnu"] ='Welcome' + loge.u_name    
            request.session["prof"] = loge.email         
            return render(request,'login.html',{'dae':loge}) 
        elif head.objects.filter(email=request.POST['email'],password=request.POST['Password']).exists():
            loge = head.objects.get(email=request.POST['email'],password=request.POST['Password'])
            request.session["lgna"] ='Welcome' + loge.a_name 
            request.session["prof"] = loge.email           
            return render(request,'login.html',{'dae':loge}) 
        else:
            request.session.modified = True
            messages.warning(request,'Invalid Username Or Password')
            return render(request,'login.html')
    return render(request,'login.html')

#view for logout
def logout(request):
    request.session.modified = True
    request.session.flush()
    request.session.modified = True
    return render(request,'index.html')

#view for forgot password for all users.
def fp(request):
    if request.method == 'POST':  
         email= request.POST.get('email','')
         if eregiser.objects.filter(email=request.POST['email']).exists():
            u = eregiser.objects.get(email=request.POST['email'])
            password=u.password
            subject = 'Recover your password'
            message = 'Your Password is :'+ password
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request,'Your Password Sent Successfully')
            return render(request,'fp.html')
         elif Uregiser.objects.filter(email=request.POST['email']).exists():
              u = Uregiser.objects.get(email=request.POST['email'])
              password=u.password
              subject = 'Recover your password'
              message = 'Your Password is :'+ password
              email_from = settings.EMAIL_HOST_USER
              recipient_list = [email]
              send_mail( subject, message, email_from, recipient_list )
              messages.success(request,'Your Password Sent Successfully')
              return render(request,'fp.html')
         elif head.objects.filter(email=request.POST['email']).exists():
              u = head.objects.get(email=request.POST['email'])
              password=u.password
              subject = 'Recover your password'
              message = 'Your Password is :'+ password  
              email_from = settings.EMAIL_HOST_USER
              recipient_list = [email]
              send_mail( subject, message, email_from, recipient_list )
              messages.success(request,'Your Password Sent Successfully')
              return render(request,'fp.html')
         else:
             messages.warning(request,'Your email is not exists.')
             return render(request,'fp.html')
    else:
       return render(request,'fp.html')

#view for edit profile for all users
def edit_profile(request):
    if Uregiser.objects.filter(email=request.session["prof"]).exists():
            user = Uregiser.objects.get(email=request.session["prof"])
            form = editprofile(instance=user)
            if request.method == "POST":
                form = editprofile(request.POST, request.FILES, instance=user)
                if form.is_valid():
                    update = form.save(commit=False)               
                    update.user = user
                    update.save()
                    messages.success(request,'Profile Update Successfully')
    elif eregiser.objects.filter(email=request.session["prof"]).exists():
            user = eregiser.objects.get(email=request.session["prof"])
            form = engprofile(instance=user)
            if request.method == "POST":
                form = engprofile(request.POST, request.FILES, instance=user)
                if form.is_valid():
                    update = form.save(commit=False)               
                    update.user = user
                    update.save()
                    messages.success(request,'Profile Update Successfully')
                    #return render(request, 'profileu.html')
    return render(request, 'edit_profile.html', {'form': form})
   
#view for engineer list
def englist(request):  
    istekler = eregiser.objects.all()
    return render(request, 'englist.html', locals())

#view for delete engineer request
def dele(request, e_id):
    eregiser.objects.get(e_id=e_id).delete()
    messages.warning(request,'Rejected Successfully')
    return redirect('englist.html')

#view for accept engineer
def reqe(request,e_id):
    eregiser.objects.filter(e_id=e_id).update(status=1)
    messages.success(request,'Engineer Approved Successfully')
    return redirect('englist.html')

def showvideo(request): 
    storage = messages.get_messages(request)
    storage.used = True
    if request.method == 'POST':
        form= VideoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()    
            messages.success(request,'Product Upload Successfully!')
            return render(request,'videos.html') 
    else:
        form = VideoForm()
        #messages.error(request,f'Somthing might be wrong!')
    return render(request,'videos.html',{'form':form})  

def videolist(request):  
    ist = video.objects.all()
    return render(request, 'englist.html', locals())    

#view for delete engineer request
def dele(request, e_id):
    #video.objects.get(e_id=e_id).delete()
    messages.warning(request,'Rejected Successfully')
    return redirect('englist.html')
