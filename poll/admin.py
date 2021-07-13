from django.contrib import admin
from poll.models import Answer, Question,Choice


admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)


