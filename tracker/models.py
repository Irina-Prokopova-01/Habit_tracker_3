from django.db import models

from users.models import User


class Habits(models.Model):
    """Модель привычки."""

    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Создатель привычки",
        help_text="Введите создателя привычки",
    )
    place_to_do = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Место выполнения привычки",
        help_text="Введите место выполнения привычки",
    )
    time_to_do = models.TimeField(
        null=True,
        blank=True,
        verbose_name="Время выполнения привычки",
        help_text="Введите время выполнения привычки",
    )
    action_to_do = models.TextField(
        verbose_name="Действие привычки",
        blank=True,
        null=True,
        help_text="Введите действие привычки",
    )
    is_pleasant = models.BooleanField(
        verbose_name="Признак приятной привычки",
        default=False,
        help_text="Установите признак приятной привычки",
    )
    related_habit = models.ForeignKey(
        "self",
        verbose_name="Связанная привычка",
        help_text="Укажите связанную привычку",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    periodicity = models.IntegerField(
        verbose_name="Периодичность выполнения привычки в днях",
        help_text="Введите периодичность выполнения привычки",
        default=1,
    )
    reward = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Награда за выполнение привычки",
        help_text="Введите награду за выполнение привычки",
    )
    duration = models.IntegerField(
        verbose_name="Длительность выполнения привычки в секундах",
        help_text="Введите длительность выполнения привычки",
        default=120,
    )
    is_public = models.BooleanField(
        verbose_name="Признак публичности",
        default=False,
        help_text="Введите признак публичности",
    )
    last_action_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего выполнения привычки",
        help_text="Введите дату последнего выполнения привычки",
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"Я буду {self.action_to_do} в {self.time_to_do} в {self.place_to_do}"
