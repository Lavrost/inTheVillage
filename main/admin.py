from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ObjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", "square", )}  # Формирование slug
    save_as = True  # В админке кнопка "Сохранить как шаблон"
    # save_on_top = True
    list_display = ('id', 'title', 'views', 'slug', 'category', 'created_at', 'get_photo', )
    list_display_links = ('id', 'title', 'get_photo', )
    list_filter = ('category', 'id', 'views', 'created_at',)
    search_fields = ('title', 'created_at', 'updated_at', 'views', 'square',)
    readonly_fields = ('views', 'id', 'created_at', 'updated_at', 'get_photo', )
    fields = ('title', 'description', 'photos', 'get_photo', 'category',
              'created_at', 'updated_at', 'views', 'square', 'slug', )

    def get_photo(self, obj):
        if obj.photos:
            return mark_safe(f'<img src="{obj.photos.url}" width="50">')
        else:
            return '-'

    get_photo.short_description = 'Фото'


admin.site.register(Category)
admin.site.register(User)
admin.site.register(RealtyObject, ObjectAdmin)
