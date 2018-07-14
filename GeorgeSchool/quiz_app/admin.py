from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from quiz_app.models import User, Subject, Quiz, Question, Answer, Student, TakenQuiz, StudentAnswer
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Subject)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(TakenQuiz)
admin.site.register(StudentAnswer)
admin.site.register(Student)