from django.db import models


class PlayerRecord(models.Model):
	steam_id = models.CharField(max_length=32, unique=True)
	is_trade_banned = models.BooleanField(default=False)
	is_vac_banned = models.BooleanField(default=False)

	def __str__(self) -> str: return self.steam_id

	