from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Question, Choice

# Create your views here.

def index(request):
    return HttpResponse("You are in the polls index")

def index(request):
    #Ultimele 5 intrebari sortate pe data
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #le insiram in output cu , intre ele
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def details(request, question_id):
    return HttpResponse("You're looking at the question %s" % question_id)

def results(request, question_id):
    response = "You are looking at the response of question %s"
    return HttpResponse(response % question_id)
#But then again, this is not The Way, we need to create templates, so we
#create a "templates" folder in pols
