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

    print(username)
    print(password)

    #TÄHÄN MUKAAN VARSINAINEN LOGIN-TOIMINNALLISUUS
    #loggedin = 


    person = Person.objects.get(username=username)

    tasks = Task.objects.filter(owner=person)

    return render(request, 'taskmanager/taskhome.html', {'person': person, 'tasks': tasks })
    

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
    
    print(title)
    print(content)
    print(person.pk)

    #muuta tämä sql-queryksi --> injection vulnerability
    new_task = Task.objects.create(owner=person, title=title, content=content)
    new_task.save()

    tasks = Task.objects.filter(owner=person)

    return render(request, 'taskmanager/taskhome.html', {'person': person, 'tasks': tasks })
    #return redirect('/taskmanager/user')