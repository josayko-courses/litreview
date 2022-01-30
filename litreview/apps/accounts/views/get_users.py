from ..models import Review, Ticket


def get_users_viewable_reviews(user):
    return Review.objects.all()


def get_users_viewable_tickets(user):
    return Ticket.objects.all()
