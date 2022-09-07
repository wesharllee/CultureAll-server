from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from cultureallapi.models import ConsultationRequest
from cultureallapi.models.cult_user import CultUser

class ConsultationRequestView(ViewSet): 
    """Consultation Request View"""

    def retrieve(self, request, pk):
        """Handle GET requests for single consultation
        
        Returns:
            Response -- JSON serialized request
        """
        try:
            request = ConsultationRequest.objects.get(pk=pk)
            serializer = ConsultationSerializer(request)
            return Response(serializer.data)
        except ConsultationRequest.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all consultation requests
        
        Returns:
            Response -- JSON serialized list of requests
            """

        requests = ConsultationRequest.objects.all()

        cult_user = CultUser.objects.get(user=request.auth.user)
        for request in requests:
            request.joined = cult_user in request.cult_user.all()

        serializer = ConsultationSerializer(requests, many=True)
        return Response(serializer.data)

class ConsultationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConsultationRequest
        fields = ('id', 'cult_user', 'date', 'time', 'in_person', 'address')
        depth = 2
