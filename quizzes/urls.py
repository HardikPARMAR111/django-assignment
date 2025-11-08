from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('dashboard/', views.quiz_dashboard, name='quiz_dashboard'),
    path('<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('<int:quiz_id>/submit/', views.submit_quiz, name='submit_quiz'),
    path('result/<int:submission_id>/', views.quiz_result, name='quiz_result'),
]