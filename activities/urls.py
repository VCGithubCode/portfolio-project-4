from django.urls import path
from .views import activities


urlpatterns = [
    path('activities/', activities.as_view(), name='activities'),
]