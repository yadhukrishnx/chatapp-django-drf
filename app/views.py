from django.shortcuts import render,redirect
from rest_framework import status
from rest_framework.response import Response
from django.contrib import messages
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse
from django.contrib.auth import authenticate,logout,login
from dotenv import load_dotenv
from os import environ
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import UserSerializer
import google.generativeai as genai
from .models import Chat
# Create your views here.


load_dotenv()
try:
    geminikey = environ["geminikey"]
except KeyError:
    print("Error: 'TOKEN' not found in environment variables.")
    exit(1)

genai.configure(api_key="AIzaSyD8H1nRIKxy5LuAex9bw4BomxgRSlC3ii4")  # Replace with your actual API key
aimodel = genai.GenerativeModel('gemini-1.5-flash')

class UserRegistrationAPIView(APIView):
    permission_classes = [AllowAny]
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
            login(request,user)
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
        if user.tokens < 200:
            return Response({"error": "Not enough tokens."}, status=status.HTTP_400_BAD_REQUEST)
        user.tokens -= 100
        user.save()
        ai_response = gemini_response(message,user)
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

class TokenBalanceAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        token_balance = request.user.tokens
        return Response({
            "message": "Token balance retrieved successfully",
            "tokens_left": token_balance
        }, status=status.HTTP_200_OK)


class UserDetailsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "tokens": user.tokens
        })




def base(request):
    return render(request,'base.html')
def signup(request):
    return render(request,'auth/signup.html')
def userlogin(request):
    return render(request,'auth/login.html')
def user_logout(request):
    request.user.auth_token.delete()
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')

def token_balance(request):
    return render(request,'tokens.html')

@login_required
def chat(request):
    try:
        token = Token.objects.get(user=request.user).key
        return render(request, 'home/chat.html', {'token': token, 'user': request.user})
    except Token.DoesNotExist:
        return redirect('login')
    
def gemini_response(message,user):
    greetings = ['hello', 'hi', 'hey', 'hola', 'greetings', 'what\'s up', 'yo']
    if any(message.lower().startswith(greet) for greet in greetings):
        message = (f'Hi there {user.username}! How can I help you?')
        return message
    try:
        prompt = message
        response = aimodel.generate_content(prompt)
        generated_response = response.text.strip()
        return generated_response[:350]
    except Exception as e:
        print(f"Error generating response: {e}")
        
            
        
            