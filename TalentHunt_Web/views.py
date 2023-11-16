from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

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

