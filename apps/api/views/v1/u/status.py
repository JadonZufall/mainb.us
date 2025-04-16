from django.views import View
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse

from django.utils import timezone

import apps.authentication.models as models

class UserStatusView(View):
	def get(self, request: HttpRequest, username: str) -> HttpResponse:
		try:
			user: models.User = models.User.objects.get(username=username)
			return JsonResponse(
				{
					"status": "success",
					"data": {
						"is_online": user.is_online,
						"last_online": user.last_online.isoformat() if user.last_online else None,
					}
				}
			)
		except models.User.DoesNotExist:
			return JsonResponse(
				{
					"status": "error", 
					"message": "User not found",
					"code": "USER_NOT_FOUND",
				},
				status=404,
			)

	def post(self, request: HttpRequest, username: str) -> HttpResponse:
		if request.user.is_authenticated and request.user.username == username:
			request.user.last_online = timezone.now()
			request.user.save(update_fields=["last_online"])
			return JsonResponse(
				{
					"status": "success",
					"message": "User.last_online updated successfully",
				}
			)
		return JsonResponse(
			{
				"status": "error", 
				"message": "No permission",
				"code": "FORBIDDEN",
			}, 
			status=403
		)

