from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.hotels_view, name='hotels'),
    # path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('<int:pk>/<str:dt>/', views.hotel_details, name='hotel_details'),


]
