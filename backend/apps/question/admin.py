from django.contrib import admin
from .models import Question, BotUser, UserQuestionAnswer
# Register your models here.

class BotUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user_id', 'username', 'user_status', 'created_at')
    list_filter = ('user_status', 'status','first_name', 'last_name',)
    search_fields = ('first_name', 'last_name', 'user_id', 'username',)
    list_display_links = ('first_name', 'last_name', 'user_id', 'username',)
    

class QuestionAdmin(admin.ModelAdmin):
    list_display = ( 'code', 'subject', 'size', 'status', 'created_at')
    list_filter = ('subject', 'size', 'status', 'created_at')
    search_fields = ('code', 'subject',)

class UserQuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'score', 'start_time', 'end_time')
    list_filter = ('user', 'question', 'score', 'status', 'start_time',)
    search_fields = ('user', 'question', 'score',)


admin.site.register(BotUser, BotUserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserQuestionAnswer, UserQuestionAnswerAdmin)