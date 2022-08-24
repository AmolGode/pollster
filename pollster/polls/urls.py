from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('homepage/',views.homepage),
    path('detail/<int:question_id>/',views.detail),
    path('result/<int:question_id>/',views.result),
    path('detail/<int:question_id>/add_vote/',views.add_vote),
]
