from django.urls import path
from apps.wiki.views.index import IndexView
from apps.wiki.views.wiki import WikiView

# Absolutely scuffed way of doing this, but it works for now.
urlpatterns = [
	path("", IndexView.as_view(), name="wiki"),
] + [path("".join([f"<str:path_{j}>/" for j in range(1, i+1)]), WikiView.as_view(), name=f"wiki_{i}") for i in range(1, 16)]
