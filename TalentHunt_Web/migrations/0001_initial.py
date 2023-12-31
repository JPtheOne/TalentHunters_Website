# Generated by Django 4.2.7 on 2023-11-16 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hunter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin_profile', models.URLField(blank=True, null=True)),
                ('industry', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('required_skills', models.CharField(max_length=200)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='TalentHunt_Web.hunter')),
            ],
        ),
    ]
