from django.db import models
from django.urls import reverse
from apps.authentication.models import User


class WikiTag(models.Model):
	name = models.CharField(
		verbose_name="Tag Name",
		max_length=255,
		unique=True,
		help_text="Name of the tag.",
	)

	def __str__(self):
		return self.name


class WikiArticle(models.Model):
	title = models.CharField(
		verbose_name="title",
		max_length=255,
		unique=False,
		help_text="Path to the article, e.g. /wiki/what-is-django/"
	)
	grub = models.CharField(
		# By default should be equal to the title, but lowercase and cleaned up.
		verbose_name="Grub",
		max_length=255,
		unique=True,
		help_text="Grub is a unique identifier for the article, used in the URL.",
	)

	tags = models.ManyToManyField(
		WikiTag,
		verbose_name="Tags",
		related_name='articles',
		help_text="Tags associated with the article.",
		blank=True,
		default=None,
	)
	author = models.ForeignKey(
		User,
		verbose_name="Author",
		on_delete=models.PROTECT,
		related_name='articles',
		help_text="Author of the article.",
	)
	parent = models.ForeignKey(
		'self',
		verbose_name="Parent Article",
		on_delete=models.CASCADE,
		null=True,
		blank=True,
		default=None,
		related_name='children',
		help_text="Parent article for nested articles.",
	)
	content = models.TextField(
		verbose_name="Content",
		help_text="Content of the article, supports Markdown.",
		blank=True,
		null=False,
		default="",
	)
	created_at = models.DateTimeField(
		verbose_name="Created At",
		auto_now_add=True,
		help_text="Date and time when the article was created.",
	)
	updated_at = models.DateTimeField(
		verbose_name="Updated At",
		auto_now=True,
		help_text="Date and time when the article was last updated.",
	)

	def __str__(self):
		return self.title
	

	def get_path_list(self):
		path = self.parent.get_path_list() if self.parent else []
		path.append(self.grub)
		return path

	def get_absolute_url(self):
		path_list = self.get_path_list()
		return reverse(f"wiki_{len(path_list)}", args=path_list)
	
