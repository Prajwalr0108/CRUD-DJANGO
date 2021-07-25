from django.db import models

# Create your models here.
class BasicDetails(models.Model):
    First_Name = models.CharField(max_length=100,blank=False)
    Last_Name = models.CharField(max_length=50,blank=False)
    Father_Name = models.CharField(max_length=50,blank=False)
    Mother_Name = models.CharField(max_length=50,blank=False)
    Date_of_birth = models.DateField(blank=False)
    Gender = models.CharField(max_length=10)
    About = models.TextField(blank=False)

    def __str__(self):
        return self.First_Name

class Education(models.Model):
    Course_Name = models.CharField(max_length=100,blank=False)
    University_or_board_Name = models.CharField(max_length=50,blank=False)
    
    Passing_Year = models.DateField(blank=False)
    

    def __str__(self):
        return self.Course_Name



