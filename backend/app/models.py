from django.db import models
from django.db.models import Count

class AirlinesModel(models.Model):
    """
    Airlines model
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AirportsModel(models.Model):
    """
    Airports model
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MovementsModel(models.Model):
    """
    Movements model
    """
    description = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.description}"

class FlightsManager(models.Manager):
    """
    Custom manager for FlightsModel
    """
    def get_airport_more_movement(self):
        """
        Get the airport with more movement
        Return { total : int, origin : int}
        """
        max_origin = self.values('origin').annotate(total=Count('id')).latest('total')
        if not max_origin:
            raise self.model.DoesNotExist
        return max_origin

    def get_airlines_more_flights(self):
        """
        Get the airline with more flights
        Return { total : int, airline : int}
        """
        max_airline = self.values('airline').annotate(total=Count('id')).latest('total')
        if not max_airline:
            raise self.model.DoesNotExist
        return max_airline

    def get_day_with_more_flights(self):
        """
        Get the day with more flights
        Return { total : int, day : date}
        """
        max_day = self.values('day').annotate(total=Count('id')).latest('total')
        if not max_day:
            raise self.model.DoesNotExist
        return max_day

    def get_airlines_with_more_than_two_fligths_by_day(self):
        """
        Get the airlines with more than two flights by day
        Return { airline : int, total : int, day : date}
        """
        return self.values('airline', 'day').annotate(total=Count('id')).filter(total__gt=2)


class FlightsModel(models.Model):
    """
    Flights model
    """
    airline = models.ForeignKey(AirlinesModel, on_delete=models.CASCADE)
    origin = models.ForeignKey(AirportsModel, on_delete=models.CASCADE, related_name='origin')
    movement = models.ForeignKey(MovementsModel, on_delete=models.CASCADE)
    day = models.DateField()

    objects = FlightsManager()

    def __str__(self):
        return f"{self.airline} - {self.origin} - {self.movement} - {self.day}"

