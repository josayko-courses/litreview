from django.urls import path

from .views import views

urlpatterns = [
    path("", views.feed, name="feed"),
]
