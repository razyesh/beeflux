from rest_framework import serializers
from entrance.models import Topic, Question, SubTopic, Answer, QuestionSet

class Topicserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class Answerserializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class Questionserializer(serializers.ModelSerializer):
    answer = Answerserializer(many=True)
    class Meta:
        model = Question
        fields = '__all__'
    
    
