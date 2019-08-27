from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .map import Map
from .form import FormLogin
from .manipulatorJson import Generator

# Create your views here.
#Static;
global KEY_MAPS
KEY_MAPS = "AIzaSyBMglCkfaEDPOIdLPfCEfSUVI6rl1ONQNQ"

def search_adress(request):
    if request.method == "GET":
        map_app = Map(KEY_MAPS)
        xd = map_app.geocode("Rio Tinto Paraiba")
        if xd != None:
            generator = Generator("Rio Tinto Paraiba")
            result = generator.createMyResponse(xd)
        
        return render(request,'map.html')

    


# retorna a pagina inicial contendo o mapa de navegação;
def index(request):
    if request.method == "GET":
        return render(request,'map.html')
    pass

# retorna a pagina de login;
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user != None:
            if user.is_active:
                login(request,user)
                # redirect index - agora com user autenticado;
                return redirect('')
        else:
            # credencial errada;
            return redirect('error/')
    pass

# create conta;
def create_account(request):
    pass

def helper(request):
    pass

def contact(request):
    pass

def about(request):
    pass

def error(request):
    if request.method == "GET":
        return render(request,'error.html')

