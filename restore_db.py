import os
import subprocess
import sys

# python restore_db.py nombre_del_backup.sql.gz

def restore_db(backup_file):
    # Variables de configuración
    WORDPRESS_DB_USER = 'exampleuser'
    WORDPRESS_DB_PASSWORD = 'examplepass'
    WORDPRESS_DB_NAME = 'exampledb'
    CONTAINER_NAME = 'mysql_production'
    BACKUP_DIR = './backups'
    
    backup_path = os.path.join(BACKUP_DIR, backup_file)

    # Comprobar si el archivo de backup existe
    if not os.path.exists(backup_path):
        raise FileNotFoundError(f"El archivo de backup no se encontró: {backup_path}")

    # Comando para restaurar la base de datos
    command = (
        f"gunzip < {backup_path} | docker exec -i {CONTAINER_NAME} /usr/bin/mysql "
        f"-u {WORDPRESS_DB_USER} -p{WORDPRESS_DB_PASSWORD} {WORDPRESS_DB_NAME}"
    )

    # Ejecutar el comando
    subprocess.run(command, shell=True, check=True)
    print(f"Restauración de la base de datos desde {backup_path} completada")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python restore_db.py <archivo_backup.sql.gz>")
        sys.exit(1)

    backup_file = sys.argv[1]
    restore_db(backup_file)
