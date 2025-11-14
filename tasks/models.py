from django.db import models

# Create your models here.
class Task(models.Model):
    # taskId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    duration = models.IntegerField(null=True, blank=True)
    dueDate = models.DateField()
    completed = models.BooleanField(default=False)
    
    Status_Choices = [
        ('complete', 'Complete'),
        ('incomplete', 'Incomplete'),
    ]
    status = models.CharField(max_length=20, choices= Status_Choices, default='incomplete')
    
    def __str__(self):
        return f"{self.name} (Due: {self.dueDate})"
    