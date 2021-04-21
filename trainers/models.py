from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

    # @staticmethod
    # def create_trainer(sender, instance, created, **kwargs):
    #     if created:
    #         Trainer.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_user_trainer(sender, instance, created, **kwargs):
    if created:
        Trainer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_trainer(sender, instance, **kwargs):
    instance.trainer.save()

class Review(models.Model):
    trainer = models.ForeignKey('Trainer', on_delete=models.CASCADE, null=True)
