from django.urls import path

from tracker.apps import TrackerConfig

from .views import (
    HabitsCreateApiView,
    HabitsDestroyApiView,
    HabitsPublicListApiView,
    HabitsRetrieveApiView,
    HabitsUpdateApiView,
    HabitsUsersListApiView,
)

app_name = TrackerConfig.name

urlpatterns = [
    path("habits/", HabitsPublicListApiView.as_view(), name="public_habits_list"),
    path("habits_users/", HabitsUsersListApiView.as_view(), name="users_habits_list"),
    path("habits/create/", HabitsCreateApiView.as_view(), name="habits_create"),
    path("habits/<int:pk>/", HabitsRetrieveApiView.as_view(), name="habits_retrieve"),
    path(
        "habits/<int:pk>/update/", HabitsUpdateApiView.as_view(), name="habits_update"
    ),
    path(
        "habits/<int:pk>/delete/", HabitsDestroyApiView.as_view(), name="habits_delete"
    ),
]
