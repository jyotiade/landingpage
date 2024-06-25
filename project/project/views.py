from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>welcome to my world</h1>")