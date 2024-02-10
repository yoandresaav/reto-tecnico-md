from rest_framework import serializers

from .models import AirlinesModel, AirportsModel, FlightsModel, MovementsModel



class AirportsModelSerializer(serializers.ModelSerializer):
    """Serializer for the AirportsModel model."""

    class Meta:
        model = AirportsModel
        fields = '__all__'


class AirlinesModelSerializer(serializers.ModelSerializer):
    """Serializer for the AirlinesModel model."""

    class Meta:
        model = AirlinesModel
        fields = '__all__'
