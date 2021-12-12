from django.contrib import admin


from .models import *


admin.site.register(Director)
admin.site.register(Film)
admin.site.register(People)
admin.site.register(Planet)
admin.site.register(Producer)

class Peoplefilm(admin.ModelAdmin):
    list_display=('id', 'name','hair_color')

admin.site.register(People_film, Peoplefilm)

