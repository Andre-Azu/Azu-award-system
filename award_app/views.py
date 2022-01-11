from django.shortcuts import render,redirect
from .forms import SignupForm,CreateProfile,UploadNewProject
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.edit import CreateView
from .models import Profile, Project, Rating
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    projects=Project.objects.all()
    return render(request, "home.html", {"projects":projects})

def Signup(request):
    form=SignupForm()

    if request.method =="POST":
        form=SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')

    else:
        form=SignupForm()

    return render(request, "sign_up.html", {"form":form})

def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if username and password:
            user=authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('index')

            else:
                messages.error(request, "Username or password is Incorrect")

        else:
            messages.error(request, "Fill out all the fields")

    return render(request, "login.html", {})

def logout(request):
    logout(request)
    return redirect('home')

class CreateProfileView(CreateView):
    model=Profile
    form_class=CreateProfile
    template_name='createprofile.html'

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


def viewProject(request, pk):
    project=Project.objects.filter(id=pk)
    current_user=request.user

    return render(request, 'viewproject.html', {"project":project})


@login_required(login_url='login')
def uploadProject(request):
    form=UploadNewProject()
    current_user=request.user

    if request.method =="POST":
        form=UploadNewProject(request.POST, request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.profile=current_user
            project.save()

        return redirect('home')

    else:
        form=UploadNewProject()

    return render(request, 'uploadproject.html', {"form":form})


