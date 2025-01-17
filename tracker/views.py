from django.utils import timezone
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from users.permissions import IsCreator

from .models import Habits
from .pagination import PageSize
from .serializers import HabitsSerializer


class HabitsPublicListApiView(ListAPIView):
    """Контроллер списка всех публичных привычек."""

    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    pagination_class = PageSize

    def get_queryset(self):
        return Habits.objects.filter(is_public=True)


class HabitsUsersListApiView(ListAPIView):
    """Контроллер списка всех привычек пользователя."""

    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    pagination_class = PageSize

    def get_queryset(self):
        return Habits.objects.filter(creator=self.request.user)


class HabitsCreateApiView(CreateAPIView):
    """Контроллер создания привычки."""

    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer

    def perform_create(self, serializer):
        habit = serializer.save(
            creator=self.request.user, last_action_date=timezone.now().date()
        )
        habit.save()


class HabitsRetrieveApiView(RetrieveAPIView):
    """Контроллер просмотра привычки."""

    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer

    def get_permissions(self):
        self.permission_classes = (IsCreator,)
        return super().get_permissions()


class HabitsUpdateApiView(UpdateAPIView):
    """Контроллер изменения привычки."""

    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer

    def get_permissions(self):
        self.permission_classes = (IsCreator,)
        return super().get_permissions()


class HabitsDestroyApiView(DestroyAPIView):
    """Контроллер удаления привычки."""

    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer

    def get_permissions(self):
        self.permission_classes = (IsCreator,)
        return super().get_permissions()
