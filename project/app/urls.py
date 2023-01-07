from django.urls import path
from .views import FormAPIView

urlpatterns = [
    path('', FormAPIView.as_view()),
]
#{"name": "call","call_date": "date","phone_number": "phone"}
