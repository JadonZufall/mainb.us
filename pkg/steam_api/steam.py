from typing import Optional
import requests

import pkg.steam_api.steam_ids as steam_ids


"https://api.steampowered.com/IEconItems_730/GetPlayerItems/v1/"
"https://api.steampowered.com/ISteamUser/GetPlayerBans/v1/"
"https://api.steampowered.com/ISteamUser/GetUserGroupList/v1/"
"https://api.steampowered.com/ITrustService/GetTrustScore/v1/"
"https://partner.steam-api.com/ISteamEconomy/CanTrade/v1/"
"https://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?steamids=sdf"

class SteamAPIError(Exception):
	pass


class SteamAPI:
	def __init__(self, api_key: str):
		self.api_key = api_key
	
	def _format_url(self, service: str, method: str, version: str="v1", **kwargs) -> str:
		url = f"https://api.steampowered.com/{service}/{method}/v1/"
		if kwargs:
			url += "?" + "&".join([f"{k}={v}" for k, v in kwargs.items()])
		return url
	
	def get_inventory(self, steam_id: str, app_id: Optional[str]=None) -> dict:
		request = requests.get(self._format_url("IInventoryService", "GetPlayerItems", version="v1", steam_id=steam_id, appid=app_id, key=self.api_key))
		if request.status_code != 200:
			raise SteamAPIError(f"Failed to get inventory: {request.status_code} {request.text}")
		return request.json()


class SteamInventory:
	def __init__(self) -> None:
		pass


class SteamUser:
	def __init__(self, steam_id: Optional[str]=None, vanity_url: Optional[str]=None):
		self._steam_id = steam_id
		self._vanity_url = vanity_url

		if not self._steam_id and not self._vanity_url:
			raise SteamAPIError("Either steam_id or vanity_url must be provided")
	
	@property
	def is_trade_banned(self, api: SteamAPI) -> bool:
		if not self.steam_id:
			raise SteamAPIError("Steam ID is required to check trade ban")
		request = requests.get(api._format_url("ISteamEconomy", "CanTrade", version="v1", steam_id=self.steam_id, key=api.api_key))
		if request.status_code != 200:
			raise SteamAPIError(f"Failed to check trade ban: {request.status_code} {request.text}")
		return request.json().get("trade_banned", False)

	@property
	def is_vac_banned(self, api: SteamAPI) -> bool:
		if not self.steam_id:
			raise SteamAPIError("Steam ID is required to check VAC ban")
		request = requests.get(api._format_url("ISteamUser", "GetPlayerBans", version="v1", steam_id=self.steam_id, key=api.api_key))
		if request.status_code != 200:
			raise SteamAPIError(f"Failed to check VAC ban: {request.status_code} {request.text}")
		return request.json().get("players", [{}])[0].get("VACBanned", False)
	
	def get_inventory(self, api: SteamAPI, app_id: Optional[str]=None) -> dict:
		if not self.steam_id:
			raise SteamAPIError("Steam ID is required to get inventory")
		return api.get_inventory(self.steam_id, app_id=app_id)
	
	@staticmethod
	def resolve_vanity_url(vanity_url: str) -> str:
		pass

	@property
	def steam_id(self) -> str:
		if not self._steam_id:
			self._steam_id = self.resolve_vanity_url(self._vanity_url)
		return self._steam_id

	@property
	def url(self) -> str:
		return f"http://steamcommunity.com/profiles/{self.steam_id}"
	



