from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Choice, Question, Poll, Answer


def index(request):
    polls_list = Poll.objects.all()
    return render(request, 'polls/index.html', {'polls_list': polls_list})


def poll_detail(request, poll_id):
    questions_list = Question.objects.filter(poll=poll_id)
    return render(request, 'polls/poll_detail.html', {'questions_list': questions_list})


def question_detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/question_detail.html', {'question': question})


def give_answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except KeyError:
        # Redisplay the question voting form.
        return render(request, 'polls/question_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:question_results', args=(question.id,)))


def question_results(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/question_results.html', {'question': question})
