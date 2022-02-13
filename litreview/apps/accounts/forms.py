from django.forms import ModelForm, Textarea, TextInput
from .models import Ticket, Review


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"
        exclude = ["user"]
        widgets = {
            'title': TextInput(attrs={'class': 'input'}),
            'description': Textarea(attrs={'class': 'textarea'}),
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ["user"]
        widgets = {
            'headline': TextInput(attrs={'class': 'input'}),
            'body': Textarea(attrs={'class': 'textarea'}),
        }
