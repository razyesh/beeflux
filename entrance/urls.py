from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('entrance',views.entrance, name="entrance"),
    path('entrance/topic', views.TopicListView.as_view(), name="topic"),
    path('entrance/topic/<int:id>', views.SubTopicListView.as_view(), name="subtopic"),
    path('entrance/topic/<int:id>/level', views.QuestionSetListView.as_view(), name="questionsets"),
    path('entrance/topic/level/<int:id>', views.QuestionListView.as_view(), name="questions"),
]