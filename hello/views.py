from django.http import HttpResponseRedirect
from django.shortcuts import render
from hello import models
import cgi

def index(request):
    return render(request, "index.html")

def index_after(request):
    return render(request, "index_after.html")

def log_in(request):
    return render(request, "log_in.html")

def contacts(request):
    return render(request, "contacts.html")

def registration(request):
    n = 100
    years = [0]*n
    for i in range(100):
        years[i] = i

    # получаем из данных запроса POST отправленные через форму данные
    if request.method == "POST":
        nickname = request.POST.get("name", "Undefined")
        email = request.POST.get("email", "Undefined")
        password = request.POST.get("password", "Undefined")
        age = request.POST.get("age", "Undefined")
        gender = request.POST.get('gender')
        #age = personal_data.getElementByName("gender")
        
        models.add_user(nickname, email, password, age, gender, 1, 0)
        return HttpResponseRedirect("/registration")

    return render(request, "registration.html", context={"years": years})