from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz, Question, UserResponse, QuizSession, Option
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
import random

# Create your views here.

def home(request):
    return render(request, "home.html")

def quiz(request):
    test = Quiz.objects.all()
    return render(request, "quiz.html", {"quizzes": test})

@login_required
def ques(request, quizid):
    quiz = get_object_or_404(Quiz, id=quizid)
    user = request.user
    # questions = Question.objects.filter(quiz=quiz).order_by('?')[:quiz.numofques].prefetch_related('options')

    quiz_session = QuizSession.objects.filter(user=user, quiz=quiz).first()

    if not quiz_session:
        all_questions = list(quiz.questions.all())
        random_question = random.sample(all_questions, min(10, len(all_questions)))
        quiz_session = QuizSession.objects.create(user = user, quiz=quiz)
        quiz_session.selected_questions.set(random_question)

    selected_questions = quiz_session.selected_questions.prefetch_related(Prefetch('options', queryset=Option.objects.all()))

    return render(request, 'ques.html', {'quiz': quiz, 'questions': selected_questions})

@login_required
def submit_quiz(request, quizid):
    if request.method == 'POST':
        quiz = get_object_or_404(Quiz, id=quizid)
        user = request.user

        quiz_session = QuizSession.objects.get(user=user, quiz=quiz)
        if not quiz_session:
            return redirect('test', quizid=quizid)
        
        selected_questions = quiz_session.selected_questions.all()
        score = 0

        for question in selected_questions:
            selected_option_id = request.POST.get(f'question_{question.id}')
            if selected_option_id:
                selected_option = Option.objects.get(id=selected_option_id)
                is_correct = selected_option.is_correct
                if is_correct:
                    score+=1
                UserResponse.objects.create(user=user,quiz=quiz, question=question, selected_option=selected_option, is_correct=is_correct, quiz_session=quiz_session)
                print(f"UserResponse created for Question ID: {question.text}")
                        
        request.session['last_quiz_session_id'] = quiz_session.id
    
        return redirect('results', quizid=quizid, score=score)
    
    return redirect('test', quizid=quizid)


@login_required
def results(request, quizid, score):
    quiz = get_object_or_404(Quiz, id=quizid)
    user = request.user

    quiz_session_id = request.session.get('last_quiz_session_id')
    if not quiz_session_id:
        return redirect('test', quizid=quizid)
    
    user_responses = UserResponse.objects.filter(user=user, quiz_session_id=quiz_session_id)

    for response in user_responses:
        response.correct_option = response.question.options.get(is_correct=True)

    if 'last_quiz_session_id' in request.session:
        del request.session['last_quiz_session_id']

    return render(request, 'result.html', {'quiz':quiz, 'score':score, 'user_responses': user_responses})


