from django.views import View
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render

from apps.wiki import models

class WikiView(View):
	def get(self, request: HttpRequest, **kwargs) -> HttpResponse:
		if not request.user.is_authenticated:
			return redirect("authentication_signin")
		
		try:
			last_parent = None
			for i, v in enumerate(list(kwargs.values())):
				last_parent = models.WikiArticle.objects.filter(grub=v, parent=last_parent).get()
		except models.WikiArticle.DoesNotExist:
			return HttpResponse("404 - page not found")
		except models.WikiArticle.MultipleObjectsReturned:
			return HttpResponse("500 - duplicate entries")

		article = last_parent	
		
	
		return render(request, "wiki.html", {
			"content": article.content,
		})
		
	def post(self, request: HttpRequest) -> HttpResponse:
		pass