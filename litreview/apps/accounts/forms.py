from django.forms import ModelForm, Textarea, TextInput
from .models import Ticket, Review, UserFollow


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
    class Meta:
        model = UserFollow
        fields = "__all__"
        exclude = ["user"]
        widgets = {
            'followed_user': TextInput(attrs={'class': 'input'}),
        }
