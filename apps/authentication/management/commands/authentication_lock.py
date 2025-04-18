from django.core.management.base import BaseCommand
from django.core.management.base import CommandError



class AuthenticationLockCommand(BaseCommand):
	help = "Lock or unlock an account so that it cannot be logged into."

	def add_arguments(self, parser):
		super().add_arguments(parser)

	def handle(self, *args, **kwargs) -> None:
		raise NotImplementedError()