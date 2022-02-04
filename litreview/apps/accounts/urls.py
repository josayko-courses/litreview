from django.urls import path

from .views import views

urlpatterns = [
    path("", views.feed, name="feed"),
    path("create-ticket", views.createTicket, name="create-ticket"),
    path("delete-ticket/<str:pk>", views.deleteTicket, name="delete-ticket"),
    path("create-review", views.createReview, name="create-review"),
    path("delete-review/<str:pk>", views.deleteReview, name="delete-review"),
]
