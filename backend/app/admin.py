from django.contrib import admin

from .models import AirlinesModel, AirportsModel, MovementsModel, FlightsModel


admin.site.register(AirlinesModel)
admin.site.register(AirportsModel)
admin.site.register(MovementsModel)
admin.site.register(FlightsModel)

