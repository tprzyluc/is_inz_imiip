from django.http import HttpResponse

def start(request):
    return HttpResponse("<h1> Start </h1>")
    