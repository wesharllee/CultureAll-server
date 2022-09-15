from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from cultureallapi.models import Question, CultUser
from cultureallapi.models.answer import Answer
from cultureallapi.models.question_type import QuestionType
from rest_framework.permissions import AllowAny


class AnswerView(ViewSet):
    """Answer View"""
    permission_classes=[AllowAny]
    def retrieve(self, request, pk):
        """Handle GET requests for single answer

        Returns:
            Response == JSON serialized answer
        """

        try:
            answer = Answer.objects.get(pk=pk)
            serializer = AnswerSerializer(answer)
            return Response(serializer.data)
        except Answer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all answers
        
        Returns:
            Response -- JSON serialized list of answers
            """

        answers = Answer.objects.all()

        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)      

    def create(self, request):
        """Handle Post operations

        Returns:
            response -- JSON serialized answer instance
        """
        # cult_user = CultUser.objects.get(user=request.auth.user)
        cult_user = CultUser.objects.get(pk=request.data["cult_user"])
        question = Question.objects.get(pk=request.data["question"])
        answer = Answer.objects.create(
            cult_user=cult_user,
            # cult_user=request.data["cult_user"],
            question=question,
            rating_value=request.data["rating_value"]
        )

        serializer = AnswerSerializer(answer)
        return Response(serializer.data)

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question', 'rating_value', 'cult_user')