import imp
from django.contrib import admin
from .models import Detail, Project

# Register your models here.
@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display= ['id','name', 'what_i_do']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display= ['id', 'name']