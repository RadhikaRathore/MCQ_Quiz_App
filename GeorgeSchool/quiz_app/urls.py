from django.contrib import admin
from django.urls import path, include
from .views import quiz_app, students



urlpatterns = [

	path('', quiz_app.home, name='home'),

    path('students/', include(([
    	
        path('', students.QuizListView.as_view(), name='quiz_list'),
        path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
        path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
    ], 'quiz_app'), namespace='students')),



]