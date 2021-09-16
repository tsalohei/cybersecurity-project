from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), #taskmanager
    path('loginform/', views.loginFormView, name='loginform'), #taskmanager/loginform
    
    path('userform/', views.userForm, name='userform'),
    path('userform/newuser/', views.addUserView, name='newuser'),

    path('user/', views.userView, name='user-view'),    

    path('user/addtask/', views.addTaskView, name='addtask'),

    #logout

    #olisiko tällainen hyvä olla?
    #path('users/<username>', views.someView, name='some-view')
    #admin 'admin'
]