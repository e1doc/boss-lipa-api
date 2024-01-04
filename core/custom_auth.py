from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

from djoser.serializers import UserCreateSerializer


class CaseInsensitiveModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        # Case-insensitive username lookup
        user = UserModel.objects.filter(username__iexact=username).first()

        if user and user.check_password(password):
            return user
        return None

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'sex', 'email', 'phone_number', 'username', 'password')