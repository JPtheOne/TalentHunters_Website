
from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('forgot/', forgot_view, name='forgot'),
    path('huntersign/', hunterSign_view, name='huntersign'),
    path('talentsign/', talentSign_view, name='talentsign'),
    path('hunterhume/', hunterHume_sign, name='hunterhume'),
    path('talentlog/', talentlog_view, name = 'talentlog'),
    path('hunterprofile/',hunterProfile_view , name='hunterprofile'),
    path('speedhunter/', speedHunter_view, name='speedhunter'),
    path('hunterproyects/',hunterProjects_view , name='hunterproyects'), 
    path('hunterchangeinfo/',hunterChangeInfo_view, name='hunterchangeinfo'), 
    path('evaluatemytalent/',evaluateTalent_view, name='evaluateTalent'), 
    path('evaluatemyhunter/', evaluateHunter_view, name='evaluateHunter') ,
    path('contracthunt/', contractHunt_view, name='contracthunt'),
    path('contracttalent/', contractTalent_view, name='contracttalent'),
    path('talentprofile/', talentProfile_view, name='talentprofile'),
    path('speedtalent/', speedTalent_view, name='speedtalent'),
    path('talentproyects/', talentProjects_view, name='talentproyects'),
    path('talentchangeinfo/', talentChangeInfo_view, name='talentchangeinfo'),
    path('simple-form/', simple_form_view, name='simple_form'),
    path('huntersign2/', huntersignup2_view, name='huntersignup2'),

]
