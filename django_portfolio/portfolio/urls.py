from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_portfolio, name='view_portfolio'),
    path('offer/', views.AddOffer.as_view(), name="add_offer")
]