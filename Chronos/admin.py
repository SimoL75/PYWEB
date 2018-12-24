from django.contrib import admin

from .models import User, Project, timetracking

admin.site.register(User)
admin.site.register(Project)
admin.site.register(timetracking)
# Register your models here.
