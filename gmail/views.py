import httplib2
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

from apiclient import discovery
from oauth2client import client
from oauth2client import GOOGLE_TOKEN_URI


class EmailList(APIView):
    """
    List all emails of user.
    """

    def get(self, request, format=None):

        credentials = request.user.google_credential.credential
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('gmail', 'v1', http=http)

        emails = []
        streams = service.users().messages().list(userId='me', maxResults=100).execute()

        def insert_animal(request_id, response, exception):
            if exception is not None:
                pass
            else:
                emails.append(response)

        batch = service.new_batch_http_request(callback=insert_animal)
        for stream in streams.get('messages'):
            email_id = stream.get('id')
            batch.add(service.users().messages().get(userId='me', id=email_id, format='minimal'))

        batch.execute(http=http)

        return Response(emails)