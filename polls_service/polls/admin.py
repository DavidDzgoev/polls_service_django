from django.contrib import admin

from .models import Poll, Choice, Question

admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Choice)


