from django.urls import path

from . import views

# Since we move the "template" folder out the current folder, we need to change html path
app_name = "catalog"

# regex find path can achieve by "re_path" method:
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views

urlpatterns = [
    path("", views.index, name="index"),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]