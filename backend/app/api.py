from rest_framework.views import APIView
from rest_framework.response import Response

from django.db.models import Count

from .models import AirlinesModel, AirportsModel, FlightsModel, MovementsModel
from .serializers import AirportsModelSerializer, AirlinesModelSerializer


class AirportMoreMovement(APIView):
    """View to get the airport with more movement."""
    allowed_methods = ['GET']

    def get(self, request):
        """Return the airport with more movement."""

        max_origin = FlightsModel.objects.get_airport_more_movement()

        if not max_origin:
            return Response({
                "airport_more_movement": None,
                "total_fligths": 0,
            })

        origin = max_origin['origin']
        total = max_origin['total']

        # Get the airport with more movement
        airport = AirportsModel.objects.get(id=origin)

        serializer = AirportsModelSerializer(airport)

        return Response({
            "airport_more_movement": serializer.data,
            "total_fligths": total,
        })


class AirlinesMoreFlights(APIView):
    """View to get the airline with more flights."""
    allowed_methods = ['GET']

    def get(self, request):
        """Return the airline with more flights."""

        max_airline = FlightsModel.objects.get_airlines_more_flights()

        if not max_airline:
            return Response({
                "airline_more_flights": None,
                "total_fligths": 0,
            })

        airline = AirlinesModel.objects.get(id=max_airline['airline'])
        total = max_airline['total']

        serializer = AirlinesModelSerializer(airline)

        return Response({
            "airline_more_flights": serializer.data,
            "total_fligths": total,
        })
