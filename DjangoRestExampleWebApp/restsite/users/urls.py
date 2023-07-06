from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

user_list = views.UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('users/',
        # views.UserList.as_view(),
        user_list,
        name='user-list'),
    # TODO: need to understand the relationship between this and router
    # path('users/', views.UserList.as_view()),
    path('users/<int:pk>/',
        # views.UserDetail.as_view(),
        user_detail,
        name='user-detail'),
]


# This way we can control request and response type
# https://www.django-rest-framework.org/tutorial/2-requests-and-responses/
urlpatterns = format_suffix_patterns(urlpatterns)