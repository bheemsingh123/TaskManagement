from django.urls import path  
from task_app import views  
 
urlpatterns = [  
    path('',views.home),
    
    # user
    path('login/',views.login_user),
    path('logout_user/',views.logout_user),
    path('register/',views.register),
    path('profile/',views.profile),

    # task
    path('create_task/', views.create_task, name='create_task'),
    path('delete/<int:taskid>', views.delete_task, name='delete'),
    path('edit/<int:taskid>', views.edit_task, name='edit'),


] 