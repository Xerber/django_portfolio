from django.urls import path
from . import views


urlpatterns = [
    path('', views.WorkExperienceView.as_view()),
    path('offer/', views.AddOffer.as_view(), name="add_offer")
]