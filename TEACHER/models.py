from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length=10, primary_key=True)
    teacher_name = models.CharField(max_length=225)
    teacher_department = models.CharField(max_length=2)

    class Meta:
        db_table = 'tbl_teacher'

    def __str__(self):
        return self.teacher_id
