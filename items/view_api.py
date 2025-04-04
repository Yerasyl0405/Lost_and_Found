from rest_framework import generics, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from silk.profiling.profiler import silk_profile

from .models import LostItem, FoundItem

from .serializers import LostItemSerializer, FoundItemSerializer


# List view (GET all lost items)
class LostItemListView(generics.ListAPIView):
    queryset = LostItem.objects.all()
    serializer_class = LostItemSerializer


# Retrieve view (GET one lost item by ID)
class LostItemDetailView(generics.RetrieveAPIView):
    queryset = LostItem.objects.all()
    serializer_class = LostItemSerializer

class LostItemCreateAPI(generics.CreateAPIView):
    serializer_class = LostItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    @silk_profile()
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MarkLostRecoveredAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    @silk_profile()
    def post(self, request, item_id):
        try:
            item = LostItem.objects.get(id=item_id)
        except LostItem.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        if request.user == item.user or request.user.is_staff:
            item.status = "recovered"
            item.is_recovered = True
            item.save()
            return Response({"message": "Item marked as recovered"})
        return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)


class FoundItemListAPI(generics.ListAPIView):
    queryset = FoundItem.objects.all()
    serializer_class = FoundItemSerializer


class FoundItemCreateAPI(generics.CreateAPIView):
    serializer_class = FoundItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    @silk_profile()
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MarkFoundClaimedAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    @silk_profile()
    def post(self, request, item_id):
        try:
            item = FoundItem.objects.get(id=item_id)
        except FoundItem.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        if request.user == item.user or request.user.is_staff:
            item.status = "claimed"
            item.is_claimed = True
            item.save()
            return Response({"message": "Item marked as claimed"})
        return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
class DeleteLostItemView(APIView):
    permission_classes = [IsAdminUser]
    @silk_profile()
    def delete(self, request, item_id):
        item = get_object_or_404(LostItem, id=item_id)
        item.delete()
        return Response({"detail": "Lost item deleted."}, status=status.HTTP_204_NO_CONTENT)

class DeleteFoundItemView(APIView):
    permission_classes = [IsAdminUser]
    @silk_profile()
    def delete(self, request, item_id):
        item = get_object_or_404(FoundItem, id=item_id)
        item.delete()
        return Response({"detail": "Found item deleted."}, status=status.HTTP_204_NO_CONTENT)