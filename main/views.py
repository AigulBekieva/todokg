from django.shortcuts import render, HttpResponse

def homepage(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test.html")

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
