
from django.contrib import admin
from django.urls import path
from app1.views import home , login , signup ,signup_custom, add_todo , signout , delete_todo, change_todo,profile


urlpatterns = [
   path('' , home , name='home' ), 
   path('login/' ,login  , name='login'), 
   path('profile/' ,profile  , name='profile'), 
   path('edit/' ,profile , name='profile'), 
   path('signup/' , signup_custom ), 
   path('add-todo/' , add_todo ), 
   path('delete-todo/<int:id>' , delete_todo ), 
   path('change-status/<int:id>/<str:status>' , change_todo ), 
   path('logout/' , signout ), 
]
