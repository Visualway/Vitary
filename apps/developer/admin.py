from django.contrib import admin
from .models import *

class TokenInline(admin.TabularInline):
    model = Token
    extra = 0
    readonly_fields = ('token',)
    can_delete = False

class DevProfileAdmin(admin.ModelAdmin):
    inlines = [TokenInline]


admin.site.register(Bot)
admin.site.register(DevProfile, DevProfileAdmin)