from rest_framework import serializers


class QuestionOptionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    text = serializers.CharField()


class QuestionSerializer(serializers.Serializer):
    title = serializers.CharField()
    score = serializers.IntegerField()
    options = QuestionOptionSerializer(many=True)
    answer = serializers.SerializerMethodField()

    def get_answer(self, obj):
        return None


class UserQuestionSessionSerializer(serializers.Serializer):
    questions = QuestionSerializer(many=True)
    answers = serializers.DictField()
    score = serializers.IntegerField()
    is_closed = serializers.BooleanField()
