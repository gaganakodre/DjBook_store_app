from email import header
import pytest
import json
from django.urls import reverse

@pytest.fixture
def get_token_header(django_user_model, client):
    user=django_user_model.objects.create_user(username='gagana1', first_name="gaga", last_name="na",
                                                 email='gagana@gmail.com',
                                                 password='1234',location='bng',phone_number=1233,is_verified=True,is_superuser=True)
    user.save()
    # login user
    url = reverse('login')
    data = {'username': 'gagana1', 'password': '1234'}
    response = client.post(url, data, content_type="application/json")
    
    json_data = json.loads(response.content)
    token = json_data['data']['token']
    header = {'HTTP_TOKEN': token, "content_type": "application/json"}
    return user, header
    


@pytest.fixture
def book_details(get_token_header):
    user, header = get_token_header
    return {
        "title":"title2",
        "author":"author2",
        "price":111,
        "quantity":2,
        "user":user.id }
@pytest.fixture
def book_details_error(get_token_header):
    user, header = get_token_header
    return {
        "titl":"title2",
        "author":"author2",
        "price":111,
        "quantity":2,
        "user":user.id }

@pytest.fixture
def book_update_data(client, get_token_header,book_details):
    user,header=get_token_header
    url = reverse('add_book')
    response = client.post(url, book_details, **header)
    json_data = json.loads(response.content)
    book_id = json_data['data']['id']
    return{'id': book_id,
             "title":"title22",
                "author":"author2",
                "price":111,
                "quantity":2}
@pytest.fixture
def book_update_data_error(client, get_token_header,book_details):
    user,header=get_token_header
    url = reverse('add_book')
    response = client.post(url, book_details, **header)
    json_data = json.loads(response.content)
    book_id = json_data['data']['id']
    return{'id': "book",
             "title":"title22",
                "author":"author2",
                "price":111,
                "quantity":2}
@pytest.fixture
def book_delete_data(client, get_token_header,book_details):
    user,header=get_token_header
    url = reverse('add_book')
    response = client.post(url, book_details, **header)
    json_data = json.loads(response.content)
    book_id = json_data['data']['id']
    url = reverse('delete_book')
    data = {'id': book_id}
    return data

class TestBooksAPI:
    
    @pytest.mark.django_db
    def test_response_as_create_book_successfully(self, client, get_token_header,book_details):
        # Create user
        user, header = get_token_header
        # Create books
        url = reverse('add_book')
        response = client.post(url, book_details, **header)
        json_data = json.loads(response.content)
        assert response.status_code == 201
        assert json_data['data']['title'] == 'title2'

    @pytest.mark.django_db
    def test_response_as_create_book_unsuccessfully(self, client, get_token_header,book_details_error):
        # Create user
        user, header = get_token_header
        # Create books
        url = reverse('add_book')
        response = client.post(url, book_details_error, **header)
        json_data = json.loads(response.content)
        assert response.status_code == 400
        


    @pytest.mark.django_db
    def test_response_as_validation_error_while_create_books(self, client, get_token_header,book_details):
        user, header = get_token_header
        # Create books
        url = reverse('add_book')
        response = client.post(url, book_details, **header)
        assert response.status_code == 201
        # Get books
        user_data = {'user_id': user.id}
        url = reverse('all_book')
        response = client.get(url, user_data, **header)
        assert response.status_code == 200
        
        

    @pytest.mark.django_db
    def test_response_as_update_books_successfully(self, client, get_token_header,book_update_data):
        user, header = get_token_header
        # Update books
        url = reverse('update_book')
        response = client.put(url, book_update_data, **header)
        json_data = json.loads(response.content)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_response_as_update_books_unsuccessfully(self, client, get_token_header,book_update_data_error):
        user, header = get_token_header
        # create book 
        url = reverse('update_book')
        response = client.put(url, book_update_data_error, **header)
        json_data = json.loads(response.content)
        assert response.status_code == 400

    

    @pytest.mark.django_db
    def test_response_as_delete_books_successfully(self, client, get_token_header,book_delete_data):
        user, header = get_token_header
        url = reverse('delete_book')
        response = client.delete(url, book_delete_data, **header)
        assert response.status_code == 200

    



