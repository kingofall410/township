from django.contrib import admin

from township.frontpage.models import State, Muni, Location, County

# Register your models here.
admin.site.register(State)
admin.site.register(Muni)
admin.site.register(Location)
admin.site.register(County)