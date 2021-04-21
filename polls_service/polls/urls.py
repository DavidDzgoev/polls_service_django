from django.urls import path

from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('poll_<int:poll_id>/', views.poll_detail, name='poll_detail'),
    path('question_<int:question_id>/', views.question_detail, name='question_detail'),
    path('question_<int:question_id>/give_answer/', views.give_answer, name='give_answer'),
    path('question_<int:question_id>/question_results/', views.question_results, name='question_results'),
]
