from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    # support regex: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views
    # re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    
    # you can pass a dictionary containing additional options to the view (using the third un-named argument to the path() function).
    # This approach can be useful if you want to use the same view for multiple resources, and pass data to configure its behavior in each case.
    # path('myurl/<fish>', views.my_view, {'my_template_name': 'some_path'}, name='aurl'),
]