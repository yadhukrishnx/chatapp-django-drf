from . import views
from django.urls import path,include
from .views import UserRegistrationAPIView

urlpatterns = [
    path('api/register/',UserRegistrationAPIView.as_view(),name="user_register"),
    
    path('', views.base,name="base"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    
    path('chat/',views.chat,name="chat"),
]
