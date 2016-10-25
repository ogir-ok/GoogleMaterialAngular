from django.contrib.auth.models import User
from django.db import models
from oauth2client.contrib.django_util.models import CredentialsField

class GoogleCredentials(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='google_credential')
    credential = CredentialsField()