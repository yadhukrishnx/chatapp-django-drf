from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
# Create your views here.


class UserRegistrationAPIView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message" : "User Created Successfully",
                "user":{
                    "username":user.username,
                    "tokens":user.tokens
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

def base(request):
    return render(request,'base.html')

def signup(request):
    return render(request,'auth/signup.html')
def login(request):
    return render(request,'auth/login.html')

def chat(request):
    return render(request,'home/chat.html')