from django.http import HttpResponse

from .models import Trainer

# See all Trainers
def index(request):
    return HttpResponse("Hello, world. You're at the trainers index.")

# Trainer Profile
def trainer(request, trainer_id):
    return HttpResponse("You're looking at trainer %s." % trainer_id)