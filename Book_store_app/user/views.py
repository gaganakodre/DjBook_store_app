from rest_framework.reverse import reverse
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSerializer
from .jwt_service import JwtService
from .models import User
from book_store import settings




class UserRegistration(APIView):
    """
    class used to register for the user
    """

    def post(self, request):
        """
        this method is used to create the user for the registration
        """
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()  
            token = JwtService().encode({"user_id": serializer.data.get(
                "id"), "username": serializer.data.get("username")})
            send_mail(
                subject='Json Web Token For User Registration',
                message=settings.BASE_URL +
                reverse('verify_token', kwargs={"token": token}),
                from_email=None,
                recipient_list=[serializer.data.get('email')],
                fail_silently=False,
            )

            return Response({"message": "Registered successfully", "data": serializer.data},
                            status=status.HTTP_201_CREATED)  # serializer.data is used for de-serializer

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        

class UserLogin(APIView):
    """
    class is used for the user login
    """

    def post(self, request):
        """
        using the post method user can login by giving the credentials
        """
        
        try:
            user = authenticate(**request.data)
            print(user)
            
            if not user:
                raise Exception("User is Invalid")
            
            return Response({"message": f"{user.username} logged in successfully", "data": {"token": user.token}},
                            status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class VerifyToken(APIView):
    """
    this class to chek the user is logged in or not with correct token
    """
    def get(self, request, token):
        try:
            decoded_data = JwtService().decode(token)
            if "username" not in decoded_data:
                raise Exception("Invalid Token")
            user = User.objects.get(username=decoded_data.get("username"))
            user.is_verified = True
            user.save()
            return Response({"message": "User verified"})
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)