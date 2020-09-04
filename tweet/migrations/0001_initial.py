# Generated by Django 3.1 on 2020-09-04 15:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(default='', max_length=140)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
