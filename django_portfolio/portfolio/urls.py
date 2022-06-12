from django.urls import path
from . import views


urlpatterns = [
    path('', views.WorkExperienceView.as_view())
]