from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import RequestContext

from .models import User, Project, Affectation

def index(request):
	return render(request,'hello.html')


def timetrack(request):
    try:
        matricule = request.POST["matricule"]
        password = request.POST["password"] 
        user = User.objects.get(matricule = matricule, password = password)
    except User.DoesNotExist:
        raise Http404("Error 404")
    myAffectedProject = Affectation.objects.filter(id_user = user.id)
    # p1 = Project(nom = 'Ravel', numero = '0155')
    # p2 = Project(nom = 'Forscad', numero = '0100')
    # p1.save()
    # p2.save()
    # p1.users.add(user)
    # p2.users.add(user)
    myProjects = user.projects.all()
    print(myProjects)
    context = {"timetracking" : myProjects}
    return render(request,'index.html', context)

	#return render(index,'test.html')
    # myAffectedProject = Affectation.objects.get(id_user = user.id)
	# tt = Project.objects.all()
    

#    context = {
#            "timetracking" : tt
#    }
#
#({"my_name": "Adrian"})