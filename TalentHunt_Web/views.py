from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'talentOrhunter.html')

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

def _view(request):
    return render(request, '')