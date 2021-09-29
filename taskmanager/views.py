from django.shortcuts import render, redirect


# Create your views here.

from django.http import HttpResponse
from django.template import loader
from taskmanager.models import Person, Task
from django.db import connection,transaction

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
            return redirect('/taskmanager/woops')
    except:
        print('who are you?')
        return redirect('/taskmanager/woops')

def homeView(request, username):
    try:
        person = Person.objects.get(username=username)
        if (person.loggedin == 'True'):
            tasks = Task.objects.filter(owner=person)
            return render(request, 'taskmanager/taskhome.html', {'person': person, 'tasks': tasks })
        else:
            return redirect('/taskmanager/woops')
    except: 
        return redirect('/taskmanager/woops')

def userForm(request):
    return render(request, 'taskmanager/newuser.html')   

def addUserView(request):
    username = request.POST.get('username')
    try:
        duplicate_username = Person.objects.get(username=username)
        return redirect('/taskmanager/woops')
    except:    
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        new_person = Person.objects.create(username=username, password=password, firstname=firstname, lastname=lastname)
        new_person.save()
        return render(request, 'taskmanager/registrationok.html')

def addTaskView(request):
    username = request.POST.get('owner')
    person = Person.objects.get(username=username)

    title = request.POST.get('title')
    content = request.POST.get('content')

    #flaw: injection
    #new_task = Task.objects.create(owner=person, title=title, content=content)
    #new_task.save()

    query = "INSERT INTO taskmanager_task (owner_id, title, content) \
        values (" + str(person.pk) + ", '" + title + "', '" + content + "')"

    cursor = connection.cursor()    
    cursor.execute(query)    
    transaction.commit()

    tasks = Task.objects.filter(owner=person)

    return render(request, 'taskmanager/taskhome.html', {'person': person, 'tasks': tasks })

def logoutView(request):
    username = request.POST.get('owner')
    person = Person.objects.get(username=username)

    person.loggedin = 'False'
    person.save()

    return redirect('index')

def woopsView(request):
    return render(request, 'taskmanager/woops.html')


def infoView(request):
    username = request.GET.get('username')

    return redirect('/taskmanager/info/' + username)

def personalView(request, username):
    try:
        person = Person.objects.get(username=username)
        return render(request, 'taskmanager/info.html', {'person': person})
    except:
        return render(request, 'taskmanager/woops.html')