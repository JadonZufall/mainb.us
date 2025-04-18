from django.core.management.base import BaseCommand
from django.core.management.base import CommandError



class FilestoreDeleteCommand(BaseCommand):
	help = "Extract content from filestore and put it somewhere else."

	def add_arguments(self, parser) -> None:
		super().add_arguments(parser)

	def handle(self, *args, **kwargs) -> None:
		raise NotImplementedError()