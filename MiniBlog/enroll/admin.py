from django.contrib import admin
from . models import PostData
# Register your models here.


@admin.register(PostData)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'titel', 'desc']
