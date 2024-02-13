import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class ApiSheets:
    def __init__(self, name_sheet, interval):
        self._SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
        self._SAMPLE_SPREADSHEET_ID = "11-Oa_qviwhrskORVfhrEWN2OLxfpMLavpwcto7LSbVs"
        self._SAMPLE_RANGE_NAME = f"{name_sheet}!{interval}"
        
    # Redeems a Google API access authentication token
    def _autenticate(self):
        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", self._SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", self._SCOPES
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        return creds

    # Returns all data in sheet
    def get_data(self):
        try:
            service = build("sheets", "v4", credentials=self._autenticate())

            sheet = service.spreadsheets()
            result = (
                sheet.values().get(spreadsheetId=self._SAMPLE_SPREADSHEET_ID, range=self._SAMPLE_RANGE_NAME).execute()
            )
            return result["values"]
        except HttpError as err:
            print(err)
    
    # Refreshes or creates new data in the table
    def update_and_write_data(self, interval_row, value: list, option="USER_ENTERED"):
        try:
            service = build("sheets", "v4", credentials=self._autenticate())

            sheet = service.spreadsheets()

            result = sheet.values().update(spreadsheetId=self._SAMPLE_SPREADSHEET_ID, range=interval_row, valueInputOption=option, body={"values": value}).execute()
            
        
        except HttpError as err:
            print(err)

