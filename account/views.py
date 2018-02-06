from django.shortcuts import render, redirect
from rest_framework import viewsets
from account.forms import UserLoginForm
from account.models import Person, Labor
from django.http.response import HttpResponse
from django.urls.base import reverse
#from .serializers import PersonSerializer, LaborSerializer, LabtransSerializer

# Create your views here.
def index(request):
    
    return render(request, 'index.html') #HttpResponse('This is the index page!!')

def account_register(request):
    
           
    return render(request, 'register.html')

def account_profile(request):
    
    return "I am account Info"

def account_edit(request):
    
    return "I am Account Edit"

def account_login(request):
    
    if request.method == 'POST':
    
        m = Labor.objects.get(laborcode=request.POST['laborcode'])
        #m = authenticate(email=request.POST['email'], password=make_password(request.POST['password']))
    
        #if check_password(request.POST['password'], m.portalpwd):
        if request.POST['password'] == m.portalpwd:
            request.session['laborcode'] = m.laborcode
            request.session['is_login'] = True
        
            #return vars(m)
            #return HttpResponse(vars(m))
            #memberdata = {'username': m.username, 'email': m.email}
            #return render(request, 'account_profile.html', {'memberdata': memberdata})
            return redirect(reverse('index'))
    
        else:
        
            return HttpResponse('Your email or password is not correct!')
    

    else:
        
        user_form = UserLoginForm()
        
    return render(request, 'login.html', {'loginform': user_form})   

def account_logout(request):
    
    try:
        
        del request.session['member_id']
        
    except KeyError:
        
        pass
    
    return HttpResponse('You are logged out!')    


