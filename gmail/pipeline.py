import datetime
from django.conf import settings
from oauth2client import GOOGLE_REVOKE_URI, GOOGLE_TOKEN_URI
from oauth2client.client import OAuth2Credentials, _extract_id_token
from .models import GoogleCredentials


def set_google_credentials(strategy, details, response, user=None, *args, **kwargs):
    if user:
        token_expiry = datetime.datetime.utcnow() + datetime.timedelta(seconds=int(response.get('expires_in')))
        id_token = _extract_id_token(response.get('id_token'))
        credential = OAuth2Credentials(
            access_token=response.get('access_token'),
            client_id=settings.GOOGLE_OAUTH2_CLIENT_ID,
            client_secret=settings.GOOGLE_OAUTH2_CLIENT_SECRET,
            refresh_token=response.get('refresh_token'),
            token_expiry=token_expiry,
            token_uri=GOOGLE_TOKEN_URI,
            user_agent=None,
            revoke_uri=GOOGLE_REVOKE_URI,
            id_token=id_token,
            token_response=response)

        google_credential, is_created = GoogleCredentials.objects.get_or_create(user=user)
        google_credential.credential = credential
        google_credential.save()
