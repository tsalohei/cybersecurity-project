from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), #taskmanager
    path('loginform/', views.loginFormView, name='loginform'), #taskmanager/loginform    
    path('userform/', views.userForm, name='userform'),
    path('userform/newuser/', views.addUserView, name='newuser'),
    path('user/', views.userView, name='user-view'),    
    path('user/<username>', views.homeView, name='home-view'),
    path('user/addtask/', views.addTaskView, name='addtask'),
    path('logout/', views.logoutView, name='logout'),
    path('woops/', views.woopsView, name='woops'),
    path('info/', views.infoView, name='info-view'),
    path('info/<username>', views.personalView, name='personal-view')

]