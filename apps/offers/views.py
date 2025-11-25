from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Offer
from .serializers import OfferSerializer
from .permissions import IsCompany, IsOfferOwner
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



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
 

class PublishOfferAPIView(APIView):
    permission_classes = [IsOfferOwner]

    def post(self, request, pk):
        offer = Offer.objects.get(pk=pk)
        self.check_object_permissions(request, offer)

        offer.is_active = True
        offer.save()

        return Response({"message": "Offer published."}, status=status.HTTP_200_OK)


class ArchiveOfferAPIView(APIView):
    permission_classes = [IsOfferOwner]

    def post(self, request, pk):
        offer = Offer.objects.get(pk=pk)
        self.check_object_permissions(request, offer)

        offer.is_active = False
        offer.save()

        return Response({"message": "Offer archived."}, status=status.HTTP_200_OK)
