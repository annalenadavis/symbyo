from django.urls import path

from . import views

# app_name= 'trainers'

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /trainers/5/
    path('<int:user_id>/', views.trainer, name='trainer'),
    path('register', views.register, name='register'),
    path('reviews', views.reviews, name='reviews'),
    path('reviewform', views.reviewform, name='reviewform'),
]