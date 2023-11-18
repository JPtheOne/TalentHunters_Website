from django import forms
from .models import SimpleModel, Hunter2, Project2


class SimpleForm(forms.ModelForm):
    class Meta:
        model = SimpleModel
        fields = ['name']

class Hunter2Form(forms.ModelForm):
    class Meta:
        model = Hunter2
        fields = ['username', 'password', 'full_name', 'email', 'phone', 'location', 'linkedin', 'industry']
        widgets = {
            'password': forms.PasswordInput(),  # Para manejar el campo de contraseña como un campo de contraseña
        }
        
    def __init__(self, *args, **kwargs):
        super(Hunter2Form, self).__init__(*args, **kwargs)
        self.fields['linkedin'].required = False
        self.fields['linkedin'].initial = 'https://www.linkedin.com/in/example/'  # Set a default value


class Project2Form(forms.ModelForm):
    class Meta:
        model = Project2
        fields = ['title', 'description', 'required_skills', 'budget', 'duration', 'status']