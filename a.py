from googleapiclient.discovery import build
from google.oauth2 import service_account
import io
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload

SERVICE_ACCOUNT_FILE = "service_account.json"
PARENT_FOLDER_ID = "19KD1YwYT5plTs9q1XuTJ8LO7lWIBHxrf"

def authenticate():
    # Load service account credentials from JSON file
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=['https://www.googleapis.com/auth/drive']  # Include the scope here
    )
    # Create a service object for interacting with the Google Drive API
    service = build('drive', 'v3', credentials=creds)
    return service

def upload_photo(file_path):
    service = authenticate()
    file_metadata = {
        'name': "Hello",
        'parents': [PARENT_FOLDER_ID]
    }
    media = MediaFileUpload(file_path)
    file = service.files().create(body=file_metadata, media_body=media).execute()

def download_photo(file_id, dest_path):
    service = authenticate()
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(dest_path, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

# Other functions...

# Example usage
file_id = get_file_id('lamp.png', PARENT_FOLDER_ID)
download_photo(file_id, 'downloaded_file.png')
update_photo(file_id, "C:\TPs\Ateliers\ATELIER_DEV_WEB\Images\lightv1.png")
# upload_photo("C:\TPs\Ateliers\ATELIER_DEV_WEB\Images\lightv1.png")
