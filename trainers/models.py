from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

class Discipline(models.Model):
    area = models.CharField(max_length=50)
    parent = models.ForeignKey('Discipline', on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return self.area

class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    business = models.CharField(max_length=100, blank=True)
    disciplines = models.ManyToManyField('Discipline', blank=True)

    @property
    def name(self):
        return self.user.first_name + " " + self.user.last_name

    def __str__(self):
        return self.name

class Review(models.Model):
    trainer = models.ForeignKey('Trainer', on_delete=models.CASCADE, null=True)
    review = models.TextField(null=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], help_text="Choose between 1 and 5", null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
