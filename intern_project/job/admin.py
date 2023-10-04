from django.contrib import admin

from .models import *
# Register your models here.

# admin.site.register(Job)
# admin.site.register(Company)
# admin.site.register(Applying)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country', 'region']

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_id', 'position', 'reward', 'content', 'technology']

@admin.register(Applying)
class ApplyingAdmin(admin.ModelAdmin):
    list_display = ['id', 'job_id', 'user_id']