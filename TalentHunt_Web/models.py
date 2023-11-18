from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models
from django.contrib.auth.models import User

class Hunter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    hunter = models.ForeignKey(Hunter, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    required_skills = models.CharField(max_length=200)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class SimpleModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Hunter2(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=50)  # Mejor usar django.contrib.auth.models.User para contraseñas
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    industry = models.CharField(max_length=200, blank=True, null=True)

class Project2(models.Model):
    hunter = models.ForeignKey(Hunter2, on_delete=models.CASCADE)  # Relacionar con Hunter2
    title = models.CharField(max_length=200)
    description = models.TextField()
    required_skills = models.CharField(max_length=300)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in-progress', 'In Progress'),
        ('completed', 'Completed')
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)

class Contract(models.Model):
    # ID de contrato, auto-generado
    contract_id = models.AutoField(primary_key=True)

    # Relacionado con el modelo Project (asumiendo que ya existe)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    # Detalles del proyecto (opcional si ya están en el modelo Project)
    project_title = models.CharField(max_length=200)
    project_description = models.TextField()
    project_skills = models.CharField(max_length=300)
    project_budget = models.DecimalField(max_digits=10, decimal_places=2)
    project_duration = models.CharField(max_length=100)
    project_status = models.CharField(max_length=20)

    # Relacionado con el modelo Hunter (asumiendo que ya existe)
    hunter = models.ForeignKey('Hunter', on_delete=models.CASCADE, related_name='contracts')

    # Relacionado con el modelo Talent (asumiendo que ya existe)
    talent = models.ForeignKey('Talent', on_delete=models.CASCADE, related_name='contracts')

    # Detalles del contrato
    terms = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    # Estados del contrato (por ejemplo, aceptado, declinado, pendiente)
    STATUS_CHOICES = [
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
        ('pending', 'Pending')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.project_title} - {self.hunter} to {self.talent}"
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency_choices = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ]
    proficiency = models.CharField(max_length=15, choices=proficiency_choices)
    years_of_experience = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.proficiency})"


class Talent(models.Model):
    # Suponiendo que usaremos el modelo User de Django para manejar username y password
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    availability = models.TextField()
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)

    # Relación con habilidades
    skills = models.ManyToManyField(Skill, related_name='talents')

    def __str__(self):
        return self.full_name

class TalentContract(models.Model):
    # Detalles del proyecto
    project_id = models.IntegerField()  # O ForeignKey si tienes un modelo Project
    project_title = models.CharField(max_length=200)
    project_description = models.TextField()
    project_skills = models.CharField(max_length=300)
    project_budget = models.DecimalField(max_digits=10, decimal_places=2)
    project_duration = models.CharField(max_length=100)
    project_status = models.CharField(max_length=20)

    # Información del cazador de talentos
    hunter_name = models.CharField(max_length=200)
    hunter_email = models.EmailField()
    hunter_phone = models.CharField(max_length=20)

    # Información del talento - asumiendo que ya tienes un modelo Talent
    talent = models.ForeignKey('Talent', on_delete=models.CASCADE)

    # Detalles del contrato
    contract_id = models.IntegerField()
    terms = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    # Estado del contrato - para gestionar la aceptación o rechazo
    STATUS_CHOICES = [
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
        ('pending', 'Pending')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.project_title} - {self.talent}"