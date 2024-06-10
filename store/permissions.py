from rest_framework.permissions import BasePermission

class SellerPermission(BasePermission):
    message = "Only seller allowed"

    def has_permission(self, request, view):
        return not request.user.is_buyer
    
class BuyerPermission(BasePermission):
    message = "Only buyer allowed"

    def has_permission(self, request, view):
        return request.user.is_buyer

class IsSame(BasePermission):
    message = "You cannot delete others products"

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
