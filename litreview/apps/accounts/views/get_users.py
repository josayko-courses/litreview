from ..models import Review, Ticket, UserFollow


def get_users_viewable_reviews(user=None):
    if user:
        return Review.objects.filter(user=user.id)
    return Review.objects.all()


def get_users_viewable_tickets(user=None):
    if user:
        return Ticket.objects.filter(user=user.id)
    return Ticket.objects.all()


def get_users_subs(user):
    return UserFollow.objects.filter(user=user)


def get_users_followers(user):
    return UserFollow.objects.filter(followed_user=user)
