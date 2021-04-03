from django.urls import path

from . import views

# app_name= 'trainers'

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /trainers/5/
    path('<int:trainer_id>/', views.trainer, name='trainer'),
]