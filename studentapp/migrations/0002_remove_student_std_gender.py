# Generated by Django 4.0.5 on 2022-07-04 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='std_gender',
        ),
    ]