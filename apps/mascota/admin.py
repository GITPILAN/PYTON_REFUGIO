from django.contrib import admin
from apps.mascota.models import Mascota, Vacunas
# Register your models here.

admin.site.register(Vacunas)
admin.site.register(Mascota)
