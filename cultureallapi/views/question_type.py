from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from cultureallapi.models import Question
from cultureallapi.models.question_type import QuestionType


class QuestionTypeView(ViewSet): 
    """Question Type View"""

    def retrieve(self, request, pk):
        """Handle GET requests for single Question Type
        
        Returns:
            Response -- JSON serialized question
        """
        try:
            question_type = QuestionType.objects.get(pk=pk)
            serializer = QuestionTypeSerializer(question_type)
            return Response(serializer.data)
        except Question.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all Questions
        
        Returns:
            Response -- JSON serialized list of questions
            """

        question_types = QuestionType.objects.all()

        serializer = QuestionTypeSerializer(question_types, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT questions for a Question

        Returns:
            Response -- Empty body with 204 status code
        """

        question_type = QuestionType.objects.get(pk=request.data["question_type"])


        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        question_type = QuestionType.objects.get(pk=pk)
        question_type.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class QuestionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionType
        fields = ('id', 'type')
        depth = 1
