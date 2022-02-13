from django.urls import path

from .views import views
from .views import authentication

urlpatterns = [
    path("login/", authentication.loginPage, name="login"),
    path("logout/", authentication.logoutUser, name="logout"),
    path("register/", authentication.registerPage, name="register"),
    path("", views.feed, name="feed"),
    path("posts/", views.posts, name="posts"),
    path("subscriptions/", views.subscriptions, name="subscriptions"),
    path("create-ticket", views.createTicket, name="create-ticket"),
    path("update-ticket/<str:pk>", views.updateTicket, name="update-ticket"),
    path("delete-ticket/<str:pk>", views.deleteTicket, name="delete-ticket"),
    path("create-review", views.createReview, name="create-review"),
    path("update-review/<str:pk>", views.updateReview, name="update-review"),
    path("delete-review/<str:pk>", views.deleteReview, name="delete-review"),
]
