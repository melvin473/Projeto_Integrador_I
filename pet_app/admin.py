from django.contrib import admin
from pet_app.models import Animal, Evento

# Register your models here.

admin.site.register(Animal),
admin.site.register(Evento)
