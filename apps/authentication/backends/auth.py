from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied


class AuthenticationBackend(ModelBackend):
	def authenticate(self, request, username=None, password=None, **kwargs):
		UserModel = get_user_model()
		try:
			user = UserModel.objects.get(username__iexact=username)
			if user.check_password(password) and self.user_can_authenticate(user):
				return user
		except UserModel.DoesNotExist:
			UserModel().set_password(password)
			return None
	
	def user_can_authenticate(self, user):
		if not user.is_active:
			raise PermissionDenied("This account is inactive")
		
		if user.is_locked:
			raise PermissionDenied("This account is locked.")
		
		if user.is_bot:
			raise PermissionDenied("This account is a bot and cannot be logged into.")

		return True
	
	def get_user(self, user_id):
		UserModel = get_user_model()
		try:
			return UserModel.objects.get(pk=user_id)
		except UserModel.DoesNotExist:
			return None