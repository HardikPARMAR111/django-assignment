from django.urls import path
from . import views

#all the urls for quiz
urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/submit/', views.submit_quiz, name='submit_quiz'),
    path('result/<int:submission_id>/', views.quiz_result, name='quiz_result'),
     path('dashboard/', views.quiz_dashboard, name='quiz_dashboard'),



]
