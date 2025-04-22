"""
For countries and states reference
https://github.com/dr5hn/countries-states-cities-database
"""
from django.db import models


class Currency(models.Model):
	name = models.CharField(
		verbose_name="Name",
		max_length=64,
		unique=True,
		help_text="The name of the currency.",
	)
	iso = models.CharField(
		verbose_name="ISO",
		max_length=3,
		unique=True,
		help_text="The unique 3 characters representing this currently",
	)
	symbol = models.CharField(
		verbose_name="Symbol",
		max_length=16,
		unique=False,
		help_text="The symbol that this currency uses.",
		default="?",
	)
	long_symbol = models.CharField(
		verbose_name="Long Symbol",
		max_length=32,
		unique=True,
		help_text="The long symbol that this currency uses that is unique to itself.",
		default=None,
		null=True,
	)
	


class Region(models.Model):
	name = models.CharField(
		verbose_name="Name",
		max_length=64,
		unique=True,
		help_text="The name of the region.",
	)


class SubRegion(models.Model):
	name = models.CharField(
		verbose_name="Name",
		max_length=64,
		unique=True,
		help_text="The name for the sub region.",
	)
	code = models.CharField(
		verbose_name="Code",
		max_length=16,
		unique=True,
		help_text="The code for the sub region.",
	)
	region = models.ForeignKey(
		Region,
		related_name="subregion_of",
		on_delete=models.CASCADE,
		help_text="Region that this subregion belongs to",
	)


class Country(models.Model):
	name = models.CharField(
		verbose_name="Name",
		max_length=64,
		unique=True,
		help_text="The name of the country",
	)
	sub_region = models.ForeignKey(
		SubRegion,
		related_name="country_of",
		on_delete=models.PROTECT,
		help_text="Sub region this country is located in",
	)
	currency = models.ForeignKey(
		Currency,
		related_name="offical_currency",
		on_delete=models.SET_NULL,
		help_text="The offical currency of the country",
		null=True,
		default=None,
	)


class State(models.Model):
	name = models.CharField(
		verbose_name="Name",
		max_length=64,
		help_text="The name of the state",
	)
	country = models.ForeignKey(
		Country,
		related_name="state_of",
		on_delete=models.PROTECT,
	)
	latitude = models.FloatField(
		verbose_name="Latitude",
		help_text="The latitude of the state.",
	)
	longitude = models.FloatField(
		verbose_name="Longitude",
		help_text="The longitude of the state.",
	)


class City(models.Model):
	name = models.CharField(
		verbose_name="Name",
		max_length=64,
	)
	state = models.ForeignKey(
		State,
		related_name="city_of",
		on_delete=models.PROTECT,
	)
	latitude = models.FloatField(
		verbose_name="Latitude",
		help_text="The latitude of the state.",
	)
	longitude = models.FloatField(
		verbose_name="Longitude",
		help_text="The longitude of the state."
	)