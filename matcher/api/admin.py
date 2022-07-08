from django.contrib import admin
from .models import Skill, Candidate, Job


# Registering all models to the admin panel.
all_models = [Skill, Candidate, Job]
admin.site.register(all_models)
