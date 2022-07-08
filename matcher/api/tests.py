from django.test import TestCase, Client
from .models import Skill, Candidate, Job


# Unit Tests (just for the basic flow, can add more according to the use-cases)
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.skill_test_1 = Skill.objects.create(name="skill_test_1")
        self.skill_test_2 = Skill.objects.create(name="skill_test_2")
        self.skill_test_3 = Skill.objects.create(name="skill_test_3")
        self.skill_test_4 = Skill.objects.create(name="skill_test_4")

        self.candidate_test_1 = Candidate.objects.create(name="Almog Lev", title="Software Engineer", skills="[1,2,4]")
        self.candidate_test_1 = Candidate.objects.create(name="Dan Cohen", title="software developer", skills="[1,2,3]")
        self.candidate_test_1 = Candidate.objects.create(name="Gal Levy", title="software developer", skills="[1]")
        self.candidate_test_1 = Candidate.objects.create(name="Dana Ayalon", title="BI Developer", skills="[1]")
        
        self.job_test_1 = Job.objects.create(id=1,title="Software Engineer", skills="[1,2,3,4]")
    

    def test_get_skills(self):
        response = self.client.get('/api/skill-list/')
        responseStr = response.content.decode("utf-8")

        self.assertEquals(response.status_code, 200)
        self.assertIn('"name":"skill_test_1"', responseStr)
        self.assertIn('"name":"skill_test_2"', responseStr)
        self.assertIn('"name":"skill_test_3"', responseStr)
        self.assertIn('"name":"skill_test_4"', responseStr)
    

    def test_get_candidates(self):
        response = self.client.get('/api/candidate-list/')
        responseStr = response.content.decode("utf-8")

        self.assertEquals(response.status_code, 200)
        self.assertIn('"name":"Almog Lev"', responseStr)
        self.assertIn('"name":"Dan Cohen"', responseStr)
        self.assertIn('"name":"Gal Levy"', responseStr)
        self.assertIn('"name":"Dana Ayalon"', responseStr)


    def test_get_jobs(self):
        response = self.client.get('/api/job-list/')
        responseStr = response.content.decode("utf-8")

        self.assertEquals(response.status_code, 200)
        self.assertIn('"title":"Software Engineer"', responseStr)


    def test_get_best_candidates(self):
        response = self.client.get('/api/best-candidate-list/1')
        responseStr = response.content.decode("utf-8")

        self.assertEquals(response.status_code, 200)
        self.assertIn('Almog Lev', responseStr)
        self.assertIn('Dan Cohen', responseStr)

        response = self.client.get('/api/best-candidate-list/100')
        self.assertEquals(response.status_code, 404)


