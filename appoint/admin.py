from django.contrib import admin
from .models import *
# Register your models here.
from import_export.admin import ImportExportActionModelAdmin


admin.site.register(Branch)
admin.site.register(Mainbranch)

@admin.register(Appoinment)
class ViewAdmin(ImportExportActionModelAdmin):
    pass

