from django.core.management.base import BaseCommand
from django.core.management.base import CommandError



class FilestoreDeleteCommand(BaseCommand):
	help = "Delete content from filestore."

	def add_arguments(self, parser):
		super().add_arguments(parser)

	def handle(self, *args, **kwargs) -> None:
		raise NotImplementedError()