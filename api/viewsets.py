from rest_framework import viewsets
from .serializers import Topicserializer, Questionserializer, Answerserializer
from entrance.models import Topic, Question, Answer


class Topicviewsets(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = Topicserializer

class Questionviewsets(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = Questionserializer

class Answerviewsets(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = Answerserializer