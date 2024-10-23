# Script de Surveillance de l'Espace Disque avec Alerte Email

## Description 📄

Ce script Python surveille l'utilisation de l'espace disque et envoie une alerte par email si l'occupation dépasse un certain seuil. Il est particulièrement utile pour éviter que le disque ne se remplisse complètement, ce qui peut entraîner des ralentissements ou des erreurs.

## Fonctionnalités 🔧

- 📊 Vérifie l'espace utilisé sur le disque spécifié.
- 📧 Envoie une alerte par email lorsque l'espace disque dépasse un seuil défini.
- 🔧 Facile à personnaliser pour surveiller d'autres disques et ajuster le seuil de déclenchement.

## Installation 📥

### Prérequis

1. **Python installé** : Assure-toi d'avoir Python installé sur ton système.
2. **Mot de passe d'application Gmail** : Si tu utilises Gmail pour l'alerte email, tu dois générer un mot de passe d'application. Voici comment faire :

   - Connecte-toi à ton compte Google.
   - Active la validation en deux étapes (2FA) dans [la sécurité de ton compte](https://myaccount.google.com/security).
   - Génère un [mot de passe d'application](https://myaccount.google.com/apppasswords) pour l'utiliser dans le script.

### Étapes d'installation

1. **Cloner ce repository** sur ton système :
   ```bash
   git clone https://github.com/tonutilisateur/surveillance-espace-disque.git
   ```

2. **Configurer les paramètres SMTP :**

- Ouvre le fichier surveillance_disque.py.
- Remplace TON_MOT_DE_PASSE_APPLICATION par le mot de passe d'application que tu as généré dans ton compte Google.

3. **Exécuter le script :**
   
   ```bash
   python surveillance_disque.py
   ```

### Personnalisation ⚙️

Modifier le seuil d'alerte
Par défaut, le script est configuré pour déclencher une alerte lorsque l'espace disque utilisé dépasse 56%. Tu peux ajuster ce seuil en modifiant la variable usage_threshold dans le script :

```bash
usage_threshold = 56  # Seuil par défaut, ajuster selon ton besoin
```
### Modifier le disque surveillé 

Par défaut, le script surveille le disque C:. Si tu souhaites surveiller un autre disque, tu peux modifier la variable disk_to_monitor :

```bash
disk_to_monitor = "D:\\"  # Par exemple pour surveiller le disque D:
``` 
### Script Python 🖥️

Voici le script complet :

```bash
import shutil
import smtplib
from email.mime.text import MIMEText

# Fonction pour vérifier l'occupation du disque
def check_disk_usage(disk, threshold):
    total, used, free = shutil.disk_usage(disk)
    # Convertir en pourcentage
    percent_used = (used / total) * 100
    print(f"Espace utilisé sur {disk}: {percent_used:.2f}%")
    
    # Si l'espace utilisé dépasse le seuil
    if percent_used > threshold:
        alert_user(percent_used, disk)

# Fonction pour alerter l'utilisateur (ex. via email)
def alert_user(percent_used, disk):
    message = f"Alerte : Le disque {disk} a atteint {percent_used:.2f}% de son espace."
    print(message)
    
    # Envoi d'un email (à configurer avec ton propre serveur SMTP)
    send_email("Alerte Espace Disque", message)

# Fonction pour envoyer un email
def send_email(subject, body):
    from_email = "akamimehdi.dev@gmail.com"  # Ton email Gmail
    password = "TON_MOT_DE_PASSE_APPLICATION"  # Remplace par le mot de passe d'application généré
    to_email = "akamimehdi.dev@gmail.com"     # Email où tu veux recevoir l'alerte
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email
    
    try:
        # Connexion au serveur SMTP de Gmail
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
        print("Email envoyé avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email: {e}")

if __name__ == "__main__":
    # Chemin du disque à surveiller (par exemple C:\ pour Windows)
    disk_to_monitor = "C:\\"
    # Seuil d'alerte (ici 56% pour tester rapidement)
    usage_threshold = 56
    
    check_disk_usage(disk_to_monitor, usage_threshold)

``` 

### Automatisation 🕒

Planifier l'exécution automatique du script avec le Planificateur de tâches Windows
1. **Ouvrir le Planificateur de tâches :**

- Dans le menu démarrer de Windows, tape "Planificateur de tâches" et ouvre l'application.
2. **Créer une nouvelle tâche :**

- Dans le menu à droite, clique sur Créer une tâche.
- Donne un nom à ta tâche, par exemple Surveillance Espace Disque.
- Coche Exécuter avec les autorisations maximales pour garantir que le script a les droits nécessaires.
3. **Configurer un déclencheur :**

- Va dans l'onglet **Déclencheurs** et clique sur Nouveau.
- Choisis quand tu veux que la tâche se déclenche, par exemple tous les jours à une heure spécifique.
- Clique sur **OK**.
  
4. **Configurer l'action (lancer le script) :**

- Va dans l'onglet **Action**s et clique sur **Nouveau**.
- Dans **Programme/script**, tape python.
- Dans **Ajouter des arguments**, entre le chemin complet vers ton script Python. Par exemple :

   ```bash
    C:\Scripts\surveillance_disque.py
   ```
- Clique sur OK.

5. **Finaliser la tâche :**

- Vérifie que tout est configuré correctement, puis clique sur OK pour sauvegarder la tâche.
- Tu peux tester en faisant un clic droit sur la tâche et en sélectionnant **Exécuter**.

### Test de l'alerte 📧

Pour simuler un test immédiat :

- Le script est actuellement configuré pour envoyer une alerte à 56% d'utilisation du disque (ce qui correspond à la situation actuelle du disque C: de ton système).
- Exécute le script pour vérifier que tu reçois bien un email d'alerte dans ta boîte Gmail.

### Auteur 👨‍💻

- Mehdi Akami - [Mon profil GitHub](https://github.com/akamidev)
  
### Licence 📜

Ce projet est sous licence MIT. Consulte le fichier [LICENSE](https://github.com/akamidev/surveillance_disque/blob/main/LICENSE) pour plus d'informations.    


### Explication des sections :

- **Description** : Explique ce que fait le script et pourquoi il est utile.
- **Fonctionnalités** : Liste les fonctionnalités principales du script.
- **Installation** : Fournit des instructions pour cloner le projet, configurer Gmail, et exécuter le script.
- **Personnalisation** : Indique comment modifier le seuil d'alerte et le disque surveillé.
- **Script Python** : Contient le code du script complet.
- **Automatisation** : Explique comment planifier l'exécution du script avec le Planificateur de tâches.
- **Test de l'alerte** : Guide pour vérifier si l'alerte email fonctionne correctement.
