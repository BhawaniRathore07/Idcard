from django.contrib import admin
from .models import Pak_IdCard, Template


class IdCardAdmin(admin.ModelAdmin):
    list_display = ('name','father_name','gender','image','pk')


admin.site.register(Pak_IdCard, IdCardAdmin)


class TemplateAdmin(admin.ModelAdmin):
    list_display = ('template','pk')


admin.site.register(Template,TemplateAdmin)