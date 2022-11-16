import pytest

from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.urls import reverse


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def user():
    user = get_user_model().objects.create_user(
        email="test@example.com",
        password="Test-pass321",
        name='Test Name',
    )
    return user


@pytest.fixture
def admin_user():
    admin_user = get_user_model().objects.create_superuser(
        email="admin@example.com",
        password="Test-pass123",
    )
    return admin_user


@pytest.mark.django_db
def test_users_listed(client, admin_user, user):
    """test that users are listed on user page"""
    client.force_login(admin_user)
    url = reverse("admin:core_user_changelist")
    response = client.get(url)

    assert user.name in response.content.decode('utf-8')
    assert user.email in response.content.decode('utf-8')


@pytest.mark.django_db
def test_users_change_page(client, admin_user, user):
    """test that the user edit page works"""
    client.force_login(admin_user)
    url = reverse("admin:core_user_change", args=[user.id])
    response = client.get(url)

    assert response.status_code == 200
