from django.shortcuts import render, redirect
from django.views.generic import ListView, View

from .models import WorkExperience, Education, Review, Heading, MyInfo, SocialContact, MySkill
from .forms import OfferForm



def index(request):
    experience = WorkExperience.objects.all().order_by('-start_year')#Опыт работы
    education = Education.objects.all().order_by('-start_year')#Образование
    review = Review.objects.all()#Отзывы
    heading = Heading.objects.all()#табы для портфолио
    myinfo = MyInfo.objects.all()[0]#Обо мне
    social = SocialContact.objects.all()#Социалки
    myskill_all = list(MySkill.objects.all())#Все социалки
    myskill = []
    for i in range(0, len(myskill_all), 2):
      myskill.append(myskill_all[i:i+2])
    return render(request, 'index.html', {'experience': experience,'education': education,'reviews': review, 
                  'heading': heading,'myinfo': myinfo, 'socials':social, 'myskills': myskill})


class AddOffer(View):
  '''Заявка на связь'''
  def post(self, request):
    form = OfferForm(request.POST)
    if form.is_valid():
      form = form.save()
      return redirect("/")
    return redirect("/")