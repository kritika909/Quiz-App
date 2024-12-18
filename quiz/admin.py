from django.contrib import admin
from .models import Question, Quiz, Answers, Session

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Session)
admin.site.register(Answers)
