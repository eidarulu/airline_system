from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('flight/<int:flight_id>/', views.flight_detail, name='flight_detail'),
    path('flight/<int:flight_id>/book/', views.book_flight, name='book_flight'),
    path('manage-booking/', views.manage_booking, name='manage_booking'),
    path('airport/<str:airport_code>/', views.airport_detail, name='airport_detail'),
]