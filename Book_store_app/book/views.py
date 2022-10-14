from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
import logging
from user.utils import verify_token
from .models import Book
from book.serializers import BookSerializer, AllBookListSerializer


logging.basicConfig(filename='book.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()


class GetAllBookListView(GenericAPIView):
    """
    Class view for getting all the book
    """
    def get(self, request):
        """
        get function for requesting get method to get all the book
        """
        try:
            book_list = Book.objects.order_by('id')
            serializer = AllBookListSerializer(book_list, many=True)
            return Response({'success': True,
                             'message': "All Book",
                             'data': serializer.data,
                             }, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False,
                             'message': "Something went Wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class BookAPIView(GenericAPIView):
    """
    class view for Book api crud operation
    """
    

    @verify_token
    def post(self, request):
        """
        method to add the book from the admin
        """
        try:

            serializer = BookSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success': True,
                                'message': "New Book Added Successfully",
                                'data': serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @verify_token
    def put(self, request):
        """
        method to modify the book from the admin
        """
        try:
            book = Book.objects.get(id=request.data.get("id"))
            serializer = BookSerializer(instance=book, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response({'success': True,
                             'message': "Book is successfully updated",
                             'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @verify_token
    def delete(self, request):
        """
        method to delete the added book from the admin
        """
        try:
            book = Book.objects.get(id=request.data.get("id"))
            book.delete()
            return Response({'success': True,
                             'message': "Book is successfully deleted"
                             }, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'success': False,
                             'message': "Something went wrong",
                             'data': str(e)}, status=status.HTTP_400_BAD_REQUEST)


