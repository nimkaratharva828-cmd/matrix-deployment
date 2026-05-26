from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page of the news section
    path('<str:category>/', views.category, name='category'),  # Category pages like /news/business
]
