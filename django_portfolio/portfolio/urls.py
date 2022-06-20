from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('offer/', views.AddOffer.as_view(), name="add_offer")
]