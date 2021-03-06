# Generated by Django 3.1.5 on 2021-01-17 13:24

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_professor', models.BooleanField(default=False)),
                ('is_aluno', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=32)),
                ('descricao', models.TextField(default='Uma descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diaSemana', models.IntegerField(choices=[(2, 'Segunda'), (3, 'Terça'), (4, 'Quarta'), (5, 'Quinta'), (6, 'Sexta'), (7, 'Sábado')])),
                ('horarioInicio', models.TimeField()),
                ('horarioFim', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacao', models.CharField(max_length=10, unique=True)),
                ('capacidade', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacao', models.CharField(max_length=10, unique=True)),
                ('capacidade', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.PositiveIntegerField()),
                ('periodo', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.user')),
                ('matricula', models.CharField(max_length=12, unique=True)),
                ('nome', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.user')),
                ('matricula', models.CharField(max_length=12, unique=True)),
                ('nome', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.disciplina')),
                ('horarioLaboratorio', models.ManyToManyField(related_name='horarios_laboratorio', to='core.Horario')),
                ('horarioSala', models.ManyToManyField(related_name='horarios_sala', to='core.Horario')),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laboratorios_turmas', to='core.laboratorio')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salas_turmas', to='core.sala')),
                ('semestre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.semestre')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Prazo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prazo', models.DateField()),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.disciplina')),
                ('semestre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.semestre')),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField()),
                ('inscricao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.inscricao')),
            ],
        ),
        migrations.AddField(
            model_name='inscricao',
            name='semestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.semestre'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.turma'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.aluno'),
        ),
    ]
