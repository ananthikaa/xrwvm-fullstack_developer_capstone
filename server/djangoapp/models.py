from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):

    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'

    CAR_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
    ]

    car_make = models.ForeignKey(
        CarMake,
        on_delete=models.CASCADE
    )

    dealer_id = models.IntegerField(default=0)

    name = models.CharField(max_length=100)

    type = models.CharField(
        max_length=20,
        choices=CAR_CHOICES,
        default=SEDAN
    )

    year = models.IntegerField(
        default=now().year,
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )

    def __str__(self):
        return self.car_make.name + " " + self.name