from django.shortcuts import render
from django.db.models import CharField, Value
from itertools import chain
from .get_users import get_users_viewable_reviews, get_users_viewable_tickets


def feed(request):

    reviews = get_users_viewable_reviews(request.user)
    # returns queryset of reviews
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    tickets = get_users_viewable_tickets(request.user)
    # returns queryset of tickets
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets), key=lambda post: post.time_created, reverse=True
    )
    context = {"title": "Feed", "posts": posts}
    return render(request, "accounts/feed.html", context)
