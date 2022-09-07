from email.policy import default
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model): 
    alias = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    firstname = models.CharField(max_length=50, default='Alex')
    lastname = models.CharField(max_length=50, default='Peters') 
    age = models.IntegerField(default=45) 
    state = models.CharField(max_length=50, default='Enugu') 
    area = models.CharField(max_length=50, default='behind flat') 
    email = models.EmailField(blank=False, null=False, default='Alexie@email.com')
    gender = models.CharField(max_length=50, default='female')
    agegroup = models.CharField(max_length=50, default='18-25') 
    religion = models.CharField(max_length=50, default='christian') 
    discipline = models.CharField(max_length=50, default='science') 
    gender1 = models.CharField(max_length=50, default='female1') 
    smoking = models.CharField(max_length=50, default='no') 
    alcohol = models.CharField(max_length=50, default='no') 
    uncleanliness = models.CharField(max_length=50, default='no') 
    lateness = models.CharField(max_length=50, default='no') 
    homepartying = models.CharField(max_length=50, default='no')
    # image = models.FileField()


    def __str__(self):
        return str(self.alias)
