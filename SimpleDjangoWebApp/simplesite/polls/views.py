from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question

# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]

#     # This is not the short version, below is the one which can direct set the context,
#     # In this case we even don't need to import loader and HttpResponse
#     # template = loader.get_template("polls/index.html")
#     # context = {
#     #     "latest_question_list": latest_question_list
#     # }
#     # return HttpResponse(template.render(context, request))

#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        Question.objects.filter(pub_date__lte=timezone.now()) returns a queryset containing Questions
        whose pub_date is less than or equal to - that is, earlier than or equal to - timezone.now.
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]


# def detail(request, question_id):
#     # This is not the short version, below is the one which can direct set success or 404
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, "polls/detail.html", {"question": question})
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        # race condition: https://docs.djangoproject.com/en/4.2/ref/models/expressions/#avoiding-race-conditions-using-f
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # This function helps avoid having to hardcode a URL in the view function. 
        # It is given the name of the view that we want to pass control to and the variable portion
        # of the URL pattern that points to that view.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
