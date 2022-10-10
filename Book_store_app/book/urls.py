from django.urls import path
from book import views

urlpatterns = [
    path('add/', views.BookAPIView.as_view(), name="add_book"),
    path('update/', views.BookAPIView.as_view(), name="update_book"),
    path('delete/', views.BookAPIView.as_view(), name="delete_book"),
    path('all_book/', views.GetAllBookListView.as_view(), name="all_book"),
]