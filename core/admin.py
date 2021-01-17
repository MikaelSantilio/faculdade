from django.contrib import admin
from core import models


# @admin.register(models.User)
# class UserAdmin(admin.ModelAdmin):
#     fields = (
#         'username',
#         'email',
#         'is_aluno',
#         'is_professor',
#         'is_active',
#         'is_superuser')


admin.site.register(models.User)
admin.site.register(models.Aluno)
admin.site.register(models.Professor)
admin.site.register(models.Sala)
admin.site.register(models.Laboratorio)
admin.site.register(models.Disciplina)
admin.site.register(models.Semestre)
admin.site.register(models.Horario)
admin.site.register(models.Turma)
admin.site.register(models.Inscricao)
admin.site.register(models.Nota)
