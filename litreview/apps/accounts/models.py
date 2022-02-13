from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

# Ticket is tied to an user: if a user is deleted, his tickets are deleted
class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    review_id = models.ForeignKey(
        'Review', on_delete=models.SET_NULL, blank=True, null=True
    )
    title = models.CharField(max_length=128, blank=False)
    description = models.CharField(max_length=8192, blank=False)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'id: {self.id}, title: {self.title}, review_id: {self.review_id}'


# Review is tied to an user or a ticket: delete the review if no user or ticket
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    ticket_id = models.OneToOneField(to=Ticket, on_delete=models.CASCADE)

    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'id: {self.id}, title: {self.ticket_id.title}, ticket_id: {self.ticket_id.id}'


class UserFollows(models.Model):
    # Your UserFollows model definition goes here
    user = models.ForeignKey(to=User, related_name='user', on_delete=models.CASCADE)
    followed_user = models.ForeignKey(
        to=User, related_name="followed_user", on_delete=models.CASCADE
    )

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = (
            'user',
            'followed_user',
        )
