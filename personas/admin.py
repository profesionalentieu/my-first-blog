from django.contrib import admin
from .models import Domicilio, Socios, Profesores, Administracion, Menores, Comunes, Jubilados, Alertas

admin.site.register(Domicilio)
admin.site.register(Socios)
admin.site.register(Profesores)
admin.site.register(Administracion)
admin.site.register(Menores)
admin.site.register(Comunes)
admin.site.register(Jubilados)
admin.site.register(Alertas)
