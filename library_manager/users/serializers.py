from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def save(self, *args, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            is_superuser=False,
            is_staff=False,
            is_active=True
            )

        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user
