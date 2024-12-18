from django.shortcuts import render, redirect
from .models import Quiz, Question, Session,Answers
from django.http import JsonResponse, HttpResponseBadRequest

# Create your views here.

def home(request):
    return render(request, "home.html")

def quiz(request):
    test = Quiz.objects.all()
    return render(request, "quiz.html", {"quizzes": test})

def ques(request, quizid):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    quiz = Quiz.objects.get(id=quizid)
    session = Session.objects.create(userid=user, quizid=quiz)
    session.save()

    questions = Question.objects.filter(quizid=quizid).order_by('?')[:quiz.numofques]
    

    if request.method == 'POST':
        sess = request.POST.get("sessionid")

        for question in questions:
            question_id = request.POST.get("quesid")
            answer = request.POST.get("answer")
            

            session = Session.objects.get(id=sess)
            question = Question.objects.get(id=question_id)

            # session_answers = request.session.get('session_answers', [])

            # if 'session_answers' not in request.session or request.session.get('current_quiz') != quizid:
            #     request.session['session_answers'] = []
            #     request.session['current_quiz'] = quizid
            
        
            if question.ans == answer:
                session.correct_ans +=1
                session.total_marks += question.marks
            else:
                session.incorrect_ans +=1
            
            session.save()

            answers= Answers.objects.create(sessionid=session, ques=question.ques, user_ans= answer, corr_ans=question.ans)
            answers.save()

        return redirect('result', sessionid=session.id)

        # return redirect('result')

        # session_answers = request.session.get('session_answers', [])
        # session_answers.append({
        #     'question': question.ques,
        #     'user_ans': answer,
        #     'correct_ans': question.ans,
        # })
        # request.session['session_answers'] = session_answers
    else:

        return render(request, "ques.html", {"questions":questions, "sessionid":session.id, "quiz":quiz})


   



def result(request, sessionid):
    
    session= Session.objects.get(id=sessionid)
    answers = Answers.objects.filter(sessionid=sessionid)
    data = {
        'session': session,
        'answers':answers,
    }
    return render(request, "result.html", data)


