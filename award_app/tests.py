from django.test import TestCase
from .models import Profile, Project, Rating
from django.contrib.auth.models import User
# Create your tests here.


# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.alice=User(username='Alice')
        self.alice.save()

        self.alice=Profile(user=self.alice, bio="this is an admin bio", profile_pic="https://www.pinterest.com/pin/492649949221163/", contact="Nairobi, Kenya")
        self.alice.save_profile()

    def test_instance(self):
        self.assertTrue(isinstance(self.alice, Profile))

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()

    def test_save_profile(self):
        self.alice.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        profiles=Profile.objects.all()

        self.alice.delete_profile()
        self.assertEqual(len(profiles), 0)

class ProjectTestClass(TestCase):
    def setUp(self):
        self.khaleesi=User(username="Khaleesi")
        self.khaleesi.save()

        self.firstproject=Project(profile=self.khaleesi, title="First Project", image="https://www.pinterest.com/pin/301319031323420209/", description="this is the first uploaded project", link="https://github.com/Alice-Githui/My-Pitch-App.git", design_rate=0, usability_rate=0, content_rate=0, average_review=0)
        self.firstproject.save_project()

    def testinstance(self):
        self.assertTrue(isinstance(self.firstproject, Project))

    def test_save_project(self):
        self.firstproject.save_project()
        projects=Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete_project(self):
        projects=Project.objects.all()

        self.firstproject.delete_project()
        self.assertEqual(len(projects), 0)