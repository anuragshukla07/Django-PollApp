from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse ,Http404,HttpResponseRedirect
# from django.template import loader
from .models import Question,Choice
from django.urls import reverse

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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'PollApp/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'PollApp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('PollApp:results', args=(question.id,)))