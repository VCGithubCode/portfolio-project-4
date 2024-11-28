from django.urls import path
from .views import Index
from activities.views import activities


urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('activities/', activities.as_view(), name='activities'),
]