from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Teacher

User = get_user_model()


class CreateTeacherSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(source='user.password')

    class Meta:
        model = Teacher
        exclude = ['user']

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['user']['email'],
            password=validated_data['user']['password']
        )

        user.set_password(user.password)
        user.is_staff = True
        user.save()

        # add user to teacher group
        group = Group.objects.get(name='teacher')
        group.user_set.add(user)

        student = Teacher.objects.create(
            user=user,
            teacher_id=validated_data['teacher_id'],
            teacher_name=validated_data['teacher_name'],
            teacher_department=validated_data['teacher_department']
        )

        student.save()

        return student


class ListTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
