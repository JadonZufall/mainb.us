from apps.authentication.models import User
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError


class FilestoreUploadCommand(BaseCommand):
	help = "Upload content to filestore."

	def add_arguments(self, parser) -> None:
		parser.add_argument(
			"-f", "--filepath",
			type=str,
			default="",
			help="The file that you wish to be uploaded to filestore",
		)
		parser.add_argument(
			"-t", "--filetype", 
			type=str, 
			default="",
			help="The type of the file you are trying to upload (optional)."
		)
		parser.add_argument(
			"-u", "--username",
			type=str,
			default="",
			help="Username of the account you wish to be the author of the content.",
		)
		parser.add_argument(
			"-p", "--password",
			type=str,
			default="",
			help="Password of the account you wish to be the author of the content.",
		)
	
	def handle(self, *args, **kwargs) -> None:
		filepath: str = kwargs["filepath"]
		filetype: str = kwargs["filetype"]

		username: str = kwargs["username"]
		password: str = kwargs["password"]
		if len(username) == 0:
			# todo - get username or default to a server account
			pass

		try:
			self.stdout.write(self.style.WARNING("Not implemented"))
		except CommandError as error:
			self.stderr.write(self.style.ERROR(f"Error: {error}"))