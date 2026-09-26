from django.db import models

# Create your models here.

class ClinicInfo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Branch(models.Model):
    name = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"
    
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    code = models.CharField(max_length=10, unique=True)
    coordinator_name = models.CharField(max_length=100)
    coordinator_contact = models.CharField(max_length=100)
    preparation = models.TextField(blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='services')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name