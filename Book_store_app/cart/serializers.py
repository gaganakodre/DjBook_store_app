from logging import exception
from rest_framework import serializers
from book.models import Book
from .models import Cart, CartItem
from user.models import User


class CartItemSerializer(serializers.ModelSerializer):
    """
    serilaizers to create the cartItem Model
    """
    
    class Meta:
        model=CartItem
        fields=['id','price','quantity','user','cart','book']
        required_field = ['price','quantity','user','cart']
    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)
        

class CartSerializer(serializers.ModelSerializer):
    """
    serializer class for creating all the cart
    """
    cart_items=CartItemSerializer(many=True,read_only=True)
    books = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:  
        model = Cart
        fields = ['id', 'total_price','is_ordered','user','books','cart_items']
        required_field = ['total_price','is_ordered','user']

        def create_cart_items(cart,book,user):
            cartitems=[]
            books=CartItemSerializer.books
            print(books)
            for book in books:
                cart,create=CartItem.objects.get_or_create(cart=cart,book=book["book"],user=user)
                if not create:
                    raise exception("insuffiuent data")
                cart.quantity += book["quantity"]
                cart.save()
                cartitems.append(cart)
            return cartitems

        def create(self,validated_data:dict):
            user=self.context["user"]
            cart,create=Cart.objects.get_or_create(user=user)
            cartitems=self.create_cart_items(book=validated_data["books"],cart=cart,user=user)
            cart.cart.add(*cartitems)
            print(cart)
            return cart

    
        


