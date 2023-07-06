from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import requests
import json
#from propio import hola




# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello Worlda</h1>")

def about(request):
    return HttpResponse("About")

def esta(request):
    return render(request, "index.html")

def inicio(request):
    if request.method=='GET':
        return render(request, "inicio/index.html",{'form': AuthenticationForm})
    else:
        name = request.POST["username"]
        psswd = request.POST["password"]
        user = authenticate(username=name, password=psswd)
        if user is None:
            return render(request, "inicio/index.html",{'form': AuthenticationForm, 'error': "Usuario y/o contraseña incorrectos"})
        else:
            login(request, user)
            return redirect("home/")



def registro(request):
    if request.method=='GET':
        return render(request, "registro/index.html",{'form' : UserCreationForm})
    else:
        if request.POST["password1"]!=request.POST["password2"]:
            return render(request, "registro/index.html",{'form' : UserCreationForm, 'error': "Las contraseñas no coinciden"})
        else:
            name = request.POST["username"]
            psswd = request.POST["password1"]
            user= User.objects.create_user(username=name, password=psswd)
            user.save
            return render(request, "registro/index.html",{'form' : UserCreationForm, 'error': "usuario registrado"})

#@login_required        
def home(request):
    return render(request,"home/index.html")

def salir(request):
    logout(request)
    return redirect('../')


def ha(request):
    url="http://www.themealdb.com/api/json/v1/1/random.php"

    r = requests.get(url)

    jsonStr1 = r.text
    jsonStr1 = jsonStr1[10:-2]

    jsondicc = json.loads(jsonStr1)
    nombre=jsondicc.get("strMeal")

    #texto1= ("vamos a hacer:"+nombre+"\n")
    #texto = (texto1 + "hola gola"+ "\n")
    archivo = open("temporal/texto.txt", "w")
    print(archivo.mode)


    return HttpResponse(jsonStr1)
    #return render(request, "ha/index.html", data)

@login_required
def api(request):
    def ingredie(dicc):
        lista=[]
        paso=True
        i=1
        while paso==True:
            ingrediente= dicc.get("strIngredient"+str(i))
            if (len(ingrediente) != 0):
                lista.append(ingrediente)
                i=i+1
            else:
                paso=False
        return lista
    
    nombreT=open("temporal/nombre.txt", "w")
    pasosT=open("temporal/pasos.txt", "w")
    ingredientesT=open("temporal/ingredientes.txt", "w")
    url="http://www.themealdb.com/api/json/v1/1/random.php"

    r = requests.get(url)

    jsonStr1 = r.text
    jsonStr1 = jsonStr1[10:-2]

    jsondicc = json.loads(jsonStr1)
    nombre=jsondicc.get("strMeal")
    nombreT.write(jsondicc.get("strMeal"))
    pasosT.write(jsondicc.get("strInstructions"))
    ingredientesT.write(str(ingredie(jsondicc)))
    nombreT.close()
    pasosT.close()
    ingredientesT.close()
    #print(ingredie(jsondicc))
    name= "<h3>Nombre de la receta:<h3/>" + "<h4>"+str(jsondicc.get("strMeal"))+ "<h4/>"
    prep="<h3>Instrucciones:<h3/>"+"<h4>"+str(jsondicc.get("strInstructions"))+"<h4/> \n"
    prep= prep + '<div> <a href="../api">Otra receta</a> <div/>'
    prep= prep + '<div> <a href="../home">Volver</a> <div/>'
    prep= prep + '<div> <a href="../salir">Salir</a> <div/>'

    return HttpResponse(name+prep)
    #return render(request,"api/index.html")
