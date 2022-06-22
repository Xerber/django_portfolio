from django.shortcuts import render, redirect
from django.views.generic import ListView, View

from .models import WorkExperience, Education, Review, Heading, MyInfo, SocialContact, MySkill, Portfolio
from .forms import OfferForm



def index(request):
    experience = WorkExperience.objects.all().order_by('-start_year')#Опыт работы
    education = Education.objects.all().order_by('-start_year')#Образование
    review = Review.objects.all()#Отзывы
    heading = Heading.objects.all()#табы для портфолио
    myinfo = MyInfo.objects.all()[0]#Обо мне
    social = SocialContact.objects.all()#Социалки

    try:
      heading_active = Heading.objects.get(is_active__exact=1)#активный таб
      heading_na = Heading.objects.get(is_active__exact=0)#неактивный таб
    except:
      heading_active = None
      heading_na = None

    portfolio_all = Portfolio.objects.raw('''SELECT portfolio_portfolio.id,title,poster,portfolio_heading.title_heading,portfolio_portfolio.link_github as url FROM portfolio_portfolio, portfolio_heading WHERE 
                                          portfolio_portfolio.heading_id == portfolio_heading.id AND is_active==True AND draft==False LIMIT 4''')
    portfolio = []
    for i in range(0, len(portfolio_all), 2):
      portfolio.append(portfolio_all[i:i+2])

    portfolio_na_all = Portfolio.objects.raw('''SELECT portfolio_portfolio.id,title,poster,portfolio_heading.title_heading,portfolio_portfolio.link_github as url FROM portfolio_portfolio, portfolio_heading WHERE 
                                          portfolio_portfolio.heading_id == portfolio_heading.id AND is_active==False AND draft==False LIMIT 4''')
    portfolio_na = []
    for i in range(0, len(portfolio_na_all), 2):
      portfolio_na.append(portfolio_na_all[i:i+2])

    myskill_all = list(MySkill.objects.all())#Все социалки
    myskill = []
    for i in range(0, len(myskill_all), 2):
      myskill.append(myskill_all[i:i+2])

    return render(request, 'index.html', {'experience': experience,'education': education,'reviews': review, 
                  'heading': heading,'myinfo': myinfo, 'socials':social, 'myskills': myskill, 'portfolios': portfolio,
                  'portfolios_na':portfolio_na,'heading_active':heading_active,'heading_na':heading_na})


class AddOffer(View):
  '''Заявка на связь'''
  def post(self, request):
    form = OfferForm(request.POST)
    if form.is_valid():
      form = form.save()
      return redirect("/")
    return redirect("/")