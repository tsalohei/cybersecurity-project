from django.shortcuts import render, redirect


# Create your views here.

from django.http import HttpResponse
from django.template import loader
from taskmanager.models import Person, Task
#from django.views.decorators.csrf import requires_csrf_token
#from django.views.decorators.csrf import csrf_protect


def index(request):
    template = loader.get_template('taskmanager/index.html')
    return HttpResponse(template.render())
    

def loginFormView(request):
    return render(request, 'taskmanager/login.html')

def userView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
        person = Person.objects.get(username=username)
        if person.password == password:
            person.loggedin = 'True'
            person.save()

            return redirect('/taskmanager/user/' + username)
        else: 
            print('wrong password')
            return redirect('/taskmanager')
    except:
        print('who are you?')
        return redirect('/taskmanager')

def homeView(request, username):
    try:
        person = Person.objects.get(username=username)
        if (person.loggedin == 'True'):
            tasks = Task.objects.filter(owner=person)
            return render(request, 'taskmanager/taskhome.html', {'person': person, 'tasks': tasks })
        else:
            #joku järkevämpi redirect
            return redirect('/taskmanager')
    except: 
        #joku järkevämpi redirect
        return redirect('/taskmanager')

def userForm(request):
    return render(request, 'taskmanager/newuser.html')   

def addUserView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')

    #TO-DO:
    #if username exists already, don't save it

    new_person = Person.objects.create(username=username, password=password, firstname=firstname, lastname=lastname)
    new_person.save()

    return render(request, 'taskmanager/registrationok.html')

def addTaskView(request):
    username = request.POST.get('owner')
    person = Person.objects.get(username=username)

    title = request.POST.get('title')
    content = request.POST.get('content')

    #muuta tämä sql-queryksi --> injection vulnerability
    new_task = Task.objects.create(owner=person, title=title, content=content)
    new_task.save()

    tasks = Task.objects.filter(owner=person)

    return render(request, 'taskmanager/taskhome.html', {'person': person, 'tasks': tasks })

def logoutView(request):
    username = request.POST.get('owner')
    person = Person.objects.get(username=username)

    person.loggedin = 'False'
    person.save()

    return redirect('index')