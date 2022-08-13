from django.contrib import admin

from .models import *


class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'desc')
    fields = ('title', 'desc', 'created_at')


admin.site.register(Tasks, TasksAdmin)

admin.site.site_title = 'Список дел'
admin.site.site_header = 'Список дел'
