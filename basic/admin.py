from django.contrib import admin


from basic.models import Student

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city') 

admin.site.register(Student, StudentsAdmin)