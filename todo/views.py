from random import choices
from turtle import title
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from todo.forms import todoForm
from todo.models import todo, profile
from django.contrib.auth import authenticate, login , logout

# Create your views here.
def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate( username = username , password = password1 )

        if user is not None:
            login(request, user)
            return redirect('todos')

        else:
            messages.error(request, "Bad credentials")
            return redirect('signin')
    else:
        return render(request , 'signin.html')



def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        photo = request.FILES.get('photo')
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        number = request.POST['number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.warning(request, "Username already exists")
                return redirect(signup)
            elif User.objects.filter(email = email).exists():
                messages.warning(request, "Email already used")
                return redirect(signup)
            else:
                myuser = User.objects.create_user(username = username, email = email ,password = password1)
                myuser.first_name = fname
                myuser.last_name = lname
                user = myuser.save()
                myuser_profile = profile.objects.create(user= myuser, ProfilePhoto = photo, PhoneNumber = number)
                
                myuser_profile.save() 
                # user_profile.user = user
                # user_profile.save()

                messages.success(request, "Your account has been successfully created")

                return render(request, 'signin.html')
        
        else:
            messages.warning(request, "Password incorrect")
            return redirect(signup)
    else:
        return render(request , 'signup.html')


def signout(request):
    logout(request)
    messages.success(request, 'logged out successfully!')
    return render(request, 'signin.html')

def todos(request):
    if request.user.is_authenticated:
        user = request.user
        todos = todo.objects.filter(user = user)
        return render(request, 'todos.html', context={'todos': todos})

def add(request):
    form = todoForm()
    return render(request, 'add.html', context={'form': form})

def add_todos(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)

        title = request.POST['title']
        description = request.POST['description']
        status = request.POST['status']
        todos = todo.objects.create(title = title, description = description, status = status)
        todos.user = user
        todos.save()
        print(todos)
        return redirect("todos")
    else:
        return render(request, 'add.html')

    

def edit(request, id):
    todos = todo.objects.get(pk = id)  
    if request.method == 'POST':
        todos.title = request.POST['title']
        todos.description = request.POST['description']
        todos.status = request.POST['status']
        todos.save();
        return redirect('todos')
    context = {
    'todo' : todos,
    'title': todos.title,
    'description':todos.description,
    'status': todos.status,
    }
    print(todos.status)
    return render(request, 'edit.html', context)



def delete(request, id):
    todo.objects.get(pk = id).delete()
    return redirect('todos')


def Profile(request):
    context = {
        'profile' : profile.objects.filter(user = request.user)
    }
    print(profile.objects.all)
    return render(request, 'profile.html', context)