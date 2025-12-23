from rest_framework import generics, permissions

from .models import (
    CompanyProfile,
    StudentProfile,
)
from .serializers import (
    CompanyProfileSerializer,
    StudentProfileSerializer,
)


class StudentProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = StudentProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return StudentProfile.objects.filter(user=self.request.user)


class CompanyProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = CompanyProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CompanyProfile.objects.filter(user=self.request.user)
