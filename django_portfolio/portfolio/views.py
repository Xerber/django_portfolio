from django.shortcuts import render
from django.views.generic.base import View

from .models import WorkExperience

# Create your views here.
class WorkExperienceView(View):
  '''Опыт работы'''
  def get(self, request):
    experience = WorkExperience.objects.all().order_by('-start_year')
    return render(request,'index.html',{'experience': experience})