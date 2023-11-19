from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.
# admin.site.register(Author)
class BooksInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Book
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    # "pass" will keep the original behavior
    # pass
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    # The fields attribute lists just those fields that are to be displayed on the form, in order.
    # Fields are displayed vertically by default, but will display horizontally if you further group them
    # in a tuple (as shown in the "date" fields above).
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    inlines = [BooksInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
# admin.site.register(Book)
# admin.site.register(BookInstance)
# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    # Book in your website — at the bottom you should now see
    # the book instances relating to this book (immediately below the book's genre fields):
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """Administration object for BookInstance models.
    Defines:
     - fields to be displayed in list view (list_display)
     - filters that will be displayed in sidebar (list_filter)
     - grouping of fields into sections (fieldsets)
    """
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
admin.site.register(Language)