from django.urls import path

from .views import (
    ArchiveOfferAPIView,
    CompanyOfferDetailView,
    OfferListCreateAPIView,
    PublishOfferAPIView,
    StudentOfferDetailView,
    StudentOfferListView,
)

urlpatterns = [
    path("student/offers/", StudentOfferListView.as_view(), name="student-offer-list"),
    path(
        "student/offers/<int:pk>/",
        StudentOfferDetailView.as_view(),
        name="student-offer-detail",
    ),
    path(
        "company/offers/",
        OfferListCreateAPIView.as_view(),
        name="company-offer-list-create",
    ),
    path(
        "company/offers/<int:pk>/",
        CompanyOfferDetailView.as_view(),
        name="company-offer-detail",
    ),
    path(
        "company/offers/<int:pk>/publish/",
        PublishOfferAPIView.as_view(),
        name="company-offer-publish",
    ),
    path(
        "company/offers/<int:pk>/archive/",
        ArchiveOfferAPIView.as_view(),
        name="company-offer-archive",
    ),
]
