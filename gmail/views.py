import datetime
import httplib2
from collections import defaultdict

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apiclient import discovery


class EmailList(APIView):
    """
    List all emails of user.
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        credentials = request.user.google_credential.credential
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('gmail', 'v1', http=http)

        emails = []
        streams = service.users().messages().list(userId='me', maxResults=100).execute()

        # Can be done as not inplace function
        def process_email(request_id, response, exception):
            if exception is not None:
                # @TODO: add some errors if API fails
                pass
            else:
                emails.append(response)

        batch = service.new_batch_http_request(callback=process_email)
        for stream in streams.get('messages'):
            email_id = stream.get('id')
            batch.add(service.users().messages().get(userId='me', id=email_id, format='metadata', metadataHeaders=['From', 'Subject']))
        batch.execute(http=http)

        # @NOTE: probably it can be done in serializers
        grouped_emails = defaultdict(list)
        for email in emails:
            mail = {'Snippet': email.get('snippet')}
            for header in email.get('payload', {}).get('headers'):
                mail[header.get('name')] = header.get('value')
            timestamp = int(email.get('internalDate')) / 1000
            date = datetime.date.fromtimestamp(timestamp)
            grouped_emails[date].append(mail)

        res = [{'date': k, 'emails': grouped_emails[k]} for k in sorted(grouped_emails.keys(), reverse=True)]

        return Response(res)
