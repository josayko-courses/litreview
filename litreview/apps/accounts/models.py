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
        if self.review_id is None:
            return f'id: {self.id}, {self.title}, Review<{self.review_id}>'
        return f'id: {self.id}, {self.title}, Review<id: {self.review_id.id}, headline: {self.review_id.headline}>'


# Review is tied to an user or a ticket: delete the review if no user or ticket
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    ticket_id = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)

    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'id: {self.id}, headline: {self.headline}, Ticket<id: {self.ticket_id.id}, title: {self.ticket_id.title}>'


class UserFollow(models.Model):
    # Your UserFollow model definition goes here
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, related_name='user', on_delete=models.CASCADE)
    followed_user = models.ForeignKey(
        to=User, related_name="followed_user", on_delete=models.CASCADE
    )

    class Meta:
        # ensures we don't get multiple UserFollow instances
        # for unique user-user_followed pairs
        unique_together = (
            'user',
            'followed_user',
        )

    def __str__(self):
        return f'{self.user} => {self.followed_user}'
