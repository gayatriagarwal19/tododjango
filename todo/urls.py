from django.urls import path
from todo import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.signin , name = 'signin'),
    path('signup', views.signup , name = 'signup'),
    path('signout', views.signout, name='signout'),
    path('todos', views.todos , name = 'todos'),
    path('add', views.add, name = 'add'),
    path('add_todos', views.add_todos, name = 'add_todos'),
    path('edit/<int:id>', views.edit , name = 'edit'),
    path('delete/<int:id>',views.delete, name= 'delete'),
    path('profile_page',views.Profile, name= 'Profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
