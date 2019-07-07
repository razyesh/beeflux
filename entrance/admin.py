from django.contrib import admin

# Register your models here.
from .models import Topic, SubTopic, Question, Answer, QuestionSet

admin.site.register(Topic)
admin.site.register(SubTopic)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionSet)

