import pytest
from django.urls import reverse

pytest_mark = pytest.mark.django_db
REGISTER_URL = reverse('register')

@pytest.fixture
def user_data():
    return {'username': 'gagana',
            'first_name': 'gaga', 'last_name': 'na',
            'email': 'gagana@gmail.com',
            'password': 'gagana',
            'location':'ban',
            'phone_number':'123'}

class TestUserLoginAndRegister:
    @pytest.mark.django_db
    def test_user_registration_successfully(self, client, django_user_model, user_data):
        response = client.post(REGISTER_URL, user_data, content_type="application/json")
        assert response.status_code == 200

