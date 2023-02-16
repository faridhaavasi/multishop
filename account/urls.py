from django.urls import path
from . import views
app_name = 'account'
urlpatterns = [
    path('login', views.LoginUser.as_view(), name='login'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('checkotp', views.CheckOtp.as_view(), name='checkotp'),
    path('registerfinal', views.RegisterFinal.as_view(), name='registerfinal'),
    path('logout', views.user_logout, name='logout'),
    path('editprofile/<int:pk>', views.Edit_profile.as_view(), name='editprofile'),
]