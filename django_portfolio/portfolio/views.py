from django.shortcuts import render, redirect
from django.views.generic import ListView, View

from .models import WorkExperience, Education
from .forms import OfferForm


class ExperienceEducation():
  '''Опыт работы и Образование'''
  def get_experience(self):
    return WorkExperience.objects.all().order_by('-start_year')
  
  def get_education(self):
    return Education.objects.all().order_by('-start_year')


class WorkExperienceView(ExperienceEducation, ListView):
  '''Опыт работы'''
  model = WorkExperience
  queryset = WorkExperience.objects.all().order_by('-start_year')
  template_name = 'index.html'


class EducationView(ExperienceEducation, ListView):
  '''Образование'''
  model = Education
  queryset = Education.objects.all().order_by('-start_year')


class AddOffer(View):
  '''Заявка на связь'''
  def post(self, request):
    form = OfferForm(request.POST)
    if form.is_valid():
      form = form.save()
      return redirect("/")
    return redirect("/")