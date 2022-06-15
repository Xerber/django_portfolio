from django.shortcuts import render, redirect
from django.views.generic import ListView, View

from .models import WorkExperience, Education, Review
from .forms import OfferForm


class all_data():
  '''Опыт работы и Образование'''
  def get_experience(self):
    return WorkExperience.objects.all().order_by('-start_year')
  
  def get_education(self):
    return Education.objects.all().order_by('-start_year')

  def get_review(self):
    return Review.objects.all()


class WorkExperienceView(all_data, ListView):
  '''Опыт работы'''
  model = WorkExperience
  queryset = WorkExperience.objects.all().order_by('-start_year')
  template_name = 'index.html'


class EducationView(all_data, ListView):
  '''Образование'''
  model = Education
  queryset = Education.objects.all().order_by('-start_year')


class ReviewView(all_data, ListView):
  '''Отзывы'''
  model = Review
  queryset = Review.objects.all()


class AddOffer(View):
  '''Заявка на связь'''
  def post(self, request):
    form = OfferForm(request.POST)
    if form.is_valid():
      form = form.save()
      return redirect("/")
    return redirect("/")