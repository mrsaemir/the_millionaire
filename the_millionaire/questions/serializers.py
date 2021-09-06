from rest_framework import serializers
from .models import Question, QuestionOption


class QuestionOptionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    text = serializers.CharField()


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    score = serializers.IntegerField()
    options = QuestionOptionSerializer(many=True)
    answer = serializers.SerializerMethodField()

    def get_answer(self, obj):
        if self.context['session'].has_answered(obj):
            return obj.answer.id
        return None


class UserQuestionSessionListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    score = serializers.IntegerField()


class UserQuestionSessionDetailSerializer(UserQuestionSessionListSerializer):
    questions = QuestionSerializer(many=True)
    answers = serializers.ListField()


class SetAnswerSerializer(serializers.Serializer):
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.published())
    answer = serializers.PrimaryKeyRelatedField(queryset=QuestionOption.objects.all())

    def save(self, **kwargs):
        return self.context['session'].set_answer(**self.validated_data)

