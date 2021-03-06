from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.db.models import F, Count
from django.utils import timezone

from .models import Choice, Question


class IndexView(generic.ListView):
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.annotate(choices_count = Count('choice')).filter(
            choices_count__gt = 0, pub_date__lte = timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    def get_queryset(self):
        """
        Excludes questions from the future.
        """
        return Question.objects.annotate(choices_count = Count('choice')).filter(
            choices_count__gt = 0, pub_date__lte = timezone.now()
        )


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': quesiton,
            'error_message': 'You did not select a choice'
        })
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
