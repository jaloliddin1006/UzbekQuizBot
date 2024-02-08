from django.contrib import admin
from .models import BotUser

# Register your models here.
class BotUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user_id', 'username', 'user_status', 'created_at')
    list_filter = ('user_status', 'status','first_name', 'last_name',)
    search_fields = ('first_name', 'last_name', 'user_id', 'username',)
    list_display_links = ('first_name', 'last_name', 'user_id', 'username',)
    
admin.site.register(BotUser, BotUserAdmin)