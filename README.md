# Téléchargeur de vidéos YouTube avec yt-dlp

Ce projet est une application de terminal basée sur Python qui utilise l'outil puissant `yt-dlp` pour télécharger des vidéos ou playlists à partir de YouTube avec une grande flexibilité.

---

## Fonctionnalités

- Télécharge des vidéos et playlists complètes de YouTube.
- Organise les vidéos téléchargées avec des noms et extensions appropriés.
- Permet de spécifier l'emplacement de téléchargement.
- Gère les erreurs pour assurer un téléchargement fluide.

---

## Prérequis

### Outils nécessaires

- **Python 3.x** :
  Assurez-vous que Python est installé sur votre machine.
  Téléchargez-le depuis [python.org](https://www.python.org/).

- **yt-dlp** :
  Installez `yt-dlp` via pip :
  ```bash
  pip install -U yt-dlp
  ```

### Vérification de l'installation

Pour vérifier que `yt-dlp` est installé, exécutez :
```bash
yt-dlp --version
```

---

## Installation

1. Clonez ce dépôt GitHub :
   ```bash
   git clone https://github.com/your-username/yt-dlp-downloader.git
   ```

2. Accédez au répertoire du projet :
   ```bash
   cd yt-dlp-downloader
   ```

---

## Utilisation

### Commande de lancement

Exécutez le script Python dans votre terminal :
```bash
python3 youtube_downloader.py
```

### Processus étape par étape

1. **Entrez le lien YouTube** :
   - Par exemple : `https://www.youtube.com/c/ExampleChannel`.

2. **Spécifiez le dossier de destination** :
   - Linux/MacOS : `/home/user/Videos/`
   - Windows : `C:\Users\YourName\Videos\`

3. **Patientez** pendant le téléchargement. Les vidéos seront enregistrées au chemin spécifié.

---

## Commandes alternatives avec yt-dlp

Vous pouvez également exécuter directement `yt-dlp` pour personnaliser les téléchargements. Voici quelques exemples :

- Télécharger une vidéo spécifique :
  ```bash
  yt-dlp "<lien de la vidéo>"
  ```

- Télécharger une playlist complète :
  ```bash
  yt-dlp --yes-playlist "<lien de la playlist>"
  ```

- Spécifier un chemin de sortie personnalisé :
  ```bash
  yt-dlp -o "/chemin/vers/dossier/%(title)s.%(ext)s" "<lien>"
  ```

---

## Exemple de sortie

### Entrée :
```
Entrez le lien de la chaîne YouTube : https://www.youtube.com/c/ExampleChannel
Entrez l'emplacement pour enregistrer les vidéos : /home/user/Videos/
```

### Sortie :
```
=== Téléchargeur de vidéos YouTube ===
Téléchargement en cours...
=== Téléchargement terminé avec succès ! ===
```

---

## Ressources utiles

- [Documentation officielle de yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [Télécharger Python](https://www.python.org/)

---

## Contribution

Les contributions sont les bienvenues ! Veuillez :

1. Forker ce dépôt.
2. Créer une branche pour vos modifications :
   ```bash
   git checkout -b feature/ma-modification
   ```
3. Soumettre une Pull Request.

---

## Remarque finale

Si vous rencontrez un problème ou avez des suggestions, veuillez ouvrir une issue sur ce dépôt. 
Merci de contribuer à rendre cet outil encore meilleur !
Patrick Mukendi

------------------------------

# YouTube Channel Video Cloner

#📜 Description

YouTube Channel Video Cloner est un script Python qui :

Télécharge toutes les vidéos d'une chaîne YouTube (Chaîne A) à l'aide de yt-dlp.
Ré-upload ces vidéos sur une autre chaîne YouTube (Chaîne B) en utilisant l'API YouTube Data v3.

# ⚠️ Important : Veuillez respecter les droits d'auteur. Assurez-vous d'avoir l'autorisation explicite de la Chaîne A avant d'utiliser leurs vidéos.

----------------------------------------

#🚀 Fonctionnalités

Téléchargement de vidéos : Télécharge automatiquement toutes les vidéos d'une chaîne YouTube.

Upload sur une autre chaîne : Re-upload les vidéos sur une autre chaîne via l'API YouTube Data.

Personnalisation facile : Vous pouvez définir le titre, la description, les tags et la confidentialité des vidéos.

-------------------------------------

#🛠️ Prérequis

 - Logiciels et bibliothèques
Python 3.7+ yt-dlp

- google-auth-oauthlib
- google-api-python-client
- Compte Google API
  
Créez un projet sur Google Cloud Console.
Activez l'API YouTube Data v3.
Configurez un OAuth 2.0 Client ID et téléchargez le fichier client_secrets.json.
---

#📦 Installation

Clonez ce dépôt :

'''bash (Copier, Modifier)
git clone https://github.com/<votre_nom_d_utilisateur>/youtube-channel-cloner.git
cd youtube-channel-cloner
'''

Installez les dépendances :

'''bash (Copier, Modifier)
pip install -r requirements.txt
'''

Placez le fichier client_secrets.json (obtenu depuis la console Google Cloud) dans le répertoire principal.

------------------------------------

#📚 Utilisation

1. Télécharger les vidéos de la chaîne A
Exécutez la commande suivante pour télécharger toutes les vidéos d'une chaîne YouTube :

'''bash 
yt-dlp -f best -o "videos/%(title)s.%(ext)s" https://www.youtube.com/c/<NomDeLaChaîneA>/videos
'''

Remplacez <NomDeLaChaîneA> par le nom ou l'URL de la chaîne cible.
Les vidéos seront téléchargées dans le dossier videos. 

2. Configurer l'upload
   
Modifiez les paramètres dans le script Python upload_videos.py pour personnaliser :
- Le titre
- La description
- Les tags
- La confidentialité (public, privé, non répertorié).
  
1. Uploader les vidéos sur la chaîne B
Exécutez le script Python pour uploader les vidéos sur la chaîne B :

'''bash
python upload_videos.py
'''

--------------------------------

#📋 Exemple de Configuration

upload_videos.py (extrait)

'''python
upload_video(
    youtube,
    file_path="videos/video1.mp4",
    title="Titre personnalisé",
    description="Description de la vidéo",
    tags=["tag1", "tag2"],
    category_id="22"  # Catégorie : 22 pour "People & Blogs"
)
'''

-------------------------------

#🚨 Avertissements

Respect des droits d'auteur : N'utilisez pas ce script pour télécharger ou re-upload des vidéos sans autorisation.

Quotas de l'API YouTube : Assurez-vous de ne pas dépasser les limites quotidiennes imposées par l'API.
Vérifiez les politiques YouTube : Ce projet est destiné à des usages légitimes uniquement.

-------------------------------

#🛠️ Développement

Pour contribuer :

Forkez le projet.

- Créez une branche :

'''bash
git checkout -b feature/ma-feature
'''

- Commitez vos modifications :

'''bash 
git commit -m "Ajout d'une nouvelle fonctionnalité"
'''

- Poussez votre branche :

'''bash 
git push origin feature/ma-feature
'''

- Ouvrez une Pull Request.

-------------------------------

#🧑‍💻 Auteur

Patrick Mukendi Nyanguila

Développeur passionné mobile et web
*Gmail [mdipatrick5@gmail.com]

-------------------------------
#📄 Licence
Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus d'informations.
