from django.db import models
import uuid


def get_profile_image_path(self, filename):
    return f'property_images/maintenance/{self.pk}/{str(uuid.uuid4())}.png'


class OfficerMaintenance(models.Model):
    description = models.CharField(max_length=100)
    cost = models.FloatField()
    image = models.ImageField(max_length=255, upload_to=get_profile_image_path, null=True, blank=True)
    officer_property = models.ForeignKey('OfficerProperty', related_name='maintenance', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', related_name='+', blank=True, null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('User', related_name='+', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
