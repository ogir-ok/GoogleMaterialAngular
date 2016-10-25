from django.contrib.auth.models import User
from django.db import models
from oauth2client.contrib.django_util.models import CredentialsField

class GoogleCredentials(models.Model):
    """
    Model to store google credentioal
    (found in best practices for google api + django)
    """
    user = models.OneToOneField(User, primary_key=True, related_name='google_credential')
    credential = CredentialsField()