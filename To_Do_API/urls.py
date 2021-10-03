from django.urls import path
from .views import (
    TaskViews,GetTaskViews, UpdateTaskViews,DeleteTaskViews
)

urlpatterns =[
    path('create-task/', TaskViews.as_view(), name="create"),
    path('get-task/', GetTaskViews.as_view(), name="get-task"),
    path('update-task/<int:pk>/', UpdateTaskViews.as_view(), name="update-task"),
    path('delete-task/<int:pk>/', DeleteTaskViews.as_view(), name="delete-task"),
]