"""
URL configuration for restsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from . import views as root_views
from handlers import views as handler_views
from users import views as user_views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'users', user_views.UserViewSet)
# router.register(r'groups', user_views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', root_views.api_root),
    # path('tasks/',
    #     handler_views.TaskList.as_view(),
    #     name='task-list'),
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    # login and logout views for the browsable API.
    # this url can be whatever you like
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('handlers.urls')),
    path('', include('users.urls')),
]
