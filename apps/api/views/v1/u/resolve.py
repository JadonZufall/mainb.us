from django.views import View
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse

from django.utils import timezone

import apps.authentication.models as models

class UserResolveView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		if request.user.is_authenticated:
			return JsonResponse(
				{
					"status": "success",
					"data": {
						"username": request.user.username,
					},
				},
			)
		return JsonResponse(
			{
				"status": "error",
				"message": "User not authenticated",
				"code": "UNAUTHORIZED"
			},
			status=401,
		)



