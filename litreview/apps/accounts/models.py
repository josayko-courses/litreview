from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Ticket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=128, null=True)
    description = models.CharField(max_length=8192, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
