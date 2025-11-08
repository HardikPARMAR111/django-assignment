from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('dashboard/', views.quiz_dashboard, name='quiz_dashboard'),
    path('results/<int:submission_id>/', views.quiz_result, name='quiz_result'),
]
