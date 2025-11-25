from rest_framework.permissions import BasePermission

class IsCompany(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user 
            and request.user.is_authenticated 
            and hasattr(request.user, 'companyprofile')
        )


class IsOfferOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.company.user == request.user
