from queue import Full
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from django.core.mail import EmailMessage
from  rest_framework import viewsets # type: ignore
from .models import Project
from .forms import ProjectForm
from .serializers import ProjectSerializer
# Create your views here.

def index(request):
    return render(request, "index.html", {})
    

def sing_in(request):

    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        user = User.objects.filter(email=email).first()
        if user:
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                login(request, auth_user)
                return redirect('dashboard')
            else:
                print("mot de pass incorrecte")
        else:
            print("User does not exist")

    return render(request, 'login.html', {})


def sing_up(request):
    error = False
    message = ""
    if request.method == "POST":
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)
        # Email
        try:
            validate_email(email)
        except:
            error = True
            message = "Enter un email valide svp!"
        # password
        if error == False:
            if password != repassword:
                error = True
                message = "Les deux mot de passe ne correspondent pas!"
        # Exist
        user = User.objects.filter(Q(email=email) | Q(username=name)).first()
        if user:
            error = True
            message = f"Un utilisateur avec email {email} ou le nom d'utilisateur {name} exist déjà'!"
        
        # register
        if error == False:
            user = User(
                username = name,
                email = email,
            )
            user.save()

            user.password = password
            user.set_password(user.password)
            user.save()

            return redirect('sing_in')

            #print("=="*5, " NEW POST: ",name,email, password, repassword, "=="*5)

    context = {
        'error':error,
        'message':message
    }
    return render(request, 'register.html', context)


@login_required(login_url='sing_in')
def dashboard(request):
    return render(request, 'admin.html', {})



def invest(request):
    return render(request, "ajout.html", {})

def update_profil(request):
    return render(request, "profile.html", {})

def log_out(request):
    logout(request)
    return redirect('sing_in')




def forgot_password(request):
    error = False
    success = False
    message = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            print("processing forgot password")
            html = """
                <p> Hello, merci de cliquer pour modifier votre email </p>
            """

            msg = EmailMessage(
                "Modification de mot de pass!",
                html,
                "soroib0879@gmail.com",
                ["soro4827@gmail.com"],
            )

            msg.content_subtype = 'html'
            msg.send()
            
            message = "processing forgot password"
            success = True
        else:
            print("user does not exist")
            error = True
            message = "user does not exist"
    
    context = {
        'success': success,
        'error':error,
        'message':message
    }
    return render(request, "forgot_password.html", context)


def update_password(request):
    return render(request, "update_password.html", {})


class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()
    
    return render(request, 'ajout.html', {'form': form})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})
        
        
        

