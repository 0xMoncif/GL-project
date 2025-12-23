from django.db.models import Q
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Offer
from .permissions import (
    IsCompany,
    IsOfferOwner,
    IsStudent,
)
from .serializers import OfferSerializer

# Student side :


class StudentOfferListView(
    ListAPIView
):  # this is for student (handle the case of cibled and uncibled offers)
    permission_classes = [IsAuthenticated, IsStudent]
    serializer_class = OfferSerializer

    def get_queryset(self):
        student = self.request.user.studentprofile

        return (
            Offer.objects.filter(is_active=True)
            .filter(Q(institutions__isnull=True) | Q(institutions=student.institution))
            .select_related("company")
            .prefetch_related("institutions", "required_skills", "domain", "specialty")
            .order_by("-created_at")
            .distinct()
        )


class StudentOfferDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsStudent]
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()

    def get_object(self):
        offer = super().get_object()
        student = self.request.user.studentprofile

        if (
            offer.institutions.exists()
            and student.institution not in offer.institutions.all()
        ):
            raise PermissionDenied("You do not have access to this offer.")

        return offer


# Company side :


class OfferListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsCompany, IsAuthenticated]
    serializer_class = OfferSerializer

    def get_queryset(self):
        return Offer.objects.filter(
            company=self.request.user.companyProfile
        )  # to return only company's own offers

    def perform_create(
        self, serializer
    ):  # this is to assign the user (company) to the offer created automatically
        company_profile = self.request.user.companyProfile
        serializer.save(company=company_profile)


class CompanyOfferDetailView(
    RetrieveUpdateDestroyAPIView
):  # this is for a single offer instance
    serializer_class = OfferSerializer

    def get_queryset(self):
        return Offer.objects.filter(company=self.request.user.companyProfile)

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAuthenticated(), IsCompany(), IsOfferOwner()]
        return [IsAuthenticated(), IsCompany()]


class PublishOfferAPIView(RetrieveAPIView):
    permission_classes = [IsOfferOwner]

    def get_queryset(self):
        return Offer.objects.filter(company=self.request.user.companyprofile)

    def post(self, request, pk):
        offer = self.get_object()
        offer.is_active = True
        offer.save()
        return Response({"message": "Offer published."}, status=status.HTTP_200_OK)


class ArchiveOfferAPIView(RetrieveAPIView):
    permission_classes = [IsOfferOwner]

    def get_queryset(self):
        return Offer.objects.filter(company=self.request.user.companyprofile)

    def post(self, request, pk):
        offer = self.get_object()
        offer.is_active = False
        offer.save()
        return Response({"message": "Offer Archived."}, status=status.HTTP_200_OK)
