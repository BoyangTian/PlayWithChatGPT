"""
URL configuration for authsite project.

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
# Use static() to add URL mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

# Now let's redirect the root URL of our site (i.e. 127.0.0.1:8000) to the URL 127.0.0.1:8000/catalog/.
# This is the only app we'll be using in this project. To do this, 
# we'll use a special view function, RedirectView, which takes the new relative URL to redirect to 
# (/catalog/) as its first argument when the URL pattern specified in the path() function is matched 
# (the root URL, in this case).
urlpatterns += [
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]

# Django does not serve static files like CSS, JavaScript, and images by default, 
# but it can be useful for the development web server to do so while you're creating your site. 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
