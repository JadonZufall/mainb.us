from django.contrib import admin
from django.urls import path, include
from . import views
from apps.authentication import urls as authentication_urls
from apps.poker import urls as poker_urls

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('auth/', include(authentication_urls), name="auth"),
    path('poker/', include(poker_urls), name='poker')
]
