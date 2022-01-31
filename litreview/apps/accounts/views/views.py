from django.shortcuts import redirect, render
from django.db.models import CharField, Value
from itertools import chain

from litreview.apps.accounts.forms import TicketForm, Ticket
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


def createTicket(request):
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("feed")

    context = {"form": form}
    return render(request, "accounts/ticket_form.html", context)


def deleteTicket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    if request.method == "POST":
        ticket.delete()
        return redirect("feed")

    context = {"obj": ticket}
    return render(request, "accounts/delete.html", context)
