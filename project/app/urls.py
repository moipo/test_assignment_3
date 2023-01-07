from django.urls import path
from .views import FormAPIView

urlpatterns = [
    path('', FormAPIView.as_view()),
]
