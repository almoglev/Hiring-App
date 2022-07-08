from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SkillSerializer, CandidateSerializer, JobSerializer
from .models import Skill, Candidate, Job
from django.db.models import Q
from functools import reduce
from operator import or_


MIN_THRESHOLD = 0.7 # Threshold to determine what is a "best candidate" - in this case - has to meet at least 70% of the required skills of the job
MAX_CANDIDATES_ABOVE_THRESHOLD = 100 # When reaching more than this number we have enough best candidates so we can stop


# View of the API
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'API Overview' : 'http://localhost:8000/api',
        'Admin Panel' : 'http://localhost:8000/admin',
        'GET best candidates': 'http://localhost:8000/api/best-candidate-list/<int:jobId>',
        'GET all skills': 'http://localhost:8000/api/skill-list',
        'GET all candidates': 'http://localhost:8000/api/candidate-list',
        'GET all jobs': 'http://localhost:8000/api/job-list',
    }
    return Response(api_urls)

########### 
# View of the models (skills, candidates, jobs)
# These endpoints return everything - Implemented them for testing purposes. 
# Of course in real production we will add paging and amount per page or top X to return, 
# as we don't want to pull everything in one go (performance)
########### 
@api_view(['GET'])
def showAllSkills(request):
    try:
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)
    except Skill.DoesNotExist:
        raise Http404("No skills in the database yet.")

@api_view(['GET'])
def showAllCandidates(request):
    try:
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)
    except Candidate.DoesNotExist:
        raise Http404("No candidates in the database yet.")

@api_view(['GET'])
def showAllJobs(request):
    try:
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
    except Job.DoesNotExist:
        raise Http404("No jobs in the database yet.")

########### 
# View of the best candidates
########### 
@api_view(['GET'])
def showBestCandidates(request, jobId):
    try:
        return Response(getBestCandidateList(jobId))
    except Job.DoesNotExist:
        raise Http404("A job with JobId=" + str(jobId) + " does not exist.")


########### 
# Helper Functions 
# (If the logic behind the endpoints grow then move these functions to another file, for example: viewsManager.py that will handle all the logic)
###########

# Get the best matching candidates for a job
def getBestCandidateList(jobId):
    job = Job.objects.get(id=jobId)

    # Get candidates with matching/partially matching title
    potential_candidates = getPotentialCandidates(job.title)  

    # Sort by matching skills count
    skills_dict = mapSkillsCounterToCandidates(job.skills, potential_candidates)
    skills_dict_ordered = orderDictionaryDesc(skills_dict)
    return skills_dict_ordered


# Pulls from db all candidates with matching/partially matching title
def getPotentialCandidates(job_title):
    title_words = job_title.split()
    query = reduce(or_, (Q(title__icontains=t) for t in title_words))
    return Candidate.objects.filter(query).values() 


# Dictionary to map between skills counter to candidates
def mapSkillsCounterToCandidates(job_skills, candidates):
    
    # Initializations.
    l = []
    dict = {}
    for i in range(0, len(job_skills) + 1):
        dict[i] = []

    candidates_above_threshold = 0
    min_skills_required = round(MIN_THRESHOLD * len(job_skills))
    
    # Build dictionary
    for candidate in candidates:
        count = countMatchingSkills(job_skills, candidate['skills'])

        if count >= min_skills_required:
            candidates_above_threshold += 1
        
        if candidates_above_threshold > MAX_CANDIDATES_ABOVE_THRESHOLD:
            break

        if dict[count] != []:
            l = dict[count]

        l.append(candidate)
        dict[count] = l
        l = []
    
    return dict


# Counts how many skills are matching between the job to the candidate.
def countMatchingSkills(job_skills, candidate_skills):
    return sum(s in job_skills for s in candidate_skills)


# Orders the dictionary by skills counter desc (so the best candidates are shown first).
def orderDictionaryDesc(skills_dict):
    res = []
    
    if all(value == [] for value in skills_dict.values()):
        return res

    for k, v in sorted(skills_dict.items(), reverse=True):
        res.append("Candidates with " + str(k) + " matching skill(s): " +str(v))
    
    return res
