from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, View

from core.models import Aluno, Inscricao, Nota


@method_decorator(login_required, name='dispatch')
class VisualizarNotasControl(DetailView):
    model = Nota
    template_name = 'TelaVisualizarNotas.html'

    def get_queryset(self):

        aluno = get_object_or_404(Aluno, user=self.request.user)
        inscricoes = Inscricao.objects.filter(aluno=aluno)
        notas = Nota.objects.filter(inscricao__in=inscricoes)

        return notas


class LancarNotasControl(View):
    slug_field = 'titulo'
    model = Nota
    context_object_name = 'meu_artigo'
    template_name = 'detalhe_artigo.html'

    def get_queryset(self):
        return self.model.filter(user=self.request.user)


class AbrirTurmaControl(View):
    slug_field = 'titulo'
    model = Nota
    context_object_name = 'meu_artigo'
    template_name = 'detalhe_artigo.html'

    def get_queryset(self):
        return self.model.filter(user=self.request.user)


class ControlarPrazosControl(View):
    slug_field = 'titulo'
    model = Nota
    context_object_name = 'meu_artigo'
    template_name = 'detalhe_artigo.html'

    def get_queryset(self):
        return self.model.filter(user=self.request.user)


class ControlarAtrasosControl(View):
    slug_field = 'titulo'
    model = Nota
    context_object_name = 'meu_artigo'
    template_name = 'detalhe_artigo.html'

    def get_queryset(self):
        return self.model.filter(user=self.request.user)


class RealizarInscricaoControl(View):
    slug_field = 'titulo'
    model = Nota
    context_object_name = 'meu_artigo'
    template_name = 'detalhe_artigo.html'

    def get_queryset(self):
        return self.model.filter(user=self.request.user)

