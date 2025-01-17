import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habits",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "place_to_do",
                    models.CharField(
                        blank=True,
                        help_text="Введите место выполнения привычки",
                        max_length=255,
                        null=True,
                        verbose_name="Место выполнения привычки",
                    ),
                ),
                (
                    "time_to_do",
                    models.TimeField(
                        blank=True,
                        help_text="Введите время выполнения привычки",
                        null=True,
                        verbose_name="Время выполнения привычки",
                    ),
                ),
                (
                    "action_to_do",
                    models.TextField(
                        blank=True,
                        help_text="Введите действие привычки",
                        null=True,
                        verbose_name="Действие привычки",
                    ),
                ),
                (
                    "is_pleasant",
                    models.BooleanField(
                        default=False,
                        help_text="Установите признак приятной привычки",
                        verbose_name="Признак приятной привычки",
                    ),
                ),
                (
                    "periodicity",
                    models.IntegerField(
                        default=1,
                        help_text="Введите периодичность выполнения привычки",
                        verbose_name="Периодичность выполнения привычки в днях",
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        help_text="Введите награду за выполнение привычки",
                        max_length=255,
                        null=True,
                        verbose_name="Награда за выполнение привычки",
                    ),
                ),
                (
                    "duration",
                    models.IntegerField(
                        default=120,
                        help_text="Введите длительность выполнения привычки",
                        verbose_name="Длительность выполнения привычки в секундах",
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=False,
                        help_text="Введите признак публичности",
                        verbose_name="Признак публичности",
                    ),
                ),
                (
                    "last_action_date",
                    models.DateField(
                        blank=True,
                        help_text="Введите дату последнего выполнения привычки",
                        null=True,
                        verbose_name="Дата последнего выполнения привычки",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        help_text="Введите создателя привычки",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Создатель привычки",
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите связанную привычку",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="tracker.habits",
                        verbose_name="Связанная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]
