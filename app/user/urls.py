"""
URL mappings for the user API.
"""
from django.urls import path

from user import views

# 逆引きで使う用
app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token')
]