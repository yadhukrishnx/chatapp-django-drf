from . import views
from django.urls import path,include
from .views import UserRegistrationAPIView,UserLoginAPIView,ChatAPIView,UserDetailsAPIView,TokenBalanceAPIView

urlpatterns = [
    path('api/register/',UserRegistrationAPIView.as_view(),name="user_register"),
    path('api/login/', UserLoginAPIView.as_view(), name='user-login'),
    path('api/chat/', ChatAPIView.as_view(), name='chat-api'),
    path('api/token-balance/', TokenBalanceAPIView.as_view(), name='token-balance'),
    path('api/user-details/', UserDetailsAPIView.as_view(), name='user-details'),
    
    
    path('', views.base,name="base"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.userlogin,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('chat/',views.chat,name="chat"),
    path('doc/',views.doc,name="doc"),
    path('tokenbalance',views.token_balance,name="tokenbalance"),
]
