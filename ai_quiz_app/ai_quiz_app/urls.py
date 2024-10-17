# ai_quiz_app/urls.py

from django.contrib import admin
from django.urls import path
from quiz.views import quiz_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', quiz_view, name='quiz'),
]