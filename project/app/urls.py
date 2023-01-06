from django.urls import path
from .views import *
from .api import FormAPIView

urlpatterns = [
    # path('', Main.main, name = 'main'),
    path('', FormAPIView.as_view()),
]
