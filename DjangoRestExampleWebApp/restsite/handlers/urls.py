from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
    # path('tasks/', views.task_list),
    # path('tasks/<int:pk>/', views.task_detail),
]

# This way we can control request and response type
# https://www.django-rest-framework.org/tutorial/2-requests-and-responses/
urlpatterns = format_suffix_patterns(urlpatterns)