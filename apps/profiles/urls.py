from django.urls import path
from .views import StudentProfileDetailView, CompanyProfileDetailView

urlpatterns = [
    path('student/profile/', StudentProfileDetailView.as_view(), name='student-profile'),
    path('company/profile/', CompanyProfileDetailView.as_view(), name='company-profile'),
]
