import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload

# Configuration
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def authenticate_youtube():
    # Authentification OAuth 2.0
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        "client_secrets.json", SCOPES
    )
    credentials = flow.run_console()
    return googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

def upload_video(youtube, file_path, title, description, tags, category_id="22"):
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": tags,
                "categoryId": category_id,
            },
            "status": {
                "privacyStatus": "public",  # Changez à "private" ou "unlisted" si nécessaire
            },
        },
        media_body=MediaFileUpload(file_path),
    )
    response = request.execute()
    print(f"Vidéo uploadée : {response['id']}")

if __name__ == "__main__":
    # Dossier contenant les vidéos téléchargées
    video_folder = "path_to_downloaded_videos"
    
    # Authentification
    youtube = authenticate_youtube()
    
    # Itérer sur les vidéos et les uploader
    for video_file in os.listdir(video_folder):
        if video_file.endswith(".mp4"):  # Assurez-vous que ce sont des vidéos
            file_path = os.path.join(video_folder, video_file)
            upload_video(
                youtube,
                file_path,
                title=video_file.replace(".mp4", ""),  # Utilisez le nom du fichier comme titre
                description="Cloned video from Channel A",
                tags=["tag1", "tag2"],  # Ajoutez vos tags ici
            )
