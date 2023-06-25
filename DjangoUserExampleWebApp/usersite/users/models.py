import uuid
from django.db import models
from django.contrib.auth.models import User

# TODO: add the combination with user
class AccessKey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    profile = models.ForeignKey('Profile', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return f'{self.profile.user.username}: {self.id}'    

# Create your models here.
class Profile(models.Model):
    # on_delete=models.CASCADE means when user been deleted, this profile will also be deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'name: {self.user.username}, email: {self.user.email}, last_login: {self.user.last_login}'

