from django.urls import path
from core import views
from django.contrib.auth import views as auth_views

from django.contrib.auth import views as auth_views

app_name = "core"


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', views.logout, name='logout'),
    
    # path('logout/', auth_views.logout, {'next_page': '/login'}),
    path('ver-nota/', views.VisualizarNotasControl.as_view(), name='ver-nota'),
]
