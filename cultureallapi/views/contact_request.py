from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from cultureallapi.models import ContactRequest
from cultureallapi.models.cult_user import CultUser

class ContactRequestView(ViewSet): 
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
        """Handl Post Operations

        Returns:
            response -- JSON serialized request instance
        """

        contact_request = ContactRequest.objects.create(
            email=request.data["email"], 
            first_name=request.data[first_name],
            last_name=request.data["last_name"],
            phone_number=request.data["phone_number"],
            contact_by_phone=int(request.data["contact_by_phone"])
        )

        serializer = ContactSerializer(contact_request)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a Contact

        Returns:
            Response -- Empty body with 204 status code
        """

        request = ContactRequest.objects.get(pk=pk)
        request.email = request.data["email"]
        request.first_name = request.data["first_name"]
        request.last_name = request.data["last_name"]
        request.phone_number = request.data["phone_number"]
        request.contact_by_phone = request.data["contact_by_phone"]
        
        request.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        request = ContactRequest.objects.get(pk=pk)
        request.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactRequest
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'contact_by_phone')
        depth = 1
