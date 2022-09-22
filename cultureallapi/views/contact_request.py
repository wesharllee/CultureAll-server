from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from cultureallapi.models import ContactRequest
from cultureallapi.models.cult_user import CultUser
from rest_framework.permissions import AllowAny

class ContactRequestView(ViewSet): 
    permission_classes=[AllowAny]
    """Contact Request View"""

    def retrieve(self, request, pk):
        """Handle GET requests for single Contact
        
        Returns:
            Response -- JSON serialized request
        """
        try:
            request = ContactRequest.objects.get(pk=pk)
            serializer = ContactSerializer(request)
            return Response(serializer.data)
        except ContactRequest.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all Contact requests
        
        Returns:
            Response -- JSON serialized list of requests
            """

        requests = ContactRequest.objects.all()

        serializer = ContactSerializer(requests, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle Post Operations

        Returns:
            response -- JSON serialized request instance
        """

        contact_request = ContactRequest.objects.create(
            email=request.data["email"], 
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            reason=request.data["reason"],
            phone_number=request.data["phone_number"],
            contact_by_phone=int(request.data["contact_by_phone"]),
            completed=False
        )

        serializer = ContactSerializer(contact_request)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a Contact

        Returns:
            Response -- Empty body with 204 status code
        """

        contact_request = ContactRequest.objects.get(pk=pk)
        contact_request.email = request.data["email"]
        contact_request.first_name = request.data["first_name"]
        contact_request.last_name = request.data["last_name"]
        contact_request.reason = request.data["reason"]
        contact_request.phone_number = request.data["phone_number"]
        contact_request.contact_by_phone = int(request.data["contact_by_phone"])
        contact_request.completed = request.data["completed"]
        
        contact_request.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        request = ContactRequest.objects.get(pk=pk)
        request.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactRequest
        fields = ('id', 'email', 'first_name', 'last_name', 'reason', 'phone_number', 'contact_by_phone', 'completed')
        depth = 1
