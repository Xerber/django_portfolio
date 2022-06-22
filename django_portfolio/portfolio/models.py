import email
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime



class WorkExperience(models.Model):
  '''Опыт работы'''
  MONTHS = (
    ('Январь','Январь'),
    ('Февраль','Февраль'),
    ('Март','Март'),
    ('Апрель','Апрель'),
    ('Май','Май'),
    ('Июнь','Июнь'),
    ('Июль','Июль'),
    ('Август','Август'),
    ('Сентябрь','Сентябрь'),
    ('Октябрь','Октябрь'),
    ('Ноябрь','Ноябрь'),
    ('Декабрь','Декабрь')
    )
  start_month = models.CharField("Месяц начала работы", max_length=10,choices=MONTHS)
  start_year = models.PositiveSmallIntegerField("Год начала работы")
  end_month = models.CharField("Месяц окончания", max_length=10,choices=MONTHS,blank=True)
  end_year = models.PositiveSmallIntegerField("Год окончания",blank=True, null=True)
  company_name = models.CharField("Название компании", max_length=100)
  position = models.CharField("Должность", max_length=150)
  responsibilities = models.TextField("Обязанности", max_length=2500)

  def __str__(self):
    return f'{self.company_name}: {self.start_month} {self.start_year} - {self.end_month} {self.end_year}'


class Education(models.Model):
  '''Образование'''
  start_year = models.PositiveSmallIntegerField("Год начала обучения")
  end_year = models.PositiveSmallIntegerField("Год окончания обучения",blank=True, null=True)
  title = models.CharField("Название учреждения", max_length=150)
  faculty = models.CharField("Название факультета", max_length=150)
  department = models.CharField("Название отделения", max_length=150)
  description = models.TextField("Описание", max_length=2500)


class Offer(models.Model):
  '''Заявки на связь'''
  STATUS = (('Новая','Новая'),('В работе','В работе'),('Закрыта','Закрыта'))
  name = models.CharField("Имя", max_length=150)
  subject = models.CharField("Тема сообщения", max_length=250)
  email = models.EmailField(blank=True,null=True)
  message = models.TextField("Сообщение", max_length=5000)
  created_at = models.DateTimeField(default=datetime.now)
  comment = models.TextField("Комментарий", max_length=5000, null=True)
  status = models.CharField("Месяц начала работы", max_length=10,choices=STATUS,default='Новая')


class MySkill(models.Model):
  '''Профессиональные навыки'''
  title = models.CharField("Название технологии", max_length=50)
  level = models.PositiveSmallIntegerField("Уровень понимания")


class MyInfo(models.Model):
  '''Обо мне'''
  name = models.CharField("Фамилия Имя", max_length=50)
  speciality = models.CharField("Специальность", max_length=100)
  age = models.PositiveSmallIntegerField("Возраст")
  languages = models.CharField("Языки", max_length=150)
  email = models.EmailField("Почта")
  phone = PhoneNumberField("Телефон")
  about = models.TextField("Обо мне", max_length=2500)
  avatar = models.ImageField("Аватар", upload_to="myinfo/")


class SocialContact(models.Model):
  '''Социалки'''
  name = models.CharField("Название в админке", max_length=100)
  title = models.CharField("Надпись при наведении на иконку", max_length=100)
  link = models.CharField("Ссылка на страницу", max_length=150)
  boot_class = models.CharField("Bootstrap класс иконки", default='fa fa-', max_length=100)


class Heading(models.Model):
  '''Рубрики для портфолио'''
  title_heading = models.CharField("Название рубрики", max_length=100)
  class_heaging = models.CharField("Bootstrap класс иконки", max_length=100)
  url = models.SlugField(max_length=160)
  is_active = models.BooleanField("Отображать рубрику активной", default=False)

  def __str__(self):
    return self.title_heading


class Portfolio(models.Model):
  '''Примеры работ'''
  title = models.CharField("Название работы", max_length=250)
  heading = models.ForeignKey(Heading, verbose_name="Рубрика", on_delete=models.SET_NULL, null=True)
  description = models.TextField("Описание", max_length=2500)
  link = models.CharField("Ссылка на работу в мире", max_length=150)
  link_github = models.CharField("Ссылка на Github", max_length=150)
  poster = models.ImageField("Постер", upload_to="portfolio/")
  draft = models.BooleanField("Черновик", default=False)

  def __str__(self):
    return f'[{self.heading}] {self.title}'



class Review(models.Model):
  '''Отзывы'''
  name = models.CharField("Имя(ник) заказчика", max_length=250)
  where = models.CharField("Источник отзыва (площадка)", max_length=150)
  order_name = models.CharField("Название заказа", max_length=250)
  description = models.TextField("Комментарий", max_length=2500)
  avatar = models.ImageField("Аватар", upload_to="reviews/", default='reviews/default.png')
  is_active = models.BooleanField("Отображать отзыв первым", default=False)