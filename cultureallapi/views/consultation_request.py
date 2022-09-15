from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from cultureallapi.models import ConsultationRequest
from cultureallapi.models.cult_user import CultUser
from rest_framework.decorators import action

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

        serializer = ConsultationSerializer(requests, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle Post operations

        Returns:
            response -- JSON serialized consultation request instance
        """
        cult_user = CultUser.objects.get(user=request.auth.user)

        consultation_request = ConsultationRequest.objects.create(
            cult_user=cult_user,
            date=request.data["date"],
            time=request.data["time"],
            in_person=int(request.data["in_person"]),
            address=request.data.get("address"),
            completed=False
        )

        serializer = ConsultationSerializer(consultation_request)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a consultation

        Returns:
            Response -- Empty body with 204 status code
        """

        consult_request = ConsultationRequest.objects.get(pk=pk)
        consult_request.date = request.data["date"]
        consult_request.time = request.data["time"]
        consult_request.in_person = request.data["in_person"]
        consult_request.address = request.data["address"]
        consult_request.completed = request.data["completed"]

        cult_user = CultUser.objects.get(pk=request.auth.user)
        request.cult_user = cult_user
        request.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        request = ConsultationRequest.objects.get(pk=pk)
        request.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=["put"], detail=True)
    def change_completed_status(self, request, pk):
        consult_request = ConsultationRequest.objects.get(pk=pk)
        consult_request.completed = not consult_request.completed
        consult_request.save()
        serializer = ConsultationSerializer(consult_request)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class ConsultationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConsultationRequest
        fields = ('id', 'cult_user', 'date', 'time', 'in_person', 'address', 'readable_time', 'readable_date', 'completed')
        depth = 2

