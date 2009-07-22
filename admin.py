from django.contrib import admin
from thespians.models import *


admin.site.register(Role)
admin.site.register(Person)


class PersonAdmin(admin.ModelAdmin):
    list_filter = ('person_types',)
    search_fields = ('user.first_name', 'user.last_name')
    #prepopulated_fields = {'slug': ('user.first_name','user.last_name')}

