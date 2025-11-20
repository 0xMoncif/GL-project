from django.db import models

class Offer(models.Model):
    OFFER_TYPES = [
        ('internship', 'Internship'),
        ('pfe', 'PFE'),
        ('job', 'First Job'),
    ]
    company = models.ForeignKey('profiles.CompanyProfile', on_delete=models.CASCADE, related_name='offers')
    title = models.CharField(max_length=255)
    description = models.TextField()
    offer_type = models.CharField(max_length=20, choices=OFFER_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="offers/images/", null=True, blank=True)
    pdf = models.FileField(upload_to="offers/pdfs/", null=True, blank=True)

    domain = models.ManyToManyField('catalog.Domain', through='offers.RequiredDomain', blank=True)
    specialty = models.ManyToManyField('catalog.Specialty', through='offers.RequiredSpecialty', blank=True)
    required_skills = models.ManyToManyField('catalog.Skill',through='offers.RequiredSkill', blank=True )
    institutions = models.ManyToManyField('catalog.Institution', through='offers.RequiredInstitution', blank=True)
    
    def __str__(self):
        return f"{self.title} ({self.offer_type})"


class RequiredSkill (models.Model):
    offer= models.ForeignKey(Offer, on_delete=models.CASCADE )
    skill= models.ForeignKey('catalog.Skill', on_delete=models.CASCADE, related_name='skills')
    
    class Meta:
        unique_together = ('offer', 'skill')

    def __str__(self):
        return f"{self.offer.title} requires {self.skill.title}"    



class RequiredInstitution (models.Model):
    offer= models.ForeignKey(Offer, on_delete=models.CASCADE )
    institution= models.ForeignKey('catalog.Institution', on_delete=models.CASCADE, related_name='institutions')
     
    class Meta:
        unique_together = ('offer', 'institution') 

    def __str__(self):
        return f"{self.offer.title} targets {self.institution.title}"   



class RequiredDomain (models.Model):
    offer= models.ForeignKey(Offer, on_delete=models.CASCADE )
    domain= models.ForeignKey('catalog.Domain', on_delete=models.CASCADE, related_name='domains')
    
    class Meta:
        unique_together = ('offer', 'domain')
 
    def __str__(self):
        return f"{self.offer.title} is for {self.domain.title}"


class RequiredSpecialty (models.Model):
    offer= models.ForeignKey(Offer, on_delete=models.CASCADE)
    specialty= models.ForeignKey('catalog.Specialty', on_delete=models.CASCADE, related_name='specialties')
       
    class Meta:
        unique_together = ('offer', 'specialty') 

    def __str__(self):
        return f"{self.offer.title} is for {self.specialty.title}"      