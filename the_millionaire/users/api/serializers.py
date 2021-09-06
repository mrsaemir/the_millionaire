from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)
    name = serializers.CharField(allow_blank=True)

    def save(self, **kwargs):
        user = User(
            **{
                "username": self.validated_data['username'],
                "name": self.validated_data['name']
            }
        )
        user.set_password(self.validated_data['password'])
        user.save()
        return user
