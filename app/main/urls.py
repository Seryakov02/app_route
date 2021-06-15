from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name="home"),
    path('buses/', views.get_buses, name="buses"),
    path('shedule/<slug:slug>/', views.get_shedule, name="shedule"),
    path('suburban/', views.get_suburban, name="suburban"),
    path('map/', views.get_map, name="map")
]
