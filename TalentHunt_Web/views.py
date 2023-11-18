from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Hunter, Project, Hunter2, Project2
from .forms import SimpleForm, Hunter2Form, Project2Form

#region DB views
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/hunterhume/')  # Redirect to a home page or dashboard
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')



def simple_form_view(request):
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = SimpleForm()

    return render(request, 'simple_form.html', {'form': form})

def huntersignup2_view(request):
    if request.method == 'POST':
        hunter_form = Hunter2Form(request.POST)
        project_forms = [Project2Form(request.POST, prefix=str(x), files=request.FILES) for x in range(0, 3)] # Ejemplo para 3 proyectos

        if hunter_form.is_valid() and all([pf.is_valid() for pf in project_forms]):
            hunter = hunter_form.save()

            for pf in project_forms:
                project = pf.save(commit=False)
                project.hunter = hunter
                project.save()

            return redirect('/hunterhume/')

    else:
        hunter_form = Hunter2Form()
        project_forms = [Project2Form(prefix=str(x)) for x in range(0, 3)] # Ejemplo para 3 proyectos

    return render(request, 'huntersign2.html', {'hunter_form': hunter_form, 'project_forms': project_forms})

def hunterHume_sign(request):
    if request.method == 'POST':
        print("Received POST data:", request.POST)
        # Correctly extracting form data using the correct field names
        username = request.POST.get('username')
        email = request.POST.get('email', '')
        print("Username:", username, "Email:", email, ...)
        password = request.POST.get('password')
        full_name = request.POST.get('full-name')
        phone_number = request.POST.get('phone', '')
        location = request.POST.get('location', '')
        linkedin_profile = request.POST.get('linkedin', '')
        industry = request.POST.get('industry', '')

        # Create a new User
        print("Creating user with Username:", username, "Email:", email)
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        # Create a new Hunter
        print("Creating hunter for User:", user.username)
        hunter = Hunter.objects.create(
            user=user,
            full_name=full_name,
            phone_number=phone_number,
            location=location,
            linkedin_profile=linkedin_profile,
            industry=industry
        )

        # Handling multiple projects
        project_titles = request.POST.getlist('project-title[]')
        project_descriptions = request.POST.getlist('project-description[]')
        required_skills = request.POST.getlist('required-skills[]')
        budgets = request.POST.getlist('budget[]')
        durations = request.POST.getlist('duration[]')
        statuses = request.POST.getlist('status[]')

        for i in range(len(project_titles)):
            Project.objects.create(
                hunter=hunter,
                title=project_titles[i],
                description=project_descriptions[i],
                required_skills=required_skills[i],
                budget=budgets[i],
                duration=durations[i],
                status=statuses[i]
            )

        return redirect('/hunterhume/')
    return render(request, 'huntersign.html')

#endregion

#region html basic views
def home_view(request):
    return render(request, 'home.html')

#def login_view(request):
#    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'talentOrhunter.html')
()
def forgot_view(request):
    return render(request, 'forgot.html')

def hunterSign_view(request):
    return render(request, 'huntersign.html')

def talentSign_view(request):
    return render(request, 'talentsign.html')

def hunterHume_sign(request):
    return render(request, 'hunterhume.html')

def talentlog_view(request):
    return render(request, 'talentlog.html')

def hunterProfile_view(request):
    return render(request, 'hunterprofile.html')

def speedHunter_view(request):
    return render(request, 'speedhunter.html')

def hunterProjects_view(request):
    return render(request, 'hunterproyects.html')

def hunterChangeInfo_view(request):
    return render(request, 'hunterchangeinfo.html')

def evaluateTalent_view(request):
    return render(request, 'evaluatemytalent.html')

def evaluateHunter_view(request):
    return render(request, 'evaluatemyhunter.html')

def contractHunt_view(request):
    return render(request, 'contracthunt.html')

def contractTalent_view(request):
    return render(request, 'contracttalent.html')

def talentProfile_view(request):
    return render(request, 'talentprofile.html')

def speedTalent_view(request):
    return render(request, 'speedtalent.html')

def talentProjects_view(request):
    return render(request, 'talentproyects.html')

def talentChangeInfo_view(request):
    return render(request, 'talentchangeinfo.html')
#endregion

