from django.contrib import admin

from .models import Habits


@admin.register(Habits)
class HabitsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "creator",
        "place_to_do",
        "time_to_do",
        "action_to_do",
        "is_pleasant",
        "related_habit",
        "periodicity",
        "reward",
        "duration",
        "is_public",
        "last_action_date",
    )
    search_fields = ["action_to_do", "time_to_do", "place_to_do"]
    list_filter = ["creator", "is_pleasant", "is_public"]
