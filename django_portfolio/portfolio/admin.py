from django.contrib import admin
from django import forms
from .models import WorkExperience, Education, Offer
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class WorkExperienceAdminForm(forms.ModelForm):
    responsibilities = forms.CharField(label='Обязанности', widget=CKEditorUploadingWidget())
    class Meta:
        model = WorkExperience
        fields = '__all__'

class EducationAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = Education
        fields = '__all__'

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


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
  '''Образование'''
  list_display = ("title","faculty","department","start_year","end_year")
  list_display_links = ("title",)
  form = EducationAdminForm
  search_fields = ("title",)
  fieldsets = (
    (None, {
      "fields": (("start_year","end_year"),)
    }),
    (None, {
      "fields": (("title","faculty","department"),)
    }),
    (None, {
      "fields": (("description"),)
    }),
  )


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
  '''Заявки на связь'''
  list_display = ("subject","name","email","message","created_at","comment","status")
  readonly_fields = ("subject","name","email","message","created_at")
  list_display_links = ("subject",)
  search_fields = ("subject",)