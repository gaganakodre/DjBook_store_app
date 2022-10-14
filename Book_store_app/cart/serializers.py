from logging import exception
from django.forms import model_to_dict
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
        
class CartItemBookSerializer(serializers.Serializer):

    quantity=serializers.IntegerField()
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    
    
    
class CartSerializer(serializers.ModelSerializer):
    """
    serializer class for creating all the cart
    """
    books=CartItemBookSerializer(many=True,write_only=True)
    cart_items=serializers.SerializerMethodField(read_only=True)

    def get_cart_items(self,obj):
        cartit=obj.cartitem_set.all()
        return CartItemSerializer(cartit,many=True).data



    class Meta:  
        model = Cart
        fields = ['id', 'total_price','total_quantity','is_ordered','user','books','cart_items']
        read_only_fields=['id', 'total_price','is_ordered','total_quantity']

    def create_cartitem(self,cart,books,user):
        """
        method to create the cartitem
        """
        cartitems=[]
        for book in books:
            quantity=book["quantity"]
            price=book["book"].price
            
            for index in range(book["quantity"]):
                cartitem=CartItem.objects.create(cart=cart,book=book["book"],user=user,
                                                    quantity= quantity,price=price)
                cart.total_quantity+= book["quantity"]
                cart.total_price+=book["book"].price*cart.total_quantity
                cart.save()
                cartitems.append(cart)

               

        return cartitems

    def create(self,validated_data:dict):
        """
        method to craete the cart
        """
        user,books=validated_data.values()
        cart,create=self.Meta.model.objects.get_or_create(user=user,is_ordered=False)
        cartitems=self.create_cartitem(cart=cart,books=validated_data["books"],user=user)
        return cart
        
       
        
       
        

    
        


