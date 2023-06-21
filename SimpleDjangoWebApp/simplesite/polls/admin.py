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
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)