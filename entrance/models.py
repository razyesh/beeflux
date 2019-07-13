from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class SubTopic(models.Model):
    title = models.ForeignKey(Topic, related_name='subtopic', on_delete=models.CASCADE)
    sub_title = models.CharField(max_length=20)
    def __str__(self):
        return self.sub_title


class QuestionSet(models.Model):
    title = models.ForeignKey(Topic, related_name='questionset', on_delete=models.PROTECT)
    sub_title = models.ForeignKey(SubTopic, related_name='questionset', on_delete= models.PROTECT)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Question(models.Model):
    questionset = models.ForeignKey(QuestionSet, related_name='question', on_delete=models.PROTECT)
    question = models.CharField(max_length=100)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answer', on_delete= models.CASCADE)
    answer = models.CharField(max_length=30)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer