from django.db import models
from django.core.validators import RegexValidator, FileExtensionValidator


class Student(models.Model):

    name = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[^\W\d_]+(?:\s+[^\W\d_]+)*$',
                message='Name must contain letters only.'
            )
        ]
    )

    university_id = models.IntegerField(
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[12]\d{8}$',
                message='University ID must start with 1 or 2 and contain 9 digits.'
            )
        ]
    )

    id_number = models.IntegerField(
        validators=[
            RegexValidator(
                regex=r'^[984]\d{8}$',
                message='ID Number must start with 9, 8, or 4 and contain 9 digits.'
            )
        ]
    )

    mobile_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^(059|056)\d{7}$',
                message='Mobile number must start with 059 or 056 and contain 10 digits.'
            )
        ]
    )

    address = models.CharField(max_length=150)

    date_of_birth = models.DateField()

    image = models.ImageField(
        upload_to='student_images/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg', 'png']
            )
        ]
    )

    def __str__(self):
        return self.name