from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from cultureallapi.models import Question
from cultureallapi.models.answer import Answer
from cultureallapi.models.question_type import QuestionType
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class QuestionView(ViewSet): 
    """Question View"""
    permission_classes=[IsAuthenticatedOrReadOnly]
    def retrieve(self, request, pk):
        """Handle GET requests for single Question
        
        Returns:
            Response -- JSON serialized question
        """
        try:
            question = Question.objects.get(pk=pk)
            serializer = QuestionSerializer(question)
            return Response(serializer.data)
        except Question.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all Questions
        
        Returns:
            Response -- JSON serialized list of questions
            """

        questions = Question.objects.all()

        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT questions for a Question

        Returns:
            Response -- Empty body with 204 status code
        """

        question = Question.objects.get(pk=pk)
        question.question_text = question.data["question_text"]

        question_type = QuestionType.objects.get(pk=request.data["question_type"])
        question.question_type = question_type

        question.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'rating_value')
        depth = 1

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'question_type', 'answers')
        depth = 2
