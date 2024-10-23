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
    message = f"Alerte Mehdi : Le disque {disk} a atteint {percent_used:.2f}% de son espace."
    print(message)
    
    # Envoi d'un email (à configurer avec ton propre serveur SMTP)
    send_email("Alerte Espace Disque", message)

# Fonction pour envoyer un email
def send_email(subject, body):
    from_email = "akamimehdi.dev@gmail.com"  # Ton email Gmail
    password = "YOUR-PASSWORD"  # Remplace par le mot de passe d'application généré
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
    usage_threshold = 80
    
    check_disk_usage(disk_to_monitor, usage_threshold)
