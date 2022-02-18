from django.forms import ModelForm, Textarea, TextInput
from .models import Ticket, Review, UserFollow
from django.db import models
from django import forms


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude = ["user", "review_id"]
        widgets = {
            'title': TextInput(attrs={'class': 'input'}),
            'description': Textarea(attrs={'class': 'textarea'}),
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ["user", "ticket_id"]
        widgets = {
            'headline': TextInput(attrs={'class': 'input'}),
            'body': Textarea(attrs={'class': 'textarea'}),
        }


class UserFollowForm(ModelForm):
    followed_user = models.CharField(max_length=128)

    class Meta:
        model = UserFollow
        exclude = ["user"]
        widgets = {
            'followed_user': TextInput(
                attrs={
                    'class': 'input',
                    'type': 'text',
                    'placeholder': 'Enter user name',
                }
            ),
        }
