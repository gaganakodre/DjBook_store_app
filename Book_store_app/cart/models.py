
from django.db import models
from book.models import Book
from user.models import User



# Create your models here.

class CartItem(models.Model):
    """
    model class to create the cartitem
    """
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()
    cart=models.ForeignKey("api.Cart",on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    


    def __str__(self):
        return str(self.price)

    def total_price(self):
        return self.book.price*self.quantity



class Cart(models.Model):
    """
    model class for cart model
    """
    total_price=models.DecimalField(max_digits=10, decimal_places=2)
    is_ordered=models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_items=models.ManyToManyField(CartItem)
    def __str__(self):
        return self.total_price

