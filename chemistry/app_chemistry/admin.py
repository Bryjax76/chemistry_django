from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Elements)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'symbol',
        'atomic_number',
        'atomic_weight',
        'block',
        'character',
        'state',
        'melting_temp',
        'boiling_temp',
        'atomic_radius'
        )

admin.site.register(Value)
admin.site.register(State)
admin.site.register(Character)
admin.site.register(Group)
admin.site.register(Period)
admin.site.register(Block)