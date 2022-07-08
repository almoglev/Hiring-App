from rest_framework import serializers
from .models import Skill, Candidate, Job


# Skill serializer.
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


# Candidate serializer.
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'


# Job serializer.
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'