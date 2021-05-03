from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Trainer, Review
from .forms import TrainerForm, UserForm, ReviewForm

# See all Trainers
def index(request):
    users_list = User.objects.all()
    trainers_list = Trainer.objects.all()
    template = loader.get_template('trainers/index.html')
    context = {
        'users_list': users_list,
        'trainers_list': trainers_list,
    }
    return HttpResponse(template.render(context, request))

# Trainer Profile
def trainer(request, user_id):
    template = loader.get_template('trainers/trainer.html')
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
            return HttpResponseRedirect('/thanks/') # todo: make this page
    else:
        user_form = UserForm()
        trainer_form = TrainerForm()
    return render(request, 'trainers/trainerform.html', {
        'user_form': user_form,
        'trainer_form': trainer_form
    })

# See all Reviews
def reviews(request):
    review_list = Review.objects.all()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=request.user)
        if review_form.is_valid():
            review_form.save()
            return HttpResponseRedirect('/trainers/reviews')
    else:
        review_form = ReviewForm()
    template = loader.get_template('trainers/reviews.html')
    context = {
        'review_list': review_list,
        'review_form': review_form,
    }
    return HttpResponse(template.render(context, request))

# Review Form
def reviewform(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=request.user)
        if review_form.is_valid():
            review_form.save()
        return HttpResponseRedirect('/trainers/reviewform') # todo: make this page
    else:
        review_form = ReviewForm()
    return render(request, 'trainers/reviewform.html', {
        'review_form': review_form,
    })