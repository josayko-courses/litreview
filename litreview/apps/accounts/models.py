from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django import forms

# Ticket is tied to an user: if a user is deleted, his tickets are deleted
class Ticket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=128, blank=False)
    description = models.CharField(max_length=8192, blank=False)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


# Review is tied to an user or a ticket: delete the review if no user or ticket
class Review(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)

    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[ {self.user} ] {self.ticket}'
