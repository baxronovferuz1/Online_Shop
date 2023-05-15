from django.contrib import admin

# Register your models here.

from .models import *

class ItemsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(BaseItem, ItemsAdmin)
admin.site.register(Television , ItemsAdmin)
admin.site.register(Computer , ItemsAdmin)
admin.site.register(Mobile , ItemsAdmin)
admin.site.register(Book , ItemsAdmin)
admin.site.register(Stationery , ItemsAdmin)