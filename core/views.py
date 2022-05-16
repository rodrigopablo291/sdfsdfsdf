
from ast import keyword

from django.shortcuts import render
from core.forms import LoginForm

from django.contrib.auth import authenticate, login
from django.views import View


from django.views import View
from .models import MatchOfertaDemanda

from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'core/index.html', {})

def login_ingresar(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = "Te has identificado de modo correcto"
                    return render(request,'core/django_administrador.html', {'message': message, 'form':form})
                    #return render(request,'core/index.html', {'message': message, 'form':form})
                else:
                    message = "Tu usuario esta inactivo"
            else:
                message = "nombre de usuario y/o password incorrecto"
    else:
        form = LoginForm()
    return render(request,'core/login_ingresar.html', {'message': message, 'form':form})


    
class MatchListView(View):
    api = keyword
    def get(self, request):
        ulist = MatchOfertaDemanda.objects.all()
        return JsonResponse(list(ulist.values('idpymed','demandapyme','idpymeo','ofertapyme')),safe=False)
        
















