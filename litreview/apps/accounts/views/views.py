from django.shortcuts import redirect, render
from django.db.models import CharField, Value
from itertools import chain
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError


from litreview.apps.accounts.forms import (
    TicketForm,
    Ticket,
    ReviewForm,
    Review,
    UserFollowForm,
    UserFollow,
)

from .get_users import (
    get_users_viewable_reviews,
    get_users_viewable_tickets,
    get_users_subs,
    get_users_followers,
)

from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def feed(request):

    reviews = get_users_viewable_reviews(request.user, feed=True)
    # returns queryset of reviews
    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))

    tickets = get_users_viewable_tickets(request.user, feed=True)
    # returns queryset of tickets
    tickets = tickets.annotate(content_type=Value("TICKET", CharField()))

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets), key=lambda post: post.time_created, reverse=True
    )
    context = {"title": "Feed", "posts": posts}
    return render(request, "accounts/feed.html", context)


@login_required(login_url="login")
def posts(request):
    reviews = get_users_viewable_reviews(request.user)
    # returns queryset of reviews
    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))

    tickets = get_users_viewable_tickets(request.user)
    # returns queryset of tickets
    tickets = tickets.annotate(content_type=Value("TICKET", CharField()))

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets), key=lambda post: post.time_created, reverse=True
    )
    context = {"title": "Posts", "posts": posts}
    return render(request, "accounts/posts.html", context)


@login_required(login_url="login")
def subscriptions(request):
    form = UserFollowForm()
    if request.method == "POST":
        if "add" in request.POST:
            form = UserFollowForm(request.POST)
            if form.is_valid:
                sub = form.save(commit=False)
                sub.user = request.user
                try:
                    if sub.user_to_add != request.user.username:
                        sub.followed_user = User.objects.get(username=sub.user_to_add)
                        sub.save()
                except IntegrityError:
                    messages.warning(request, "Already suscribed to this user")
                except:
                    messages.error(request, "User does not exists")
                return redirect("subscriptions")
        else:
            id = request.POST.get("delete")
            UserFollow.objects.filter(id=id).delete()
            return redirect("subscriptions")

    subs = get_users_subs(request.user)
    followers = get_users_followers(request.user)

    context = {
        "title": "Subscriptions",
        "form": form,
        "subs": subs,
        "followers": followers,
    }
    return render(request, "accounts/subscriptions.html", context)


@login_required(login_url="login")
def createTicket(request):
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid:
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("feed")

    context = {"title": "New Ticket", "form": form}
    return render(request, "accounts/ticket_form.html", context)


@login_required(login_url="login")
def createReview(request, pk):
    ticket = None
    try:
        ticket = Ticket.objects.get(id=pk)
    except:
        ticket = None

    form1 = None
    if ticket is None:
        form1 = TicketForm()

    form2 = ReviewForm()
    if request.method == "POST":
        if form1:
            form1 = TicketForm(request.POST, request.FILES)
            if form1.is_valid:
                ticket = form1.save(commit=False)
                ticket.user = request.user
                ticket.save()

        form2 = ReviewForm(request.POST)
        if ticket and form2.is_valid:
            review = form2.save(commit=False)
            review.user = request.user
            review.ticket_id = ticket
            review.save()
            ticket.review_id = review
            ticket.save()
            return redirect("feed")

    context = {"title": "New Review", "form1": form1, "form2": form2, "post": ticket}
    return render(request, "accounts/review_form.html", context)


@login_required(login_url="login")
def updateTicket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    form = TicketForm(instance=ticket)

    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect("posts")

    context = {"title": "Update Ticket", "form": form, "update": True}
    return render(request, "accounts/ticket_form.html", context)


@login_required(login_url="login")
def updateReview(request, pk):
    review = Review.objects.get(id=pk)
    form = ReviewForm(instance=review)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("posts")

    context = {"title": "Update Review", "form2": form, "update": True}
    return render(request, "accounts/review_form.html", context)


@login_required(login_url="login")
def deleteTicket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    if request.method == "POST":
        ticket.delete()
        return redirect("posts")

    context = {"title": "Delete Review", "obj": ticket}
    return render(request, "accounts/delete.html", context)


@login_required(login_url="login")
def deleteReview(request, pk):
    ticket = Review.objects.get(id=pk)
    if request.method == "POST":
        ticket.delete()
        return redirect("posts")

    context = {"title": "Delete Review", "obj": ticket}
    return render(request, "accounts/delete.html", context)
