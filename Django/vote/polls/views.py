from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice,Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #常规写法
    '''
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list,
    }
    #output = ','.join([q.question_text for q in latest_question_list])
    return HttpResponse(template.render(context,request))
    '''
    #推荐写法,需要导入render
    context = {'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)


def detail(request,question_id):
    #平常写法
    '''
    try:
        question = Question.objects.get(pk=question_id)
    except:
        #使用404方法友好输出
        raise Http404("Question does not exists")
    return render(request,'polls/detail.html',{'question':question})
    '''
    #简写方法
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})



def results(request,question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})


def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
    #return HttpResponse("You're voting on question %s." % question_id)


#genetic view
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five"""
        #return Question.objects.order_by('-pub_date')[:5]
        #return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        return Question.objects.filter(pub_date__lte=timezone.now())


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'