from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from .models import Question, Topic, SubTopic, QuestionSet

def entrance(request):
    return render(request, 'entrance/entrance-intro.html', {'title':'Entrance'})

class TopicListView(ListView):
    model = Topic
    context_object_name = 'topics'
    template_name = 'entrance/topic.html'

class SubTopicListView(ListView):
    model = SubTopic
    context_object_name = 'subtopics'
    template_name = 'entrance/subtopic.html'

class QuestionSetListView(ListView):
    model = QuestionSet
    context_object_name = 'questionsets'
    template_name = 'entrance/questionsets.html'

class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    template_name='entrance/question.html'

    def get_queryset(self):
        questions = Question.objects.all()
        questions = questions.filter(questionset=1)
        return questions