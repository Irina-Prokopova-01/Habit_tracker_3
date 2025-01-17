from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from tracker.models import Habits
from users.models import User


class HabitsTestCase(APITestCase):
    def setUp(self):
        """Подготовка исходных данных для тестирования."""
        self.user = User.objects.create(email="test@test.com")
        self.test_habit = Habits.objects.create(
            creater=self.user,
            place_to_do="Test",
            action_to_do="Test",
            is_pleasant=True,
            periodicity=100,
            duration=5,
            is_public=True,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        """Тестирование получения информации о привычке."""
        url = reverse("tracker:habits_retrieve", args=(self.test_habit.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json().get("action_to_do")
        self.assertEqual(result, self.test_habit.action_to_do)

    def test_habit_create(self):
        """Тестирование создания новой привычки."""
        url = reverse("tracker:habits_create")
        data = {
            "place_to_do": "Test",
            "action_to_do": "Test",
            "is_pleasant": False,
            "periodicity": 5,
            "duration": 100,
            "is_public": True,
            "related_habit": self.test_habit.id,
            "reward": "",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habits.objects.all().count(), 2)

    def test_habit_update(self):
        """Тестирование изменения привычки."""
        url = reverse("tracker:habits_update", args=(self.test_habit.id,))
        data = {
            "place_to_do": "Test_new",
            "action_to_do": "Test_new",
            "is_pleasant": True,
            "periodicity": 2,
            "duration": 100,
            "is_public": True,
            "related_habit": "",
            "reward": "",
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json().get("place_to_do")
        self.assertEqual(result, data.get("place_to_do"))

    def test_habit_delete(self):
        """Тестирование удаления привычки."""
        url = reverse("tracker:habits_delete", args=(self.test_habit.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habits.objects.all().count(), 0)

    def test_habit_list_public(self):
        """Тестирование получения списка публичных привычек."""
        url = reverse("tracker:public_habits_list")
        response = self.client.get(url)

        # готовим данные для сравнения - id привычки, признак публичности привычки и id создателя привычки
        result = {
            "id": self.test_habit.id,
            "is_public": self.test_habit.is_public,
            "creator": self.user.id,
        }

        # выбираем из response данные для сравнения - d привычки, признак публичности привычки и id создателя привычки
        habit_id = response.json().get("results")[0].get("id")
        creator_id = response.json().get("results")[0].get("creator").get("id")
        is_public = response.json().get("results")[0].get("is_public")
        result_to_assert = {
            "id": habit_id,
            "is_public": is_public,
            "creator": creator_id,
        }

        # сравнение кодов ответа с ожидаемыми данными и подготовленных данных с выбранными
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result_to_assert, result)

    def test_habit_list_users(self):
        """Тестирование получения списка пользовательских привычек."""
        url = reverse("tracker:users_habits_list")
        response = self.client.get(url)

        # готовим данные для сравнения - id привычки, действие привычки и id создателя привычки
        result = {
            "id": self.test_habit.id,
            "action_to_do": self.test_habit.action_to_do,
            "creater": self.user.id,
        }

        # выбираем из response данные для сравнения - id привычки, действие привычки и id создателя привычки
        habit_id = response.json().get("results")[0].get("id")
        action_to_do = response.json().get("results")[0].get("action_to_do")
        creator_id = response.json().get("results")[0].get("creator").get("id")
        result_to_assert = {
            "id": habit_id,
            "action_to_do": action_to_do,
            "creator": creator_id,
        }

        # сравнение кодов ответа с ожидаемыми данными и подготовленных данных с выбранными
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result_to_assert, result)

    def test_habit_create_wrong_duration(self):
        """Тестирование получения сообщения о неверной длительности при создании привычки."""
        url = reverse("tracker:habits_create")
        data = {
            "place_to_do": "Test",
            "action_to_do": "Test",
            "is_pleasant": False,
            "periodicity": 5,
            "duration": 1000,
            "is_public": True,
            "related_habit": self.test_habit.id,
            "reward": "",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"),
            ["Время выполнения привычки не может превышать 120 секунд."],
        )

    def test_habit_create_wrong_periodicity(self):
        """Тестирование получения сообщения о неверной периодичности при создании привычки."""
        url = reverse("tracker:habits_create")
        data = {
            "place_to_do": "Test",
            "action_to_do": "Test",
            "is_pleasant": False,
            "periodicity": 10,
            "duration": 100,
            "is_public": True,
            "related_habit": self.test_habit.id,
            "reward": "",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"),
            ["Периодичность выполнения привычки не может быть реже раза в неделю."],
        )

    def test_habit_create_reward_related_habit(self):
        """Тестирование получения сообщения об одновременно выборе награды
        и связанной привычки при создании привычки."""
        url = reverse("tracker:habits_create")
        data = {
            "place_to_do": "Test",
            "action_to_do": "Test",
            "is_pleasant": False,
            "periodicity": 2,
            "duration": 100,
            "is_public": True,
            "related_habit": self.test_habit.id,
            "reward": "Test",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"),
            ["Нельзя выбирать связанную привычку и вознаграждение одновременно."],
        )

    def test_habit_create_reward_for_pleasant_habit(self):
        """Тестирование получения сообщения о неверном выборе награды
        и связанной привычки при создании приятной привычки."""
        url = reverse("tracker:habits_create")
        data = {
            "place_to_do": "Test",
            "action_to_do": "Test",
            "is_pleasant": True,
            "periodicity": 2,
            "duration": 100,
            "is_public": True,
            "related_habit": "",
            "reward": "Test",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"),
            [
                "Нельзя выбирать связанную привычку или вознаграждение для приятной привычки."
            ],
        )
