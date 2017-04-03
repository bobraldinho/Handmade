from django.contrib import admin

from .models import FaqQuestion, FaqAnswer

admin.site.register(FaqQuestion)
admin.site.register(FaqAnswer)
