from django.forms import ModelForm, Textarea
from .models import Ticket


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
