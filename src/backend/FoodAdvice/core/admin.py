from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Client)
admin.site.register(Restaurant)
admin.site.register(Localisation)
admin.site.register(Reservation)


@admin.register(Carte)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('intitule',)
    fieldsets = (
        (None, {
            'fields': ('resto',  'intitule'),
        }),
    )


admin.site.register(Plat)
admin.site.register(Like)
admin.site.register(Menu)
admin.site.register(MenuPlate)
admin.site.register(SavedMenu)
