from typing import Optional

from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

class Group(models.Model):
	name = models.CharField(max_length=128, unique=True)
	desc = models.TextField(null=True, blank=True)
	permissions = models.ManyToManyField("Permission", blank=True)

	def __str__(self) -> str: return self.name

	def has_permission(self, code: str) -> bool:
		return self.permissions.filter(code=code).exists()

	def get_users(self):
		return User.objects.filter(groups=self)

class Permission(models.Model):
	name = models.CharField(max_length=128, unique=True)
	code = models.SlugField(unique=True)
	desc = models.TextField(null=True, blank=True)

	def __str__(self) -> str: return self.name


class UserManager(BaseUserManager):
	def validate_username(self, username: str) -> tuple[bool, str]:
		# Username must be 5 characters or longer.
		if len(username) < 5:
			return False, "Password must be 5 character or longer."
		
		# Username must only contain alpha numeric characters.
		if not username.isalnum():
			return False, "Password may only contain alpha numeric characters."
		
		return True, "Okay"
	
	def create_user(self, username: str, password: str=None, **kwargs) -> "User":
		if not username:
			raise ValueError("Username is a required field.")
		
		#^ Validate the username.
		is_valid, reason = self.validate_username(username)
		if not is_valid:
			raise ValueError(reason)

		#^ Create the user.
		instance: User = self.model(username=username, **kwargs)
		instance.set_password(password)
		instance.save(using=self._db)
		return instance
	
	def create_superuser(self, username: str, password: str=None, **kwargs) -> "User":
		kwargs.setdefault("is_superuser", True)
		kwargs.setdefault("is_staff", True)
		return self.create_user(username=username, password=password, **kwargs)



class User(AbstractBaseUser):
	username = models.CharField(max_length=32, unique=True)

	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	date_created = models.DateTimeField(auto_now_add=True)
	date_altered = models.DateTimeField(auto_now=True)

	last_online = models.DateTimeField(null=True, default=None)

	groups = models.ManyToManyField(
		Group,
		related_name="user_set",
		blank=True,
		help_text="The groups this user belongs to.",
		verbose_name="groups",
	)

	permissions = models.ManyToManyField(
		Permission,
		related_name="permissions_set",
		blank=True,
		help_text="The permissions this user holds.",
		verbose_name="permissions",
	)

	objects = UserManager()

	USERNAME_FIELD = "username"
	REQUIRED_FIELDS = []			# Username is counted by default as required

	def __str__(self) -> str: return self.username

	def has_perm(self, code: str) -> bool:
		if self.is_superuser:
			return True

		return self.permissions.filter(code=code).exists()

	def has_module_perms(self, label: str) -> bool:
		if self.is_superuser:
			return True
		
		#todo implement this function properly.
		return False
	
	@property
	def is_online(self) -> bool:
		if self.last_online is None:
			return False
		else:
			return self.last_online >= timezone.now() - timedelta(minutes=5)


	
