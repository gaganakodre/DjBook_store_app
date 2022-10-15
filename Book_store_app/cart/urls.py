from django.urls import path
from cart import views

urlpatterns = [
    path('add/', views.CartViews.as_view(), name="add_book_to_cart"),
    path('get/',views.CartViews.as_view(),name="get_books_from_cart"),
    path('delete/', views.CartViews.as_view(), name="delete_cart"),
    # path('adding/',views.RawQueriesCart.as_view(),name="add")
    path('checkout/',views.CheckoutApi.as_view(),name="checkout_api")
    
    
    
]