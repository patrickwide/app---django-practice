from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# rest_framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle

class OncePerDayUserThrottle(UserRateThrottle):
    rate = '1/day'

# @api_view(['POST'])
@throttle_classes([OncePerDayUserThrottle])
class apiOverview(APIView):	
	def get(self,req):
		print("hello world")
		data = "Hello for today! See you tomorrow!"
		return HttpResponse(data)


# Create your views here.
# def view(request):
#     return Response({"message": "Hello for today! See you tomorrow!"})

