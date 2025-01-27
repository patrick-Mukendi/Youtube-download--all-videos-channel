import os
import subprocess

def download_videos():
    print("=== YouTube Video Downloader ===")
    
    # Demander le lien de la chaîne
    channel_url = input("Entrez le lien de la chaîne YouTube : ").strip()
    if not channel_url:
        print("Le lien est vide. Veuillez réessayer.")
        return
    
    # Demander l'emplacement de téléchargement
    download_path = input("Entrez l'emplacement pour enregistrer les vidéos : ").strip()
    if not os.path.exists(download_path):
        print(f"Le chemin {download_path} n'existe pas. Voulez-vous le créer ? (oui/non)")
        create_folder = input("> ").strip().lower()
        if create_folder == "oui":
            os.makedirs(download_path)
            print(f"Dossier créé : {download_path}")
        else:
            print("Opération annulée.")
            return

    # Commande yt-dlp
    command = [
        "yt-dlp", 
        "-f", "best", 
        "-ciw", 
        "--yes-playlist", 
        "-o", f"{download_path}/%(title)s.%(ext)s", 
        channel_url
    ]
    
    # Lancer la commande dans le terminal
    try:
        subprocess.run(command, check=True)
        print("\n=== Téléchargement terminé avec succès ! ===")
    except subprocess.CalledProcessError as e:
        print("\nUne erreur s'est produite lors du téléchargement.")
        print(f"Erreur : {e}")

# Lancer le programme
if __name__ == "__main__":
    download_videos()
