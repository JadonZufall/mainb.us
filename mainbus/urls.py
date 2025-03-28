from django.contrib import admin
from django.urls import path, include
from . import views
from apps.poker import urls as poker_urls

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('signup/', view=views.SignupView.as_view(), name='signup'),
    path('signin/', view=views.SigninView.as_view(), name='signin'),
    path('signout/', view=views.SignoutView.as_view(), name='signout'),
    path('poker/', include(poker_urls), name='poker')
]
