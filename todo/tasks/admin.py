from django.contrib import admin


from .models import task, Subtask, User

admin.site.register(task)
admin.site.register(Subtask)
admin.site.register(User)
# Register your models here.
