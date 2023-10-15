from django.contrib import admin
from .models import *
# Register your models here.
from import_export.admin import ImportExportActionModelAdmin


# admin.site.register(Branch)
admin.site.register(Mainbranch)

# @admin.register(Appoinment)
# class ViewAdmin(ImportExportActionModelAdmin):
#     pass


class AppointmentInline(admin.TabularInline):
    model=Appoinment

@admin.register(Appoinment)
class Member(admin.ModelAdmin):
    list_display = ('name', 'location', 'branch', 'is_complete')



@admin.register(Branch)
class Branch(admin.ModelAdmin):
    # list_display = ('name', 'location', 'branch', 'is_complete')
    inlines=[AppointmentInline]