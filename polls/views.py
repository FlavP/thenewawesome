from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Question, Choice

# Create your views here.
'''
def index(request):
    return HttpResponse("You are in the polls index")

def some_else(request):
    return HttpResponse("You are one step deeper")
'''
'''
def index(request):
    #Ultimele 5 intrebari sortate pe data
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #le insiram in output cu , intre ele
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
But then again, this is not The Way, we need to create templates, so we
create a "templates" folder in pols
'''