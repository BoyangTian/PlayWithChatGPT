from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, Language

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    # pass will keep the default format which call __str__ method
    # pass
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    # The fields attribute lists just those fields that are to be displayed on the form, in order. 
    # Fields are displayed vertically by default, but will display horizontally if you further 
    # group them in a tuple (as shown in the "date" fields)
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# it can make sense to be able to add associated records at the same time. For example, 
# it may make sense to have both the book information and information about the specific copies 
# you've got on the same detail page.
# You can do this by declaring inlines, of type TabularInline (horizontal layout) or StackedInline 
# (vertical layout, just like the default model layout). You can add the BookInstance information 
# inline to our Book detail by specifying inlines in your BookAdmin
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Register the Admin classes for Book using the decorator
# @register decorator to register the models (this does exactly the same thing as the admin.site.register() syntax)
# Unfortunately we can't directly specify the genre field in list_display because it is a 
# ManyToManyField (Django prevents this because there would be a large database access "cost" in doing so).
# Instead we'll define a display_genre function to get the information as a string
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # Once you've got a lot of items in a list, it can be useful to be able to filter which 
    # items are displayed. This is done by listing fields in the list_filter attribute.
    list_filter = ('status', 'due_back')

    # You can add "sections" to group related model information within the detail form
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

# admin.site.register(Book)
# admin.site.register(Author)
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)
