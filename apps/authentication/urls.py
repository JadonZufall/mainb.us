from django.urls import path
from views.authentication_action_signup import SignupView
from views.authentication_action_signin import SigninView
from views.authentication_action_signout import SignoutView
from views.authentication_inspect import InspectView
from views.authentication_inspect_group import InspectGroupView
from views.authentication_inspect_permission import InspectPermissionView
from views.authentication_inspect_user import InspectUserView
from views.authentication_user_profile import UserProfileView
from views.authentication_group_profile import GroupProfileView

# this one has to be weird cuz I want it to be
# <url>/u/<username>
# <url>/g/<groupname>
# <url>/a/signup
# <url>/a/signin
# <url>/a/signout
urlpatterns = [
	path("/a/signup/", SignupView.as_view(), name="authentication_signup"),
	path("/a/signin/", SigninView.as_view(), name="authentication_signin"),
	path("/a/signout/", SignoutView.as_view(), name="authentication_signout"),
	path("/a/inspect/", InspectView.as_view(), name="authentication_inspect"),
	path("/a/inspect/<str:permissionname>", InspectPermissionView.as_view(), name="authentication_inspect_group"),
	path("/a/inspect/<str:groupname>", InspectGroupView.as_view(), name="authentication_inspect_permission"),
	path("/a/inspect/<str:username>", InspectUserView.as_view(), name="authentication_inspect_user"),
	path("/u/<str:username>", UserProfileView.as_view(), name="authentication_user_profile"),
	path("/g/<str:groupname>", GroupProfileView.as_view(), name="authentication_group_profile"),
]