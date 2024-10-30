# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'is_staff']

    def create(self, validated_data):
        # Create user with hashed password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            is_staff=validated_data.get('is_staff', False),
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        # Update only the fields specified
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)

        # Update password if provided
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])  # Hash the new password

        instance.save()  # Save the user instance
        return instance
