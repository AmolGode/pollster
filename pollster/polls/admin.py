from django.contrib import admin

# Register your models here.

from .models import Question,Choice

admin.site.site_header = 'Pollster Admin'
admin.site.site_title = 'Pollster Admin Area'
admin.site.index_title = 'Pollster admin page'

# admin.site.register(Question)
# admin.site.register(Choice)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['question_text','pub_date']
    fieldsets = [('Question Text',{'fields':['question_text']}),('Date Information',{'fields':['pub_date'],'classes':['colapse']}),]
    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)