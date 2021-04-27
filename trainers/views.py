from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Trainer
from .forms import TrainerForm, UserForm

# See all Trainers
def index(request):
    users_list = User.objects.all()
    trainers_list = Trainer.objects.all()
    template = loader.get_template('reviews/index.html')
    context = {
        'users_list': users_list,
        'trainers_list': trainers_list,
    }
    return HttpResponse(template.render(context, request))

# Trainer Profile
def trainer(request, user_id):
    template = loader.get_template('reviews/trainer.html')
    user = User.objects.get(id=user_id)
    context = {
        'user_id' : user_id,
        'user' : user,
        'disc_list' : user.trainer.disciplines.all(),
    }
    return HttpResponse(template.render(context, request))

# Register Trainer Form
def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        trainer_form = TrainerForm(request.POST, instance=request.user.trainer)
        if user_form.is_valid() and trainer_form.is_valid():
            user_form.save()
            trainer_form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        user_form = UserForm()
        trainer_form = TrainerForm()
    return render(request, 'trainerform.html', {
        'user_form': user_form,
        'trainer_form': trainer_form
    })