from django.contrib import admin

# Register your models here.
from .models import Choice, Question

# customize admin page
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        # The first element of each tuple in fieldsets is the title of the fieldset.
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)