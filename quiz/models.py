from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):
    LEVEL_CHOICES = [
        ('BASIC', 'Basic'),
        ('INTERMEDIATE', 'Intermediate'),
        ('ADVANCED', 'Advanced'),
    ]
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=12, choices=LEVEL_CHOICES, default='BASIC')
    numofques = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.level})"

class Question(models.Model):
    quizid = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    ques = models.CharField(max_length=255)
    optionA = models.CharField(max_length=100)
    optionB = models.CharField(max_length=100)
    optionC = models.CharField(max_length=100)
    optionD = models.CharField(max_length=100)
    ans = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    marks = models.IntegerField(default=1)


class Session(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    quizid = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    correct_ans = models.IntegerField(default=0)
    incorrect_ans= models.IntegerField(default=0) 
    taken_at = models.DateTimeField(auto_now=True)
    total_marks = models.IntegerField(default=0)

class Answers(models.Model):
    sessionid = models.ForeignKey(Session, on_delete=models.CASCADE)
    ques = models.CharField(max_length=255, default="None")
    user_ans = models.CharField(max_length=1, null=True)
    corr_ans = models.CharField(max_length=1)



