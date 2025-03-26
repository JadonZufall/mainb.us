from django.http import HttpResponse


def index(request) -> HttpResponse:
	return HttpResponse("<h1>Hello World!</h1>")

