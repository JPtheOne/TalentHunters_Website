# Generated by Django 4.2.7 on 2023-11-18 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TalentHunt_Web', '0002_simplemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hunter2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('industry', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('required_skills', models.CharField(max_length=300)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('open', 'Open'), ('in-progress', 'In Progress'), ('completed', 'Completed')], max_length=15)),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TalentHunt_Web.hunter2')),
            ],
        ),
    ]