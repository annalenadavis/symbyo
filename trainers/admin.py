from django.contrib import admin

from .models import Discipline, Trainer, Review

# Register your models here.
admin.site.register(Discipline)
admin.site.register(Trainer)
admin.site.register(Review)
