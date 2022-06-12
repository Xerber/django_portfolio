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
  list_display = ("company_name","start_month","start_year","end_month","end_year","position")
  list_display_links = ("company_name",)
  form = WorkExperienceAdminForm
  search_fields = ("company_name",)
  fieldsets = (
    (None, {
      "fields": (("start_month","start_year"),)
    }),
    (None, {
      "fields": (("end_month","end_year"),)
    }),
    (None, {
      "fields": (("company_name","position"),)
    }),
    (None, {
      "fields": (("responsibilities"),)
    }),
  )
