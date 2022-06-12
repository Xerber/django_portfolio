from django.db import models


# Create your models here.
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
  start_month = models.CharField("Месяц начала работы", max_length=10,choices=MONTHS,default='Январь')
  start_year = models.PositiveSmallIntegerField("Год начала работы",default=1999)
  end_month = models.CharField("Месяц окончания", max_length=10,choices=MONTHS,default='',blank=True)
  end_year = models.PositiveSmallIntegerField("Год окончания",default=2000,blank=True, null=True)
  company_name = models.CharField("Название компании", max_length=100)
  position = models.CharField("Должность", max_length=150)
  responsibilities = models.TextField("Обязанности", max_length=2500)

  def __str__(self):
    return f'{self.company_name}: {self.start_month} {self.start_year} - {self.end_month} {self.end_year}'