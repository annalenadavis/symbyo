from django.http import HttpResponse
from django.template import loader

from .models import Trainer

# See all Trainers
def index(request):
    trainers_list = Trainer.objects.all()
    template = loader.get_template('reviews/index.html')
    context = {
        'trainers_list': trainers_list,
    }
    return HttpResponse(template.render(context, request))

# Trainer Profile
def trainer(request, trainer_id):
    template = loader.get_template('reviews/trainer.html')
    context = {
        'trainer_id' : trainer_id,
    }
    return HttpResponse(template.render(context, request))