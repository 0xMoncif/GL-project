from django.urls import path
from .views import *

urlpatterns = [
    path("offers/", OfferListCreateAPIView.as_view(), name="offer-list-create"),
    path("offers/<int:pk>/", OfferDetailAPIView.as_view(), name="offer-detail"),
    path("offers/<int:pk>/publish/", PublishOfferAPIView.as_view(), name="offer-publish"),
    path("offers/<int:pk>/archive/", ArchiveOfferAPIView.as_view(), name="offer-archive"),
]