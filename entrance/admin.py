from django.contrib import admin

# Register your models here.
from .models import Topic, SubTopic, Question, Answer, QuestionSet
class QuestionsetAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'sub_title', 'name')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','questionset', 'question')

admin.site.register(Topic)
admin.site.register(SubTopic)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(QuestionSet,QuestionsetAdmin)

