from django.db import models
from .student_helper import calculate_age
from .student_choices import GENDER_CHOICES


class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default="Female")

    def save(self, *args, **kwargs):
        self.age = calculate_age(self.dob)
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
