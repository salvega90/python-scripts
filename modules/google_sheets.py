from __future__ import print_function
import pickle
import os.path
import webbrowser
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '11aQWWmfUCInhLOEgt2D9rjNna79s4dgKGG_WfBfM82A'
RANGE = 'Sheet1!B2'
CLEAR_RANGE = RANGE + ':L12'


class GoogleShit:
    def __init__(self):
        self.butt = ""
        self.service = build('sheets', 'v4', credentials=self._authenticate())

    @staticmethod
    def _authenticate():
        """Shows basic usage of the Sheets API.
                Prints values from a sample spreadsheet.
                """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'useful_stuff/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        return creds

    def write_to_sheet(self, values):
        data = [
            {
                'range': RANGE,
                'values': values
            },
        ]
        body = {
            'valueInputOption': "USER_ENTERED",
            'data': data
        }
        result = self.service.spreadsheets().values().batchUpdate(
            spreadsheetId=SPREADSHEET_ID, body=body).execute()
        print('{0} cells updated.'.format(result.get('totalUpdatedCells')))

    @staticmethod
    def open_sheet():
        """
        Opens up the google sheet in a new tab in your Chrome Web browser
        :return:
        """
        return webbrowser.get(using='chrome').open(
            f'https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}', new=2)

    def clear_cells(self):
        request = self.service.spreadsheets().values().clear(spreadsheetId=SPREADSHEET_ID,
                                                             range=CLEAR_RANGE,
                                                             body={})
        response = request.execute()

        # TODO: Change code below to process the `response` dict:
        print(response)
