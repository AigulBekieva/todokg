from django.shortcuts import render, HttpResponse
from .models import ToDo

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list= ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def go(request):
    return render(request, "go.html")
            
def check(request):
    return HttpResponse("текшеруу")

def third(request):
    return HttpResponse("This is page test3")   

def hw31(request):
    return HttpResponse("Сиздин жазуунуз ийгиликтуу кошулду.")   

def hw31change(request):
    return HttpResponse("Сиздин жазуунуз ийгиликтуу озгортулду.")    

def hw31del(request):
    return HttpResponse("Сиздин жазуунуз жок кылынды.")    
