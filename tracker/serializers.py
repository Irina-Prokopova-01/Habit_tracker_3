from rest_framework.serializers import ModelSerializer

from users.serializers import UserSerializer

from .models import Habits
from .validators import HabitValidator


class HabitsSerializer(ModelSerializer):
    """Сериализатор привычки."""

    creator = UserSerializer(read_only=True)

    class Meta:
        model = Habits
        fields = "__all__"
        validators = [HabitValidator(field="__all__")]
