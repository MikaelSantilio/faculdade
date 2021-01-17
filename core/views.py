from django.shortcuts import render
from django.views.generic import View, DetailView, FormView, RedirectView
from core.models import Nota, Inscricao, Aluno
from django.shortcuts import get_object_or_404
from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.conf import settings
from django.utils.decorators import method_decorator

class LoginView(FormView):
    """
    Provides the ability to login as a user with a username and password
    """
    success_url = '/'
    template_name = 'Login.html'
    form_class = AuthenticationForm

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('core:ver-nota')


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/ver-notas')

class LogoutView(View):
    def get(self, request):
        return HttpResponseRedirect(settings.LOGIN_URL)


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


class AbrirTurmaControl(View):
    slug_field = 'titulo'
    model = Nota
    context_object_name = 'meu_artigo'
    template_name = 'detalhe_artigo.html'

    def get_queryset(self):
        return self.model.filter(user=self.request.user)