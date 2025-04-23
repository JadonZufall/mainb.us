from django.views import View
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.shortcuts import redirect

from apps.wiki import models


class IndexView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		if not request.user.is_authenticated:
			return redirect("authentication_signin")
		
		page_urls = []
		for article in models.WikiArticle.objects.filter(parent=None):
			page_urls.append(article.get_absolute_url())
		

		return render(request, "wiki_home.html", {"page_urls": page_urls})
		
	def post(self, request: HttpRequest) -> HttpResponse:
		pass