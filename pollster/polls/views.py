from multiprocessing import context
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Question,Choice
from django.urls import reverse

# Create your views here.


def homepage(request):
    question_list = Question.objects.all().order_by('-pub_date')
    context = {'question_list':question_list}
    return render(request,'index.html',context)

def detail(request,question_id):
    try:
        que = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist.')
    return render(request,'detail.html',{'question':que})

def result(request,question_id):
    que = get_object_or_404(Question,id=question_id)
    return render(request,'result.html',{'question':que})


def add_vote(request,question_id):
    question = Question.objects.get(id=question_id)
    try:
        selected_choice = question.choice_set.get(id = request.POST['choice'])
    except:
        # return render(request,'detail.html',{'question':question,'error_message':"You didn't select a choice"})
        return redirect(f'/polls/detail/{question_id}')
    selected_choice.votes += 1
    selected_choice.save()
    return redirect(f'/polls/result/{question_id}')
    
