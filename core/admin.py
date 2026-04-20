from django.contrib import admin
from .models import *
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Feedback._meta.fields]

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Perfil._meta.fields]

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Servico._meta.fields]    