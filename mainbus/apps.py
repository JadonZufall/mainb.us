from apps.api.apps import ApiConfig
from apps.authentication.apps import AuthenticationConfig
from apps.base.apps import BaseConfig
from apps.poker.apps import PokerConfig
from apps.authentication.apps import AuthenticationConfig
from apps.factory.apps import FactoryConfig
from apps.filestore.apps import FilestoreConfig
from apps.wiki.apps import WikiConfig
from apps.support.apps import SupportConfig
from apps.vmdash.apps import VMDashConfig
from apps.location.apps import LocationConfig

#todo: currently this does nothing
import os
from django.conf import settings

APPS: list = []
def _locate_apps(dir):
	result = []
	for fp in os.listdir(dir):
		if os.path.exists(os.path.join(fp, "apps.py")):
			result.append(fp)
		elif os.path.isdir(fp):
			result = result + _locate_apps(fp)
	return result
		
		
APPS = _locate_apps(settings.APPS_DIR)
for app in APPS:
	print(f"Located {app}")