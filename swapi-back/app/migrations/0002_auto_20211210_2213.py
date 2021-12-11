# Generated by Django 2.2.13 on 2021-12-11 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='eye_color',
            field=models.CharField(choices=[('BLACK', 'black'), ('BROWN', 'brown'), ('YELLOW', 'yellow'), ('RED', 'red'), ('GREEN', 'green'), ('PURPLE', 'purple'), ('UNKNOWN', 'unknown')], max_length=32),
        ),
        migrations.AlterField(
            model_name='people',
            name='hair_color',
            field=models.CharField(choices=[('BLACK', 'black'), ('BROWN', 'brown'), ('BLONDE', 'blonde'), ('RED', 'red'), ('WHITE', 'white'), ('BALD', 'bald')], max_length=32),
        ),
    ]
