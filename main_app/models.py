from django.db import models

# Create your models here.

# Model for New Employee's
class Employee(models.Model):
    EmpNumber = models.IntegerField()
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    JobTitle = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.LastName + " " + self.FirstName + " " +self.JobTitle
    
    class Meta:
        ordering = ["LastName"]
    