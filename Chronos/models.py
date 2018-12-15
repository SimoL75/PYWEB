from django.db import models

# Create your models here.
class User(models.Model):
	nom = models.CharField(max_length=64)
	prenom = models.CharField(max_length=64)
	matricule = models.CharField(max_length=64)
	password = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.id} - user {self.nom}"

class Project(models.Model):
	nom = models.CharField(max_length=64)
	numero = models.IntegerField()
	users = models.ManyToManyField(User, related_name = "projects")

	def __str__(self):
		return f" project name {self.nom} - number {self.numero}"

class Affectation(models.Model):
	id_user = models.ForeignKey(User, on_delete = models.CASCADE)
	id_project = models.ForeignKey(Project, on_delete = models.CASCADE, related_name = "affected_projects")

	def __str__(self):
		return f" project number {self.id_project} - affected to {self.id_user}"

class timetracking(models.Model):
	id_seance = models.IntegerField()
	id_week = models.IntegerField()
	id_year = models.IntegerField()
	fk_id_user = models.ForeignKey(User, on_delete = models.CASCADE)
	fk_id_project = models.ForeignKey(Project, on_delete = models.CASCADE)

	def __str__(self):
		return f" user {self.fk_id_user} timetracked project {self.fk_id_project} on plage {self.id_seance}"




# class Project(models.model):
