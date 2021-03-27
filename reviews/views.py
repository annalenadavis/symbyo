from django.http import HttpResponse

# from .models import Discipline, Trainer

def index(request):
    return HttpResponse("Hello, world. You're at the reviews index.")