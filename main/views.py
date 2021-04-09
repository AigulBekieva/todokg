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