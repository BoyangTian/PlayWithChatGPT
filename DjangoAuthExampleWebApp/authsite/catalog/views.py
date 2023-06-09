from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }
    
    # Render the HTML template index.html with the data in the context variable
    # Since we move the "template" folder out the current folder, we need to change html path
    # return render(request, 'index.html', context=context)
    return render(request, 'catalog/index.html', context=context)

class BookListView(generic.ListView):
    # Only this one line under "generic.ListView" will query the database to get all records for the 
    # specified model (Book) then render a template located at book_list.html
    # the generic views look for templates in /application_name/the_model_name_list.html 
    # (catalog/book_list.html in this case) inside the application's /application_name/templates/ 
    # directory (/catalog/templates/). You can overwrite by "template_name" attribute
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html' 
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    queryset = Book.objects.all()

    paginate_by = 2

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context

class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book
    # this is the object name pass to html file
    # context_object_name = 'book-detail'
    template_name = 'catalog/book_detail.html' 

    paginate_by = 2

    # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
    # You can also specify an alternative location to redirect the user to if they are 
    # not authenticated (login_url), and a URL parameter name instead of "next" to insert 
    # the current absolute path (redirect_field_name).
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'


