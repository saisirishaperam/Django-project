from django.contrib import admin

# Register your models here.
from app1.models import student,teacher

class st_admin(admin.ModelAdmin):

    list_display = ['st_id','st_name','st_email','st_age','st_gender','st_mobile','st_address']
    ordering = ['st_id']
    

admin.site.register(student, st_admin)

class teach_admin(admin.ModelAdmin):

    list_display = ['teach_id','teach_name','teach_email','teach_age','teach_gender','teach_mobile','teach_address']
    ordering = ['teach_id']
    
admin.site.register(teacher,teach_admin)