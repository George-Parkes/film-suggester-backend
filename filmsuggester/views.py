from django.http import HttpResponse

def message(request):
    return HttpResponse("Hello, world!")
