from django.contrib import admin

# Register your models here.
from .models import Choice, Question

# in this way it tells Django "Choice" object are edited on the "Question" admin page.
# By default, provide enough fileds for 3 choices
# StackedInline will show 3 fileds one by one
# class ChoiceInline(admin.StackedInline):
# TabularInline will show a tabular way of displaying inline related objects
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# customize admin page
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        # The first element of each tuple in fieldsets is the title of the fieldset.
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    # show all field under home display place
    list_display = ["question_text", "pub_date", "was_published_recently"]
    # enable "admin" page adds a “Filter” sidebar that lets people filter the change list by the pub_date field
    list_filter = ["pub_date"]
    inlines = [ChoiceInline]
    # enable search capability
    # because it uses a LIKE query behind the scenes,
    # limiting the number of search fields to a reasonable number will make it easier
    # for your database to do the search
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)