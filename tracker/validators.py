from rest_framework import serializers


class HabitValidator:
    """Валидатор привычек."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value["duration"] > 120:
            raise serializers.ValidationError(
                "Время выполнения привычки не может превышать 120 секунд."
            )

        if value["periodicity"] > 7:
            raise serializers.ValidationError(
                "Периодичность выполнения привычки не может быть реже раза в неделю."
            )

        if value["related_habit"] and value["reward"]:
            raise serializers.ValidationError(
                "Нельзя выбирать связанную привычку и вознаграждение одновременно."
            )

        if value["is_pleasant"]:
            if value["reward"] or value["related_habit"]:
                raise serializers.ValidationError(
                    "Нельзя выбирать связанную привычку или вознаграждение для приятной привычки."
                )

        if value["related_habit"]:
            if not value["related_habit"].is_pleasant:
                raise serializers.ValidationError(
                    "В связанные привычки можно выбрать только привычки с признаком приятной привычки."
                )