from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Question, Choice
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# Create your views here.
'''
def index(request):
    return HttpResponse("You are in the polls index")

def index(request):
    #Ultimele 5 intrebari sortate pe data
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #le insiram in output cu , intre ele
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question' : question})

def result(request, question_id):
    #response = "You are looking at the response of question %s"
    #return HttpResponse(response % question_id)
#But then again, this is not The Way, we need to create templates, so we
#create a "templates" folder in pols
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question' : question})
'''
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question' : question,
            'error_message' : 'You did not select a choice',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))

#We replace index, result and details

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        #return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailsView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'

