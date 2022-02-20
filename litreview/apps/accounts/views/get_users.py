from ..models import Review, Ticket, UserFollow


def get_users_subs(user):
    """Returns user's subscriptions to other users"""
    return UserFollow.objects.filter(user=user)


def get_users_followers(user):
    """Returns users that are following user"""
    return UserFollow.objects.filter(followed_user=user)


def get_users_viewable_reviews(user, feed=False):
    """Filter reviews posts a user can see"""
    if feed is False:
        # Posts page, show only user reviews
        return Review.objects.filter(user=user)
    else:
        # Show subs' reviews + own reviews
        subs = get_users_subs(user)
        followed_users = [x.followed_user for x in subs]
        followed_users.append(user)

        # Show other users review to tickets
        reviews = Review.objects.filter(user__in=followed_users)
        reviews_to_tickets = Review.objects.filter(ticket__user__in=followed_users)
        return reviews | reviews_to_tickets


def get_users_viewable_tickets(user, feed=False):
    """Filter tickets posts a user can see"""
    if feed is False:
        # Posts page, show only user tickets
        return Ticket.objects.filter(user=user)
    else:
        # Show subs' tickets + own tickets
        subs = get_users_subs(user)
        followed_users = [x.followed_user for x in subs]
        followed_users.append(user)
        return Ticket.objects.filter(user__in=followed_users)
