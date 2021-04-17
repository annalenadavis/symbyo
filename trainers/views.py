from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User

from .models import Trainer

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
    object_id = user_id - 1
    user = User.objects.all()[object_id]
    context = {
        'user_id' : user_id,
        'user' : user,
        'disc_list' : user.trainer.disciplines.all(),
    }
    return HttpResponse(template.render(context, request))