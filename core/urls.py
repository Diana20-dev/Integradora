from django.urls import path
from .views import HomePageView, EmpleoPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('empleo/', EmpleoPageView.as_view(), name="empleo"),
]