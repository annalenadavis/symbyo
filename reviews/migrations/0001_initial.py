# Generated by Django 3.1.7 on 2021-03-27 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(choices=[('MEDITATION', 'Meditation'), ('MUAYTHAI', 'Muay Thai'), ('MMA', 'Mixed Martial Arts'), ('YOGA', 'Yoga')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('portrait', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='reviews.person')),
                ('description', models.TextField()),
                ('website', models.URLField()),
                ('disciplines', models.ManyToManyField(to='reviews.Discipline')),
            ],
            bases=('reviews.person',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='reviews.person')),
                ('teachers', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reviews.trainer')),
            ],
            bases=('reviews.person',),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.student')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.trainer')),
            ],
        ),
    ]