from django.urls import path,include
from . import views

urlpatterns = [
	path("",views.apiOverview.as_view(), name="apiOverview"),
]