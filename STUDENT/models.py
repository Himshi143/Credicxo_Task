from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    enrollment = models.CharField(max_length=12, primary_key=True)
    branch = models.CharField(max_length=2, null=False, blank=False)

    class Meta:
        db_table = 'tbl_students'

    def __str__(self):
        return self.enrollment
