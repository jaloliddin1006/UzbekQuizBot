from django.contrib import admin
from .models import Question,  UserQuestionAnswer
# Register your models here.



class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'subject', 'size', 'is_active', 'created_at')
    list_filter = ('user', 'subject', 'size', 'is_active', 'created_at')
    search_fields = ('code', 'subject',)
    list_editable = ('is_active', 'user')
    list_display_links = ('code', 'subject',)

class UserQuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'score', 'start_time', 'end_time')
    list_filter = ('user', 'question', 'score', 'is_active', 'start_time',)
    search_fields = ('user', 'question', 'score',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(UserQuestionAnswer, UserQuestionAnswerAdmin)