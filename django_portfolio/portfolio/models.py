from django.db import models


# Create your models here.
class WorkExperience(models.Model):
  '''Опыт работы'''
  start_date = models.DateField("Начало работы", auto_now=False, auto_now_add=False)
  end_date = models.DateField("Окончание", auto_now=False, auto_now_add=False, blank=True, null=True)
  company_name = models.CharField("Название компании", max_length=100)
  position = models.CharField("Должность", max_length=150)
  responsibilities = models.TextField("Обязанности", max_length=2500)

  def __str__(self):
    return f'{self.company_name}: {self.start_date} - {self.end_date}'