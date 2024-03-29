"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import permissions

from django.contrib import admin
from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import api
from app import api as app_api

schema_view = get_schema_view(
   openapi.Info(
      title="Reto Tecnico Fullstack MD API",
      default_version='v1',
      description="API para el reto tecnico fullstack MD",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="yoandre.saavedra@google.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/answers/responsed/and/notresponsed/', api.AnswersResponsedAndNotResponsedView.as_view(), name='answers-reponsed-and-notresponsed'),
    path('api/answers/high-reputation/', api.AnswersHighReputationView.as_view(), name='high-reputation'),
    path('api/answers/low-number-of-views/', api.AnswersLowNumberOfViewsView.as_view(), name='low-number-of-views'),
    path('api/answers/olds-news/', api.AnswersOldsAndNewsView.as_view(), name='olds-news'),
    path('api/answers/prints/', api.PrintsView.as_view(), name='prints'),

    path('api/flights/airport/more/movement/', app_api.AirportMoreMovement.as_view(), name='flights-airport-more'),
    path('api/flights/airline/more/flights/', app_api.AirlinesWithMoreFlightsView.as_view(), name='flights-airline-more'),
    path('api/flights/day/more/flights/', app_api.DayWithMoreFligthsView.as_view(), name='flights-day-more-flights'),

    path('api/flights/airlines/more/two/fligths/by/day/', app_api.AirlinesWithMoreThanTwoFlightsByDayView.as_view(), name='flights-airlines-more-two-flights-by-day'),

]

