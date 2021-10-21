from django.contrib import admin
from .models import Category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display= ('image_tag','title', 'description', 'url', 'add_date')
    search_fields = ('title',)



admin.site.register(Category, CategoryAdmin)
