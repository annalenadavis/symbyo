from django.db import models

class Discipline(models.Model):
    AREA = [
        ('MEDITATION', 'Meditation'),
        ('MUAYTHAI', 'Muay Thai'),
        ('MMA', 'Mixed Martial Arts'),
        ('YOGA', 'Yoga'),       
    ]
    area = models.CharField(max_length=50, choices=AREA)

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    portrait = models.ImageField()

class Trainer(Person):
    description = models.TextField()
    website = models.URLField()
    disciplines = models.ManyToManyField('Discipline', on_delete=models.PROTECT)

class Student(Person):
    teachers = models.ForeignKey('Trainer', on_delete=models.PROTECT)

class Review(models.Model):
    trainer = models.ForeignKey('Trainer', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
