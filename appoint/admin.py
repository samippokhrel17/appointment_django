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
    list_display = ('name','limit', 'assign', 'complete' , 'slot_available',)

    def assign(self, obj):
        return Appoinment.objects.filter(branch=obj).count()
    
    def complete(self,obj):
        return Appoinment.objects.filter(branch=obj,is_complete=True).count()
    
    def slot_available(self,obj):
        return obj.limit-(self.assign(obj)-self.complete(obj))
   

    inlines=[AppointmentInline]