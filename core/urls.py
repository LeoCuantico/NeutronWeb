from django.urls import path
from core import views as core_views
from arte import views as arte_views


urlpatterns = [
    path('', core_views.home, name="home"),
    path('diseños/',arte_views.arte, name="diseños"),
    path('about-me/', core_views.about, name="about"),
]