from django.contrib import admin
from .models import Question,  UserQuestionAnswer
# Register your models here.



class QuestionAdmin(admin.ModelAdmin):
    list_display = ( 'code', 'subject', 'size', 'status', 'created_at')
    list_filter = ('subject', 'size', 'status', 'created_at')
    search_fields = ('code', 'subject',)

class UserQuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'score', 'start_time', 'end_time')
    list_filter = ('user', 'question', 'score', 'status', 'start_time',)
    search_fields = ('user', 'question', 'score',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(UserQuestionAnswer, UserQuestionAnswerAdmin)