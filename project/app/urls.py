from django.urls import path
from .views import *
from .api import FormAPIView

urlpatterns = [
    path('', Main.main, name = 'main'),
    path('api/test', FormAPIView.as_view()),
]
