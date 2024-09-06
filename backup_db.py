import os
import subprocess
from datetime import datetime

# Variables de configuración
WORDPRESS_DB_USER = 'exampleuser'
WORDPRESS_DB_PASSWORD = 'examplepass'
WORDPRESS_DB_NAME = 'exampledb'
CONTAINER_NAME = 'mysql_production'
BACKUP_DIR = './backups'
TIMESTAMP = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
BACKUP_FILE = f"{BACKUP_DIR}/mysql_backup_{TIMESTAMP}.sql.gz"

# Crear directorio de backups si no existe
os.makedirs(BACKUP_DIR, exist_ok=True)

# Comando para realizar el backup y comprimirlo
command = (
    f"docker exec {CONTAINER_NAME} /usr/bin/mysqldump -u {WORDPRESS_DB_USER} "
    f"-p{WORDPRESS_DB_PASSWORD} {WORDPRESS_DB_NAME} | gzip > {BACKUP_FILE}"
)

# Ejecutar el comando
subprocess.run(command, shell=True, check=True)

print(f"Backup de la base de datos realizado en {BACKUP_FILE}")
