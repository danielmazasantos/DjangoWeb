from django.contrib import admin
from gestionUsuarios.models import Usuarios
# Register your models here.


class usersAdmin(admin.ModelAdmin):
    list_display = ("nombre","email")
    search_fields = ("nombre","email")
    

admin.site.register(Usuarios,usersAdmin)


