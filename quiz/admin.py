from django.contrib import admin
from .models import Question, Quiz, Option, UserResponse, QuizSession

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(UserResponse)
admin.site.register(QuizSession)
