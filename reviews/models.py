from django.db import models

class Discipline(models.Model):
    AREA = [
        ('MEDITATION', 'Meditation'),
        ('MUAYTHAI', 'Muay Thai'),
        ('MMA', 'Mixed Martial Arts'),
        ('YOGA', 'Yoga'),       
    ]
    area = models.CharField(max_length=50, choices=AREA)

    def __str__(self):
        return self.area

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    name = str(first_name) + str(last_name)
    email = models.EmailField()
    portrait = models.ImageField()

    def __str__(self):
        return self.name

class Trainer(Person):
    description = models.TextField()
    website = models.URLField()
    disciplines = models.ManyToManyField('Discipline')

    def __str__(self):
        return self.name

class Student(Person):
    teachers = models.ForeignKey('Trainer', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Review(models.Model):
    trainer = models.ForeignKey('Trainer', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
