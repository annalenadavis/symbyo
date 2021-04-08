from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Discipline(models.Model):
    area = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return self.area

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teachers = models.ForeignKey('Trainer', on_delete=models.PROTECT, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Trainer(Profile):
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    business = models.CharField(max_length=100, blank=True)
    disciplines = models.ManyToManyField('Discipline', blank=True)

class Review(models.Model):
    # trainer = models.ForeignKey('Trainer', on_delete=models.CASCADE)
    reviewer = models.ForeignKey('Profile', on_delete=models.CASCADE)