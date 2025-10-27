from django.http import HttpResponse

def index(request):
    return HttpResponse("УРАРАРАРРАРА")

def about(request):
    return HttpResponse("ЗАРАБОТАЛО УРА УРА УРА УРА УРА")

def contact(request):
    return HttpResponse("НАКОНЕЦ_ТО НАКОНЕЦ_ТО")