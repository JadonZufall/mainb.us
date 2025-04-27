from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

import os
import sys
import subprocess

from django.conf import settings



class Command(BaseCommand):
	help = "Compile static files."

	def add_arguments(self, parser):
		super().add_arguments(parser)

	def handle(self, *args, **kwargs) -> None:
		print("Compiling static files...")
		for app_dir in os.listdir(settings.APPS_DIR):
			print("Compiling static files for app:", app_dir)
			wd = os.path.join(settings.APPS_DIR, app_dir, "static", "ts")
			if not os.path.exists(wd):
				print("No ts directory found in", app_dir)
				continue
			print(wd)
			result = subprocess.run("tsc", cwd=wd, capture_output=True, text=True, check=True)
			print(result.stdout)