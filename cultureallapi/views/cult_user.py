from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from cultureallapi.models.cult_user import CultUser

class CultUserView(ViewSet):
    """Cult User view"""

    def retrieve(self, request, pk):
        """handle GET requests for a single user
        """

        try:
            user = CultUser.objects.get(pk=pk)
            serializer = CultUserSerializer(user)
            return Response(serializer.data)
        except CultUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all CultUsers

        Returns:
            Response -- JSON serialized list of CultUsers
        """
        cult_users = CultUser.objects.all().order_by("user__username")
        
        serializer = CultUserSerializer(cult_users, many=True)
        return Response(serializer.data)

    
    def update(self, request, pk):
        """Response -- Empty body with 204 status code"""
        user = User.objects.get(pk=pk)
        cult_user = CultUser.objects.get(user=request.auth.user)
        user.is_staff = not user.is_staff


    @action(methods=["put"], detail=True)
    def change_staff_status(self, request, pk):
        cult_user = CultUser.objects.get(pk=pk)
        
        cult_user.user.is_staff = not cult_user.user.is_staff
        cult_user.user.save()
        serializer = UserSerializer(cult_user.user)
        return Response(serializer.data, status=status.HTTP_200_OK)






class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff')
        # ordering =  ['username']

class CultUserSerializer(serializers.ModelSerializer):
    """JSON serializer for CultUsers"""
    user = UserSerializer()
    class Meta:
        model = CultUser
        fields = ('id', 'user', 'company_name', 'phone_number', 'terms_signed')