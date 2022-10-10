from django.db import models
from user.models import User



class Book(models.Model):
    """
    model class for book model
    """
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
