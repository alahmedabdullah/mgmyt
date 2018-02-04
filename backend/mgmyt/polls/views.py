#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import authenticate, login
from .models import Question  #2index


#from django.template import loader #3index

#from django.shortcuts import render  #4index

#from django.http import Http404   #2detail

from django.shortcuts import get_object_or_404, render #3detail

#from django.http import HttpResponseRedirect, HttpResponse #2vote

from django.core.urlresolvers import reverse #2vote
from django.http import HttpResponseRedirect #LESS_CODE_IS_BETTER
from django.views import generic             #LESS_CODE_IS_BETTER

import logging
logger = logging.getLogger(__name__)
print __name__

#======================================================================
#                         INDEX 
#======================================================================
#1-------------
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

#2-------------
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([p.question_text for p in latest_question_list])
#     return HttpResponse(output)

#3-------------
# def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context, request))

#4-------------
@login_required
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    logger.debug('%s' %context)
    return render(request, 'polls/index.html', context)

#LESS_CODE_IS_BETTER----------------
#class IndexView(generic.ListView):
#    template_name = 'polls/index.html'
#    context_object_name = 'latest_question_list'
#
#    def get_queryset(self):
#        """Return the last five published questions."""
#        return Question.objects.order_by('-pub_date')[:5]

#======================================================================
#                         DETAIL 
#======================================================================
#1-------------
# def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)

#2-------------
# def detail(request, question_id):
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#    return render(request, 'polls/detail.html', {'question': question})

#3-------------
@login_required
def detail(request, question_id):
     question = get_object_or_404(Question, pk=question_id)
     return render(request, 'polls/detail.html', {'question': question})

#LESS_CODE_IS_BETTER----------------
#class DetailView(generic.DetailView):
#    model = Question
#    template_name = 'polls/detail.html'
#======================================================================
#                         RESULTS 
#======================================================================
#1--------------
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

#2-------------
@login_required
def results(request, question_id):
     question = get_object_or_404(Question, pk=question_id)
     return render(request, 'polls/results.html', {'question': question})

#LESS_CODE_IS_BAETTER----------------

#class ResultsView(generic.DetailView):
#    model = Question
#    template_name = 'polls/results.html'

#======================================================================
#                         VOTE 
#======================================================================
#1------------------
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

#2-----------------
@login_required
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
