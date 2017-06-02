from django.contrib import admin

from township.frontpage.models import State, Muni, Location

# Register your models here.
admin.site.register(State)
admin.site.register(Muni)
admin.site.register(Location)