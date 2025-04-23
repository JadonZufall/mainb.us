from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from apps.base import urls as base_urls
from apps.api import urls as api_urls
from apps.authentication import urls as authentication_urls
from apps.poker import urls as poker_urls
from apps.factory import urls as factory_urls
from apps.filestore import urls as filestore_urls
from apps.vmdash import urls as vmdash_urls
from apps.wiki import urls as wiki_urls


urlpatterns = [
    path('', include(base_urls), name="base"),
	path('api/', include(api_urls), name='api'),
    path('admin/', admin.site.urls, name='admin'),
    path('poker/', include(poker_urls), name='poker'),
	path('factory/', include(factory_urls), name='factory'),
	path('f/', include(filestore_urls), name='filestore'),
	path('vmdash/', include(vmdash_urls), name="vmdash"),
	path('wiki/', include(wiki_urls), name="wiki"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + authentication_urls.urlpatterns