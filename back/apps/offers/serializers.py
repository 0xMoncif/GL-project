from rest_framework import serializers
from .models import Offer
from ..catalog.models import Institution

# class OfferSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Offer
#         fields = "__all__"
#         read_only_fields = ["company", "created_at"]


class OfferSerializer(serializers.ModelSerializer):
    institutions = serializers.PrimaryKeyRelatedField(queryset=Institution.objects.all(),many=True)

    class Meta:
        model = Offer
        fields = [
            'id', 'title', 'description', 'offer_type', 'created_at',
            'end_date', 'is_active', 'image', 'pdf',
            'domain', 'specialty', 'required_skills', 'institutions'
        ]
        read_only_fields = ['company', 'is_active', 'created_at']

    def create(self, validated_data):
        institutions = validated_data.pop("institutions", [])
        offer = Offer.objects.create(**validated_data)
        offer.institutions.set(institutions)
        return offer

    def update(self, instance, validated_data):
        institutions = validated_data.pop("institutions", None)
        offer = super().update(instance, validated_data)
        if institutions is not None:
            offer.institutions.set(institutions)
        return offer
