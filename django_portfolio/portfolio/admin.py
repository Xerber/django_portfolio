from django.contrib import admin
from django import forms
from .models import WorkExperience
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class WorkExperienceAdminForm(forms.ModelForm):
    responsibilities = forms.CharField(label='Обязанности', widget=CKEditorUploadingWidget())
    class Meta:
        model = WorkExperience
        fields = '__all__'


# Register your models here.
@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
  '''Опыт работы'''
  list_display = ("start_date","end_date","company_name","position","responsibilities")
  form = WorkExperienceAdminForm
  search_fields = ("company_name",)