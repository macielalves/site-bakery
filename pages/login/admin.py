from django.contrib import admin

from pages.login import models

# Register your models here.

@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = 'id' ,'nome_de_usuário', 'email'
    ordering = "id",
    list_filter = "nome_de_usuário",
    search_fields = 'id','nome_de_usuário'
    list_per_page = 10
    list_max_show_all = 50
