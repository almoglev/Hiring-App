from django.db import models
from jsonfield import JSONField


# Skill model.
class Skill(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


# Candidate model.
class Candidate(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    skills = JSONField(default=list, blank=True)

    def __str__(self):
        return self.name + " - " + self.title


# Job model.
class Job(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    skills = JSONField(default=list, blank=True)

    def __str__(self):
        return self.title
