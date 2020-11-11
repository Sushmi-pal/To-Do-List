from django.urls import path
from .views import todolist
urlpatterns=[
    path('',todolist),
    path('/delete/<int:pk>',todolist),
    path('/update/<int:pk>',todolist),
]