from asyncio import exceptions
from django.shortcuts import render
from rest_framework import status
from user.utils import verify_token
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
import logging
from .serializers import CartSerializer,CartItemSerializer
from .models import Cart, CartItem

from user.utils import verify_token
logging.basicConfig(filename='book.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()


# Create your views here.
class CartViews(GenericAPIView):
    """
    Class to perform curd operation for the Cart
    """
    @verify_token
    def post(self,request):
        """
        method to perform the add operation to cart
        """
        serializer=CartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True,'message': " Book Added to cart Successfully",
                                'data': serializer.data}, status=status.HTTP_201_CREATED)
    @verify_token
    def get(self,request):
        """
        method to get the books inside the cartitem
        """
        try:
            print(request.data.get('user'))
            cart_list = Cart.objects.filter(user=request.data.get("user"))
            serializer = CartSerializer(cart_list, many=True)
            return Response({'success': True,
                             'message': " Book in the cartitem",
                             'data': serializer.data,
                             }, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False,
                             'message': "Something went Wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    @verify_token
    def delete(self,request):
        """
        method to get the books inside the cart
        """
        try:
            cart = Cart.objects.get(id=request.data.get("id"),user=request.data.get("user"))
            cart.delete()
            return Response({'success': True,
                             'message': "item in cart is successfully deleted"
                             }, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)


