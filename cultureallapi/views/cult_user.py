from dataclasses import fields
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from cultureallapi.models import CultUser, Answer
from cultureallapi.models.question import Question
from cultureallapi.models.question_type import QuestionType


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
        user.save()
        serializer = UserSerializer(user)
        serializer = CultUserSerializer(cult_user)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(methods=["put"], detail=True)
    def change_staff_status(self, request, pk):
        cult_user = CultUser.objects.get(pk=pk)
        
        cult_user.user.is_staff = not cult_user.user.is_staff
        cult_user.user.save()
        serializer = UserSerializer(cult_user.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["put"], detail=True)
    def change_terms_status(self, request, pk):
        cult_user = CultUser.objects.get(pk=pk)
        
        cult_user.terms_signed = not cult_user.terms_signed
        cult_user.save()
        serializer = UserSerializer(cult_user.user)
        return Response(serializer.data, status=status.HTTP_200_OK)






class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff')
        # ordering =  ['username']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'rating_value')
        depth = 1

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'answers')
        depth = 1

class QuestionTypeSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = QuestionType
        fields = ('id', 'type', 'questions')
        depth = 2


class CultUserSerializer(serializers.ModelSerializer):
    """JSON serializer for CultUsers"""
    user = UserSerializer()
    # answers = AnswerSerializer(many=True)
    question_types = QuestionTypeSerializer(many=True)
    class Meta:
        model = CultUser
        fields = ('id', 'user', 'company_name', 'phone_number', 'terms_signed', 'question_types')
        depth = 2