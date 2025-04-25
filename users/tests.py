from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    def setUp(self):
        """Подготовка исходных данных для тестирования."""
        self.user = User.objects.create(
            email="test@test.com",
            first_name="Test",
            last_name="Test",
            phone_number="+79139397935",
            is_active=True,
            is_superuser=True,
        )
        self.client.force_authenticate(user=self.user)

    def test_user_retrieve(self):
        """Тестирование получения информации о пользователе."""
        url = reverse("users:user_retrieve", args=(self.user.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json().get("email")
        self.assertEqual(result, self.user.email)

    def test_user_update(self):
        """Тестирование изменения информации о пользователе."""
        url = reverse("users:user_update", args=(self.user.id,))
        data = {"first_name": "New_test"}
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json().get("first_name")
        self.assertEqual(result, data.get("first_name"))

    def test_user_create(self):
        """Тестирование создания нового пользователя."""
        url = reverse("users:user_register")
        data = {
            "email": "new_test@test.com",
            "password": "12345",
            "first_name": "New_Test",
            "last_name": "New_Test",
            "phone_number": "+79139397935",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)

    def test_user_delete(self):
        """Тестирование удаления пользователя."""
        url = reverse("users:user_delete", args=(self.user.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.all().count(), 0)

    def test_user_list(self):
        """Тестирование получения списка всех пользователей."""
        url = reverse("users:user_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
