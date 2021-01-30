from django.urls import path
from core import views
from django.contrib.auth import views as auth_views

app_name = "core"


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('ver-notas/', views.VisualizarNotasControl.as_view(), name='ver-notas'),
    path('controlar-inscricoes/<int:pk>/',
         views.ControlarAndamentoInscricoesControl.as_view(), name='controlar-inscricoes'),
]
