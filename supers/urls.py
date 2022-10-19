from django.urls import path
from . import views

urlpatterns = [
    path('', views.hero_list),
    path('<int:pk>/', views.hero_details),
]