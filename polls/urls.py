from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index', ),
    # ex: /polls/5/
    path('(?P<question_id>[0-9]+)/', views.detail, name='detail'),
    # ex：/polls/5/results/
    path('(?P<question_id>[0-9]+)/results/', views.results, name='results'),
    # ex:/polls/5/vote/
    path('(?P<question_id>[0-9]+)/vote/', views.vote, name='vote'),

]
