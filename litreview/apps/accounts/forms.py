from django.forms import ModelForm, Textarea, TextInput, RadioSelect, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ticket, Review, UserFollow


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude = ["user", "review_id"]
        widgets = {
            "title": TextInput(attrs={"class": "input"}),
            "description": Textarea(attrs={"class": "textarea"}),
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ["user", "ticket_id"]
        widgets = {
            "headline": TextInput(attrs={"class": "input"}),
            "body": Textarea(attrs={"class": "textarea"}),
            "rating": RadioSelect(
                choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]
            ),
        }


class UserFollowForm(ModelForm):
    class Meta:
        model = UserFollow
        exclude = ["user", "followed_user"]
        widgets = {
            "user_to_add": TextInput(
                attrs={
                    "class": "input",
                    "type": "text",
                    "placeholder": "Enter user name",
                }
            ),
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        widgets = {
            "username": TextInput(
                attrs={"class": "input", "type": "text", "placeholder": "Username"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["password1"].widget = PasswordInput(
            attrs={"class": "input", "type": "password", "placeholder": "Password"}
        )
        self.fields["password2"].widget = PasswordInput(
            attrs={
                "class": "input",
                "type": "password",
                "placeholder": "Password confirmation",
            }
        )
