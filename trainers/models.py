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
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    portrait = models.ImageField(blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Trainer(Person):
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    business = models.CharField(max_length=100, blank=True)
    disciplines = models.ManyToManyField('Discipline', blank=True)

    if (not business):
        def __str__(self):
            return self.first_name + " " + self.last_name
    else:
        def __str__(self):
            return self.first_name + " " + self.last_name + ", " + self.business

class Student(Person):
    teachers = models.ForeignKey('Trainer', on_delete=models.PROTECT, blank=True)

class Review(models.Model):
    trainer = models.ForeignKey('Trainer', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
