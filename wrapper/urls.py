from django.urls import path
from .views import ActivityAPI

app_name = 'wrapper'

urlpatterns = [
    path('activity/', ActivityAPI.as_view()),
]
