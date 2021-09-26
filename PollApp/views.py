from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse ,Http404
# from django.template import loader
from .models import Question

def index(request):
    latestQuestionList = Question.objects.order_by('pub_date')[:5]
    # template = loader.get_template('PollApp/index.html')
    context = {
        'latestQuestionList': latestQuestionList}
    return render(request,'PollApp/index.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'PollApp/detail.html', {'question':question})

def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)