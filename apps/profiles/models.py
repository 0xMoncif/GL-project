from django.db import models
from apps.accounts.models import User


class StudentProfile (models.Model):
    user=models.OneToOneField(User, on_delete= models.CASCADE )
    first_name = models.CharField(max_length=50, null=False )
    last_name = models.CharField(max_length=50, null=False )
    profile_picture=models.ImageField(upload_to='profilePics/', blank=True, null=True)                    
    cv_pdf = models.FileField(upload_to='cv_pdfs/', blank=True, null=True)
    headline= models.CharField(max_length=100, blank=True)
    bio= models.TextField(blank=True ,null=True)
    is_Profile_Public = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now=True)
 
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class CompanyProfile (models.Model):
    user=models.OneToOneField(User, on_delete= models.CASCADE)
    company_name = models.CharField(max_length=50, null= False)
    phone_nbr= models.CharField(max_length=15, blank=True)
    description= models.TextField(blank=True, null=True)
    profile_picture=models.ImageField(upload_to='profilePics/', blank=True, null=True)  
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    city= models.CharField(max_length=50, blank=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.company_name
