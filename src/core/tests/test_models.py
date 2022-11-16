import pytest

from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_create_user_with_email_successful():
    """Test creating a new user with an email is successfull"""
    email = 'test@test.com'
    password = "Test-pass123"
    user = get_user_model().objects.create_user(
        email=email,
        password=password
    )
    assert user.email == email
    assert user.check_password(password)


@pytest.mark.django_db
def test_new_user_email_normalized():
    """Test the email for new user is normalized"""
    email = 'test@TEST.COM'
    user = get_user_model().objects.create_user(
        email=email,
        password="Test-pass123"
    )
    assert user.email == email.lower()


@pytest.mark.django_db
def test_new_user_invalid_email():
    """Test creating user with no email raises error"""
    email = None
    with pytest.raises(ValueError):
        get_user_model().objects.create_user(
            email=email,
            password="Test-pass123"
        )
