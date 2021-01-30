from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, View, ListView
from django.core.exceptions import PermissionDenied

from core.models import Aluno, Inscricao, Nota, Disciplina


@method_decorator(login_required, name='dispatch')
class VisualizarNotasControl(ListView):
    model = Nota
    template_name = 'TelaVisualizarNotas.html'

    def get_queryset(self):

        aluno = get_object_or_404(Aluno, user=self.request.user)
        inscricoes = Inscricao.objects.filter(aluno=aluno)
        notas = Nota.objects.filter(inscricao__in=inscricoes)

        return notas


@method_decorator(login_required, name='dispatch')
class ControlarAndamentoInscricoesControl(ListView):
    model = Inscricao
    template_name = 'ControlarAndamentoInscricoes.html'

    def get_context_data(self, **kwargs):
        context = super(ControlarAndamentoInscricoesControl, self).get_context_data(**kwargs)
        disciplina = get_object_or_404(Disciplina, pk=self.kwargs['pk'])
        context['disciplina'] = disciplina.nome
        context['object_list'] = Inscricao.objects.filter(turma__disciplina__pk=self.kwargs['pk'])
        return context

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise PermissionDenied()
        return super(ControlarAndamentoInscricoesControl, self).get(request, *args, **kwargs)


class LancarNotasControl(View):
    pass


class AbrirTurmaControl(View):
    pass


class ControlarPrazosControl(View):
    pass


class ControlarAtrasosControl(View):
    pass


class RealizarInscricaoControl(View):
    pass

