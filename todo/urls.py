from django.urls import path
from todo import views

urlpatterns = [
    path('', views.signin , name = 'signin'),
    path('signup', views.signup , name = 'signup'),
    path('signout', views.signout, name='signout'),
    path('todos', views.todos , name = 'todos'),
    path('add', views.add, name = 'add'),
    path('add_todos', views.add_todos, name = 'add_todos'),
    path('edit/<int:id>', views.edit , name = 'edit'),
    path('delete/<int:id>',views.delete, name= 'delete'),
    # path('profile_page',views.profile_page, name= 'profile_page'),
]