from django.db import models

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

class FlightsModel(models.Model):
    """
    Flights model
    """
    airline = models.ForeignKey(AirlinesModel, on_delete=models.CASCADE)
    origin = models.ForeignKey(AirportsModel, on_delete=models.CASCADE, related_name='origin')
    movement = models.ForeignKey(MovementsModel, on_delete=models.CASCADE)
    day = models.DateField()

    def __str__(self):
        return f"{self.airline} - {self.origin} - {self.movement} - {self.day}"

