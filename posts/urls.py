from django.urls import path
from .views import AllPageView

urlpatterns = [
    path('', AllPageView.as_view(), name='home'),
]