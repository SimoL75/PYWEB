from django.contrib import admin

from .models import User, Project, Affectation, timetracking

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Affectation)
admin.site.register(timetracking)
# Register your models here.
