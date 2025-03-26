from django.http import HttpResponse


def index(request) -> HttpResponse:
	return HttpResponse("<h1>Hello World!</h1>")

def signup(request) -> HttpResponse:
    return HttpResponse("Invalid")

def signin(request) -> HttpResponse:
    return HttpResponse("Invalid")

def signout(request) -> HttpResponse:
    return HttpResponse("Invalid")



