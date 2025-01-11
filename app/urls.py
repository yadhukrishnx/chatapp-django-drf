from . import views
from django.urls import path,include
from .views import UserRegistrationAPIView,UserLoginAPIView

urlpatterns = [
    path('api/register/',UserRegistrationAPIView.as_view(),name="user_register"),
    path('api/login/', UserLoginAPIView.as_view(), name='user-login'),
   
    
    path('', views.base,name="base"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('chat/',views.chat,name="chat"),
]
