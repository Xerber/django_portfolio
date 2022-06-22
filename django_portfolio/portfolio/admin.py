from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import WorkExperience, Education, Offer, Review, Heading, MyInfo, SocialContact, MySkill, Portfolio
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

class MyInfoAdminForm(forms.ModelForm):
    about = forms.CharField(label='Обо мне', widget=CKEditorUploadingWidget())
    class Meta:
        model = MyInfo
        fields = '__all__'

class PortfolioAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание работы', widget=CKEditorUploadingWidget())
    class Meta:
        model = Portfolio
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



@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
  '''Примеры работ'''
  list_display = ("title","heading","link_github","draft")
  readonly_fields = ("get_image",)
  list_editable = ("draft",)
  form = PortfolioAdminForm
  fieldsets = (
    (None, {
      "fields": (("title","heading"),)
    }),
    (None, {
      "fields": (("description",),)
    }),
    (None, {
      "fields": (("link","link_github"),)
    }),
    (None, {
      "fields": (("poster","get_image"),)
    }),
    (None, {
      "fields": (("draft"),)
    }),
  )


  def get_image(self,obj):
    return mark_safe(f'<img src={obj.poster.url} width="50" height="50"')
  
  get_image.short_description = "Превью"

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

@admin.register(MySkill)
class MySkillAdmin(admin.ModelAdmin):
  '''Профессиональные навыки'''
  list_display = ("title","level")


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
  '''Заявки на связь'''
  list_display = ("subject","name","email","message","created_at","comment","status")
  readonly_fields = ("subject","name","email","message","created_at")
  list_display_links = ("subject",)
  search_fields = ("subject",)

@admin.register(Heading)
class HeadingAdmin(admin.ModelAdmin):
  '''Категории портфолио'''
  list_display = ("title_heading","class_heaging","url","is_active")
  list_editable = ("is_active",)

@admin.register(MyInfo)
class MyInfoAdmin(admin.ModelAdmin):
  '''Личная информация'''
  list_display = ("name","speciality")
  readonly_fields = ("get_image",)
  form = MyInfoAdminForm
  fieldsets = (
    (None, {
      "fields": (("name","speciality","age","languages"),)
    }),
    (None, {
      "fields": (("email","phone"),)
    }),
    (None, {
      "fields": (("about",),)
    }),
    (None, {
      "fields": (("avatar","get_image"),)
    }),
  )

  def get_image(self,obj):
    return mark_safe(f'<img src={obj.avatar.url} width="50" height="50"')
  
  get_image.short_description = "Превью"


@admin.register(SocialContact)
class SocialContactAdmin(admin.ModelAdmin):
  '''Социалки'''
  list_display = ("name","title","link")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
  '''Отзывы'''
  list_display = ("order_name","where","name","description","get_image","is_active")
  readonly_fields = ("get_image",)
  list_display_links = ("order_name",)
  search_fields = ("order_name","where")
  list_editable = ("is_active",)
  fieldsets = (
    (None, {
      "fields": (("name","order_name","where"),)
    }),
    (None, {
      "fields": (("description",),)
    }),
    (None, {
      "fields": (("avatar","get_image"),)
    }),
    (None, {
      "fields": (("is_active",),)
    }),
  )

  def get_image(self,obj):
    return mark_safe(f'<img src={obj.avatar.url} width="50" height="50"')
  
  get_image.short_description = "Превью"