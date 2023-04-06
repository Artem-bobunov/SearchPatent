from django.contrib import admin
#from import_export.admin import ImportExportModelAdmin
from .models import Patents, acd_Patents
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class journalAdmnin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display_list = '__all__'

class TechicalErrorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display_list = ('id')

admin.site.register(Patents,journalAdmnin)
admin.site.register(acd_Patents,TechicalErrorAdmin)