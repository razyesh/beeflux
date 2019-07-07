from django.shortcuts import render
from . import viewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'topic', viewsets.Topicviewsets)
router.register(r'question', viewsets.Questionviewsets)
router.register(r'answer', viewsets.Answerviewsets)

urlpatterns = [
    path('', include(router.urls)),
    path('api', include('rest_framework.urls', namespace= 'rest-framework'))
]