# views.py

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Product
from .serializers import ProductSerializer,  LoginSerializer,  UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer

class HomeView(APIView):
     
   permission_classes = (IsAuthenticated, )

   def get(self, request):
       
       content = {'message': 'Welcome to the JWT  Authentication page using React Js and Django!'}
       return Response(content)
   
class LogoutView(APIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):
          
          try:
               refresh_token = request.data["refresh_token"]
               token = RefreshToken(refresh_token)
               token.blacklist()
               return Response(status=status.HTTP_205_RESET_CONTENT)
          except Exception as e:
               return Response(status=status.HTTP_400_BAD_REQUEST)