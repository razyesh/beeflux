from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from .models import Question, Topic, SubTopic, QuestionSet, Answer

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

    def get_queryset(self):
        subtopics = SubTopic.objects.all()
        subtopics = subtopics.filter(title=self.kwargs['id'])
        return subtopics

class QuestionSetListView(ListView):
    model = QuestionSet
    context_object_name = 'questionsets'
    template_name = 'entrance/questionsets.html'

    def get_queryset(self):
        questionsets = QuestionSet.objects.all()
        questionsets = questionsets.filter(sub_title=self.kwargs['id'])
        return questionsets


class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    template_name='entrance/question.html'

    def get_queryset(self):
        questions = Question.objects.all()
        questions = questions.filter(questionset=self.kwargs['id'])
        return questions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answers'] = Answer.objects.all()
        return context

    