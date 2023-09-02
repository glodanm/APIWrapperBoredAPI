from django.urls import path
from .views import GetActivityAPI, ActivityList

app_name = 'wrapper'

urlpatterns = [
    path('get_activity/', GetActivityAPI.as_view()),
    path('activities/', ActivityList.as_view()),
]
