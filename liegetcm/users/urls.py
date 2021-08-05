from django.urls import path
from users import views as userviews

urlpatterns = [
    path("register/<str:ut>/",userviews.register),
]