from typing import Optional
from django.db import models
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
			return False
		
		# Username must only contain alpha numeric characters.
		if not username.isalnum():
			return False
		
		return True
	
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
		return self.create_user(username=username, password=password, **kwargs)



class User(AbstractBaseUser):
	username = models.CharField(max_length=32, unique=True)

	is_superuser = models.BooleanField(default=False)

	date_create = models.DateTimeField(auto_now_add=True)
	date_edited = models.DateTimeField(auto_now=True)

	groups = models.ManyToManyField(
		"Permission",
		related_name="user_set",
		blank=True,
		help_text="The groups this user belongs to.",
		verbose_name="groups"
	)

	objects = UserManager()

	USERNAME_FIELD = "username"
	REQUIRED_FIELDS = []			# Username is counted by default as required

	def __str__(self) -> str: return self.username

	def has_permission(self, code: str) -> bool:
		return self.permissions.filter(code=code).exists()

	
