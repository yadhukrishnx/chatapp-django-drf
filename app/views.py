from django.shortcuts import render,redirect
from rest_framework import status
from rest_framework.response import Response
from django.contrib import messages
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse
from django.contrib.auth import authenticate,logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import UserSerializer
from urllib.parse import unquote
from .models import Chat
# Create your views here.


class UserRegistrationAPIView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message" : "User Created Successfully ",
                "user":{
                    "username":user.username,
                    "tokens":user.tokens
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self,request,*args,**kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            token,created = Token.objects.get_or_create(user=user)
            chat_url = request.build_absolute_uri(reverse('chat'))
            return Response({
                "message" : "Login Successfull",
                "token" : token.key,
                "chat_url": chat_url,
            },status=status.HTTP_200_OK)
        else:
            return Response({"error":"Invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)



class ChatAPIView(APIView):
    permission_classes = [IsAuthenticated] 
    def post(self, request, *args, **kwargs):
        user = request.user
        message = request.data.get("message")
        if not message:
            return Response({"error": "Message is required."}, status=status.HTTP_400_BAD_REQUEST)
        if user.tokens < 100:
            return Response({"error": "Not enough tokens."}, status=status.HTTP_400_BAD_REQUEST)
        user.tokens -= 100
        user.save()
        ai_response = "This is a dummy AI response to your question."
        chat = Chat.objects.create(
            user=user,
            message=message,
            response=ai_response
        )
        return Response({
            "message": "Question asked successfully.",
            "response": ai_response,
            "tokens_left": user.tokens,
        }, status=status.HTTP_200_OK)



def base(request):
    return render(request,'base.html')
def signup(request):
    return render(request,'auth/signup.html')
def login(request):
    return render(request,'auth/login.html')
def user_logout(request):
    request.user.auth_token.delete()
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')


def chat(request):
    if request.user.is_authenticated:
        token = Token.objects.get(user=request.user).key
        return render(request, 'home/chat.html', {'token': token,'user':request.user})
    else:
        return redirect('login')