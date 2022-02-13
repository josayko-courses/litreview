from ..models import Review, Ticket


def get_users_viewable_reviews(user=None):
    if user:
        return Review.objects.filter(user=user.id)
    return Review.objects.all()


def get_users_viewable_tickets(user=None):
    if user:
        return Ticket.objects.filter(user=user.id)
    return Ticket.objects.all()
