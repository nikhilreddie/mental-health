from django.urls import path
from .views import home, login, validate_login, register, edituser, updateuser, assistant, video_feed, healthreference, nearbydoctors, index, history,get_session_data, showAsstiant
from  django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name="index"),
    path('index/', index, name="index"),
    path('login/', login, name="login"),
    path('validate_login', validate_login, name="validate_login"),
    path('register', register, name="register"),
    path('home', home, name="home"),
    path('edituser/<int:id>', edituser, name="edituser"),
    path('updateuser', updateuser, name="updateuser"),
    path('logout/', index, name="logout"),
    path('assistant', assistant, name="assistant"),
    path('video_feed/', video_feed, name='video_feed'),
    path('healthreference/', healthreference, name='healthreference'),
    path('nearbydoctors/', nearbydoctors, name='nearbydoctors'),
    path('history/', history, name='history'),
    path('showAsstiant/<str:emotion_detected>/', showAsstiant, name='showAsstiant'),
    path('get_session_data/', get_session_data, name='get_session_data')
]
