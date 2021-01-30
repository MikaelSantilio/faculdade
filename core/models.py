from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_professor = models.BooleanField(default=False)
    is_aluno = models.BooleanField(default=False)


class Aluno(models.Model):
    user = models.OneToOneField(User, related_name='aluno', on_delete=models.CASCADE, primary_key=True)
    matricula = models.CharField(max_length=12, unique=True)
    nome = models.CharField(max_length=32)


class Professor(models.Model):
    user = models.OneToOneField(User, related_name='professor', on_delete=models.CASCADE, primary_key=True)
    matricula = models.CharField(max_length=12, unique=True)
    nome = models.CharField(max_length=32)


class Sala(models.Model):
    localizacao = models.CharField(max_length=10, unique=True)
    capacidade = models.PositiveIntegerField()


class Laboratorio(models.Model):
    localizacao = models.CharField(max_length=10, unique=True)
    capacidade = models.PositiveIntegerField()


class Disciplina(models.Model):
    nome = models.CharField(max_length=32)
    descricao = models.TextField(default='Uma descrição')


class Semestre(models.Model):
    ano = models.PositiveIntegerField()
    periodo = models.PositiveIntegerField()


class Horario(models.Model):
    DIAS_SEMANA = (
        (2, "Segunda"),
        (3, "Terça"),
        (4, "Quarta"),
        (5, "Quinta"),
        (6, "Sexta"),
        (7, "Sábado")
    )

    diaSemana = models.IntegerField(choices=DIAS_SEMANA)
    horarioInicio = models.TimeField()
    horarioFim = models.TimeField()


class Turma(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, related_name="salas_turmas", on_delete=models.CASCADE)
    horarioSala = models.ManyToManyField(Horario, related_name="horarios_sala")
    laboratorio = models.ForeignKey(Laboratorio, related_name="laboratorios_turmas", on_delete=models.CASCADE)
    horarioLaboratorio = models.ManyToManyField(Horario, related_name="horarios_laboratorio")


class Inscricao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)


class Nota(models.Model):
    nota = models.FloatField()
    inscricao = models.ForeignKey(Inscricao, on_delete=models.CASCADE)











class Prazo(models.Model):
    prazo = models.DateField()
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)




