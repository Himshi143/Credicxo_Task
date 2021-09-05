from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Student

User = get_user_model()


class CreateStudentSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(source='user.password')

    class Meta:
        model = Student
        exclude = ['user']

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['user']['email'],
            password=validated_data['user']['password']
        )

        user.set_password(user.password)
        user.save()

        student = Student.objects.create(
            user=user,
            enrollment=validated_data['enrollment'],
            name=validated_data['name'],
            branch=validated_data['branch']
        )

        student.save()

        return student


class ListStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class DetailStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
