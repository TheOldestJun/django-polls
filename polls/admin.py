from django.contrib import admin
from . import models

admin.site.register(models.Question, list_display=['question_text', 'pub_date', 'was_published_recently'])
admin.site.register(models.Choice, list_display=['question', 'choice_text', 'votes'])

