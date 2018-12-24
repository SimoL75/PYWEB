from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpRequest
from django.template import RequestContext
from datetime import date, timedelta, datetime
from .models import User, Project, timetracking
import json

def index(request):
	return render(request,'hello.html')


def timetrack(request):
    try:
        # matricule = request.POST["matricule"]
        # password = request.POST["password"]
        matricule = "X124106"
        password = "1234" 
        user = User.objects.get(matricule = matricule, password = password)
    except User.DoesNotExist:
        raise Http404("Error 404")

    myDay = datetime.now()
    myMonth = datetime.today().strftime('%m - %Y')
    myWeek = myDay.isocalendar()[1]
    
    palette = ["#e60028","#cac843","#9e6aad","#f34400","#003962"]
    myProjects = user.projects.all()
    myTimetrackedProjects = user.timetracked_projects.all()
    context = {"my_Projects" : myProjects, 
    			"timetracked_projects" : myTimetrackedProjects,
    			"my_colors" : palette,
              "myMonth" : myMonth,
              "days_of_week" : foo(2018,myWeek)}
    return render(request,'index.html', context)

def saveTask(request):
	# if HttpRequest.is_ajax():
	print('moimoi')
	print(request.data)
		#print(Drag_Drop_event)
	
	return render(request,'index.html')
    	#print(Drag_Drop_event)



def foo(year, week):
    d = date(year,1,1)
    d = d - timedelta(d.weekday())
    dlt = timedelta(days = (week-1)*7)
    
    Monday = d + dlt
    Mon = Monday.strftime('%d')
    
    Tuesday = Monday + timedelta(days=1)
    Tue = Tuesday.strftime('%d')
    
    Wednesday = Tuesday + timedelta(days=1)
    Wed = Wednesday.strftime('%d')
    
    Thursday = Wednesday + timedelta(days=1)
    Thu = Thursday.strftime('%d')
    
    Friday = Thursday + timedelta(days=1)
    Fri = Friday.strftime('%d')

    Saturday = Friday + timedelta(days=1)
    Sat = Saturday.strftime('%d')
    
    Sunday = Saturday + timedelta(days=1)
    Sun = Sunday.strftime('%d')

    myWeekCalendar = {'Mon': Mon,'Tue' :Tue,'Wed' :Wed, 'Thu' : Thu, 'Fri': Fri, 'Sat' : Sat, 'Sun' : Sun}
#

    return myWeekCalendar


	# id_seance = models.IntegerField()
	# id_week = models.IntegerField()
	# id_year = models.IntegerField()
	# fk_id_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "timetracked_projects")
	# fk_id_project = models.ForeignKey(Project, on_delete = models.CASCADE)    

	#return render(index,'test.html')
    # myAffectedProject = Affectation.objects.get(id_user = user.id)
	# tt = Project.objects.all()
#    myAffectedProject = Affectation.objects.filter(id_user = user.id)
    # p1 = Project(nom = 'Paloma', numero = '0163')
    # p2 = Project(nom = 'Forscad', numero = '0100')
#    p1.save()
    # p2.save()
#    p1.users.add(user)
    # p2.users.add(user)
    # p1 = Project.objects.get(nom = 'Paloma', numero = '0163')
    # p2 = Project.objects.get(nom = 'Forscad', numero = '0100')
    # t1 = timetracking(id_seance = 11, id_week = 50, id_year = 2018, fk_id_user = user, fk_id_project = p1)
    # t2 = timetracking(id_seance = 12, id_week = 50, id_year = 2018, fk_id_user = user, fk_id_project = p1)
    # t3 = timetracking(id_seance = 13, id_week = 50, id_year = 2018, fk_id_user = user, fk_id_project = p2)
    # t4 = timetracking(id_seance = 14, id_week = 50, id_year = 2018, fk_id_user = user, fk_id_project = p2)
    # t1.save()
    # t2.save()
    # t3.save()
    # t4.save()