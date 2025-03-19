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
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions', null=True)
    text = models.TextField(null=True)

    def __str__(self):
        return self.text or "Untitled Question "
    
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    
class QuizSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    selected_questions = models.ManyToManyField(Question)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.name}"
    
class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    quiz_session = models.ForeignKey(QuizSession, on_delete=models.CASCADE, related_name='user_responses')

    def __str__(self):
        return f"{self.user.username} - {self.quiz.name} - {self.question.text}"


# class Session(models.Model):
#     userid = models.ForeignKey(User, on_delete=models.CASCADE)
#     quizid = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     correct_ans = models.IntegerField(default=0)
#     incorrect_ans= models.IntegerField(default=0) 
#     taken_at = models.DateTimeField(auto_now=True)
#     total_marks = models.IntegerField(default=0)

# class Answers(models.Model):
#     sessionid = models.ForeignKey(Session, on_delete=models.CASCADE)
#     ques = models.CharField(max_length=255, default="None")
#     user_ans = models.CharField(max_length=1, null=True)
#     corr_ans = models.CharField(max_length=1)



