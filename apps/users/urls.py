from django.urls import path
from .views import (
    UserListView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
    GroupListView,
    GroupCreateView,
    GroupUpdateView,
    GroupDeleteView,
)

urlpatterns = [
    path("", UserListView.as_view(), name="user_list"),
    path("users/add/", UserCreateView.as_view(), name="user_create"),
    path("users/<int:pk>/edit/", UserUpdateView.as_view(), name="user_edit"),
    path("users/<int:pk>/delete/", UserDeleteView.as_view(), name="user_delete"),
    path("groups/", GroupListView.as_view(), name="group_list"),
    path("groups/add/", GroupCreateView.as_view(), name="group_create"),
    path("groups/<int:pk>/edit/", GroupUpdateView.as_view(), name="group_edit"),
    path("groups/<int:pk>/delete/", GroupDeleteView.as_view(), name="group_delete"),
]
