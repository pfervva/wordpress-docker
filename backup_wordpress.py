import os
import subprocess
from datetime import datetime

# Variables de configuración
CONTAINER_NAME = 'wordpress_production'
BACKUP_DIR = './backups'
TIMESTAMP = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
BACKUP_FILE = f"{BACKUP_DIR}/wordpress_backup_{TIMESTAMP}.tar.gz"

# Crear directorio de backups si no existe
os.makedirs(BACKUP_DIR, exist_ok=True)

# Comando para realizar el backup y comprimirlo
command = (
    f"docker exec {CONTAINER_NAME} tar -czf - /var/www/html | gzip > {BACKUP_FILE}"
)

# Ejecutar el comando
subprocess.run(command, shell=True, check=True)

print(f"Backup de archivos de WordPress realizado en {BACKUP_FILE}")
