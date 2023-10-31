from django.contrib import admin
from menu_app.models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('parent',)
    search_fields = ('name',)


admin.site.register(MenuItem, MenuItemAdmin)
