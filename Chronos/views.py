from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpRequest
from django.template import RequestContext
from datetime import date, timedelta, datetime
from .models import User, Project, timetracking
from django.contrib.auth import authenticate, login, logout
import random

def index(request):   
	return render(request,'hello.html')


def timetrack(request):

    if 'user' not in request.session:

        try:
            matricule = request.POST["matricule"]
            password = request.POST["password"]
            matricule = "X124106"
            password = "1234" 
            user = User.objects.get(matricule = matricule, password = password)

        except User.DoesNotExist:
            raise Http404("Error 404")
            
        request.session['user'] = user.id
        request.session['day'] = datetime.now().strftime('%d/%m/%Y')
        request.session['week'] = datetime.now().isocalendar()[1]
    else:
        user = User.objects.get(id = request.session.get('user'))
    
    myMonth = datetime.strptime(request.session['day'],  '%d/%m/%Y').strftime('%m - %Y')
    myWeek = request.session['week']
    myYear = int(datetime.strptime(request.session['day'], '%d/%m/%Y').strftime('%Y'))

##    request.session['day'] = datetime.now()
#    request.session['week'] = request.session.get('day').isocalendar()[1]
    
    myProjects = user.projects.all()
    dic = {}
    for o in myProjects:
    #for idx, val in enumerate(myProjects):
        item = {o:"#{:06x}".format(random.randint(0,0xFFFFFF))}
        dic.update(item)
    myTimetrackedProjects = user.timetracked_projects.filter(id_week = request.session.get('week'))
    #palette = {1: "#003962",2 :"#cac843",3 :"#9e6aad", 4 : "#f34400"}
    palette = ["#003962","#cac843","#9e6aad","#f34400", "#f34400"]
    context = {"my_Projects" : dic, 
    			"timetracked_projects" : myTimetrackedProjects,
    			"my_colors" : palette,
              "myMonth" : myMonth,
              "days_of_week" : myWeekDays(myYear,myWeek)}


    return render(request,'indexxx.html', context)

def saveTask(request):
    if request.method == 'POST':
        idProject = request.POST['idProject']
        idPlage = request.POST['idPlage']
        timetrackedProject =  Project.objects.get(id = idProject)
        user = User.objects.get(id = request.session.get('user'))
        myDay = datetime.now()
        myWeek = request.session.get('week')
        new_entry = timetracking.objects.create(id_seance=idPlage,id_week=myWeek,id_year=2018,fk_id_user=user,fk_id_project=timetrackedProject)
        new_entry.save()

    return render(request,'index.html')

def deleteTask(request):
    if request.method == 'POST':
        user = User.objects.get(id = request.session.get('user'))
        idPlage = request.POST['idPlage']
        myDay = datetime.now()
        myWeek = request.session.get('week')        
        myTimetrackedProjects = user.timetracked_projects.get(id_seance=idPlage,id_week=myWeek,id_year=2018)
        myTimetrackedProjects.delete()

    return render(request,'index.html')

def previous(request):
    if request.method == 'POST':
        user = User.objects.get(id = request.session.get('user'))

        myDay =  datetime.strptime(request.session['day'],  '%d/%m/%Y')
        myDay = myDay - timedelta(days = 7)
        request.session['day'] = myDay.strftime('%d/%m/%Y')
        request.session['week']  = myDay.isocalendar()[1]

        myMonth = myDay.strftime('%m - %Y')
        myWeek =  request.session['week']
        myYear = int(datetime.strptime(request.session['day'], '%d/%m/%Y').strftime('%Y'))
    
        myProjects = user.projects.all()
        dic = {}
        for o in myProjects:
            item = {o:"#{:06x}".format(random.randint(0,0xFFFFFF))}
            dic.update(item)       
        myTimetrackedProjects = user.timetracked_projects.filter(id_week = myWeek,id_year = myYear)
        
        print(request.session.get('week'))
        
        palette = {1: "#003962",2 :"#cac843",3 :"#9e6aad", 4 : "#f34400"}
        context = {"my_Projects" : dic, 
        			"timetracked_projects" : myTimetrackedProjects,
        			"my_colors" : palette,
                  "myMonth" : myMonth,
                  "days_of_week" : myWeekDays(myYear,myWeek)}
    
    
        return render(request,'index.html', context)


def next(request):
    
    if request.method == 'POST':

        user = User.objects.get(id = request.session.get('user'))
        myDay =  datetime.strptime(request.session['day'],  '%d/%m/%Y')
        myDay = myDay + timedelta(days = 7)
        request.session['day'] = myDay.strftime('%d/%m/%Y')
        request.session['week']  = myDay.isocalendar()[1]
        myMonth = myDay.strftime('%m - %Y')
        myWeek =  request.session['week']
        myYear = int(datetime.strptime(request.session['day'], '%d/%m/%Y').strftime('%Y'))

    
        myProjects = user.projects.all()
        dic = {}
        for o in myProjects:
            item = {o:"#{:06x}".format(random.randint(0,0xFFFFFF))}
            dic.update(item)        
        myTimetrackedProjects = user.timetracked_projects.filter(id_week = myWeek, id_year = myYear)
        
        
        palette = {1: "#003962",2 :"#cac843",3 :"#9e6aad", 4 : "#f34400"}
        #palette = ["#003962","#cac843","#9e6aad","#f34400"]

        context = {"my_Projects" : dic, 
        			"timetracked_projects" : myTimetrackedProjects,
        			"my_colors" : palette,
                  "myMonth" : myMonth,
                  "days_of_week" : myWeekDays(myYear,myWeek)}
    
    
        return render(request,'index.html', context)


def myWeekDays(year, week):
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