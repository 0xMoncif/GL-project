from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Offer
from .serializers import OfferSerializer
from .permissions import IsCompany, IsOfferOwner

# class OfferCreateView(CreateAPIView):
#     queryset = Offer.objects.all()
#     serializer_class = OfferSerializer
#     permission_classes = [IsCompany, IsOfferOwner]   


# class OfferListView(ListAPIView):
#     queryset = Offer.objects.all()
#     serializer_class = OfferSerializer
#     permission_classes = []   

# class OfferUpdateView(UpdateAPIView):
#     queryset = Offer.objects.all()
#     serializer_class = OfferSerializer
#     permission_classes = [IsCompany, IsOfferOwner]


# class OfferUpdateView(DestroyAPIView):
#     queryset = Offer.objects.all()
#     serializer_class = OfferSerializer
#     permission_classes = [IsCompany, IsOfferOwner]


class OfferListCreateAPIView(ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def get_permissions(self):
        if self.request.method == "POST":  
            return [IsCompany()]  
        return []  
    
    def perform_create(self, serializer):   # this is to assign the user (company) to the offer created
        company_profile = self.request.user.companyProfile
        serializer.save(company=company_profile)


class OfferDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsOfferOwner()]  
        return []   
