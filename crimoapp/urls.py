from django.urls import path
from crimoapp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
