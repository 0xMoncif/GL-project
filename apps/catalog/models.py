from django.db import models

from django.db import models

class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Institution(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    wilaya= models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=250, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name    
    
class Domain(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name    
    
class Specialty(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name="specialties")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.domain.name})"    