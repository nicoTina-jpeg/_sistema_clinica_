from django.contrib import admin

# Importação do módulo models.py
from sistema import models

# Importação do módulo timezone que traz datas e horários
from django.utils import timezone

# Aqui fica o model do paciente
@admin.register(models.Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'telefone', 'ativo',)
    list_editable = ('ativo',)
    search_fields = ('id', 'nome', 'email',)

# Aqui fica o model da especialidade
@admin.register(models.Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)    

# Aqui fica o model do médico
@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'crm', 'ativo',)
    list_editable = ('ativo',)