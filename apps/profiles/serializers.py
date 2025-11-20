
from rest_framework import serializers
from .models import StudentProfile, CompanyProfile

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = [
            'first_name', 'last_name', 'cv_pdf','profile_picture'
            'headline', 'bio', 'is_profile_public','domain','speciality',
            'institution'
        ]

class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = [
            'company_name', 'phone_nbr', 'description','profile_picture'
            'logo', 'city'
        ]