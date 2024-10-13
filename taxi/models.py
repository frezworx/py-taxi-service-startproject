from django.conf import settings
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.db.models import CASCADE


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return (
            f"First name: {self.first_name}, "
            f"last name: {self.last_name}, "
            f"license number: {self.license_number}"
        )


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self) -> str:
        return f"Name: {self.name}, " f"country: {self.country}"


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    def __str__(self) -> str:
        return f"model: {self.model}, drivers: {self.drivers}"
