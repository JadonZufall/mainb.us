from typing import Optional
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser

class UserManager(BaseUserManager):
    def create_user(self, username: str, email: str, password: Optional[str]=None) -> "User":
        if not username:
            raise ValueError("User must provide a username.")
        
        if not email:
            raise ValueError("User must provide an email address.")
        
        instance: User = self.model(username=username, email=email)
        instance.set_password(password)
        instance.save(using=self._db)
        return instance
    
    def create_super_user(self, email: str, password: Optional[str]=None) -> "User":
        instance: User = self.create_user(email=email, password=password)
        instance.is_admin = True
        instance.save(using=self._db)
        return instance    
    

class User(AbstractUser):
    USERNAME_FIELD: str = "username"
    
    username: models.CharField = models.CharField(
        name="username",
        verbose_name="Username",
        null=False,
        blank=False,
    )
    
    email: models.CharField = models.CharField(
        name="email",
        verbose_name="Email",
        null=False,
        blank=False,
    )
    
    is_active: models.BooleanField = models.BooleanField(
        name="is_active",
        verbose_name="Is Active",
        default=True,
        null=False,
    )
    
    is_admin: models.BooleanField = models.BooleanField(
        name="is_admin",
        verbose_name="Is Admin",
        default=False,
        null=False,
    )
    
    date_created: models.DateTimeField = models.DateTimeField(
        name="date_created",
        verbose_name="Date Created",
        auto_now=True,
    )
    
    date_altered: models.DateTimeField = models.DateTimeField(
        name="date_altered",
        verbose_name="Date Altered",
        auto_now=True,
    )
    
    def __str__(self) -> str:
        return self.username
    
    def has_perm(self, perm, obj=None) -> bool:
        # TODO: Implement permissions system.
        return True
    
    def has_module_perms(self, app_label) -> bool:
        # TODO: Implement module system.
        return True
    

class Group(models.Model):
    name: models.CharField = models.CharField(
        name="name",
        verbose_name="Name",
    )


class Membership(models.Model):
    group: models.ForeignKey = models.ForeignKey(
        name="group",
        verbose_name="Group",
        to=Group,
        on_delete=models.CASCADE,
    )
    
    user: models.ForeignKey = models.ForeignKey(
        name="user",
        verbose_name="User",
        to=User,
        on_delete=models.CASCADE,
    )

