from django.db import models
import uuid


def get_profile_image_path(self, filename):
    return f'property_images/non-residential/property/{self.pk}/{str(uuid.uuid4())}.png'


class NonResidentialProperty(models.Model):
    PROPERTY_SM_BARAK = 1
    PROPERTY_MT_SHED = 2
    PROPERTY_PARK_FUTSAL= 3

    PROPERTY_CHOICES = (
        (PROPERTY_SM_BARAK, 1),
        (PROPERTY_MT_SHED, 2),
        (PROPERTY_PARK_FUTSAL, 3)
    )

    name = models.CharField(max_length=100)
    bk_no = models.CharField(max_length=100, unique=True)
    loc = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    image = models.ImageField(max_length=255, upload_to=get_profile_image_path, null=True, blank=True)
    type = models.IntegerField(default=PROPERTY_SM_BARAK, choices=PROPERTY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', related_name='+', blank=True, null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('User', related_name='+', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
