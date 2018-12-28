from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name = "index"),
	path("timetrack", views.timetrack, name = "timetrack"),
	path("saveTask", views.saveTask, name = "saveTask"),
	path("deleteTask", views.deleteTask, name = "deleteTask"),
	path("previous", views.previous, name = "previous"),
	path("next", views.next, name = "next"),
]