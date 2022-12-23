from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostAPIView.as_view(), name='posts'),
    path('posts/<str:pk>', views.PostAPIView.as_view(), name='posts')
]
