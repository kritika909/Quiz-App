# Generated by Django 5.0.3 on 2024-12-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='quesid',
        ),
        migrations.AddField(
            model_name='answers',
            name='ques',
            field=models.CharField(default='None', max_length=255),
        ),
        migrations.AlterField(
            model_name='session',
            name='correct_ans',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='session',
            name='incorrect_ans',
            field=models.IntegerField(default=0),
        ),
    ]
