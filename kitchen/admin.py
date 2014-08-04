from django.contrib import admin

from kitchen.models import *

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'category', 'created_at', 'modified_at']
    search_fields = ['title', 'description']
    filter = ['category']
    readonly_fields = ['created_at', 'modified_at']
    raw_id_field = ['user', 'modified_by']
admin.site.register(Recipe, RecipeAdmin)