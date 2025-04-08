from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('ask/', views.ask_question, name='ask_question'),
    path('signup/', views.signup_view, name='signup'),
    path('like/<int:pk>/', views.like_question, name='like_question'),
]