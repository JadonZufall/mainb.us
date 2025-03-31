from django.urls import path, include
from .views import SignupView
from .views import SigninView
from .views import SignoutView

urlpatterns = [
	path('signup/', SignupView.as_view(), name="signup"),
    path('signin/', SigninView.as_view(), name="signin"),
	path('signout/', SignoutView.as_view(), name="signout"),
]