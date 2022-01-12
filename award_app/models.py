from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Project(models.Model):
    profile=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=500)
    image=CloudinaryField('image')
    description=models.TextField()
    link=models.CharField(max_length=1000)
    design_rating=models.ManyToManyField(User, related_name="rate_design")
    usability_rating=models.ManyToManyField(User, related_name="rate_usability")
    content_rating=models.ManyToManyField(User, related_name="rate_content")
    average_review=models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def search_by_title(search_term):
        projects=Project.objects.filter(title__icontains=search_term)
        return projects

class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField()
    profile_pic=CloudinaryField('image' ,blank=True)
    #projects=models.ForeignKey(Project, on_delete=models.CASCADE)
    contact=models.TextField()

    def __str__(self):
        return str(self.user)  

class Rating(models.Model):
    design=models.ForeignKey(Project, related_name="design_rated", on_delete=models.CASCADE)
    design_rate=models.IntegerField()
    usability=models.ForeignKey(Project, related_name="usability_rated", on_delete=models.CASCADE)
    usability_rate=models.IntegerField()
    content=models.ForeignKey(Project, related_name="content_rated", on_delete=models.CASCADE)
    content_rate=models.IntegerField()

    def __str__(self):
        return self.design_rate

    def get_absolute_url(self):
        return reverse('home')
