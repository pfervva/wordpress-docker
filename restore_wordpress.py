import os
import subprocess
import sys

# python restore_wordpress.py nombre_del_backup.tar.gz

def restore_wordpress(backup_file):
    # Variables de configuración
    CONTAINER_NAME = 'wordpress_production'
    BACKUP_DIR = './backups'
    
    backup_path = os.path.join(BACKUP_DIR, backup_file)

    # Comprobar si el archivo de backup existe
    if not os.path.exists(backup_path):
        raise FileNotFoundError(f"El archivo de backup no se encontró: {backup_path}")

    # Comando para restaurar los archivos de WordPress
    command = (
        f"docker exec -i {CONTAINER_NAME} tar -xzf - -C /var/www/html < {backup_path}"
    )

    # Ejecutar el comando
    subprocess.run(command, shell=True, check=True)
    print(f"Restauración de archivos de WordPress desde {backup_path} completada")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python restore_wordpress.py <archivo_backup.tar.gz>")
        sys.exit(1)

    backup_file = sys.argv[1]
    restore_wordpress(backup_file)
