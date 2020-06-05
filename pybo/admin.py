from django.contrib import admin

from .models import *

class QuestionAdmin(admin.ModelAdmin) :
    search_fields = ['subject']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Project_Info)

# Register your models here.
