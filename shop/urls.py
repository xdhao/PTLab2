from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buy/', views.PurchaseCreate.as_view(), name='buy'),
]
