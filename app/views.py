from django.shortcuts import render
from django.views import View
from app.models import Question

# Create your views here.
def main(request):
    return render(request,"main.html")

class PollQuestions(View):
    title = "Questions"
    template = 'questions.html'

    def get(self, request):
        questions = list(Question.objects.values('pk', 'question_text'))

        context = {
            'question_text': self.title,
            'D': questions,
        }

        return render(request, self.template, context)