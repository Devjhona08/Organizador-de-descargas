import os
import shutil

def organizar_descargas():
    # Definir la carpeta de descargas
    carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")

    # Definir las subcarpetas y extensiones
    subcarpetas = {
        "Documentos": [".pdf", ".docx", ".xlsx", ".pptx", ".txt"],
        "Imágenes": [".jpg", ".jpeg", ".png", ".gif"],
        "Vídeos": [".mp4", ".mov", ".avi"],
        "Programas": [".exe", ".msi"],
        "Comprimidos": [".zip", ".rar", ".7z"],
        "Otros": []  # Archivos que no coincidan con ninguna extensión
    }

    # Iterar sobre los archivos en la carpeta de descargas
    for archivo in os.listdir(carpeta_descargas):
        ruta_archivo = os.path.join(carpeta_descargas, archivo)

        # Verificar si es un archivo
        if os.path.isfile(ruta_archivo):
            # Obtener la extensión del archivo
            extension = os.path.splitext(archivo)[1].lower()
            movido = False

            # Clasificar el archivo según su extensión
            for subcarpeta, extensiones in subcarpetas.items():
                if extension in extensiones:
                    carpeta_destino = os.path.join(carpeta_descargas, subcarpeta)
                    os.makedirs(carpeta_destino, exist_ok=True)
                    shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
                    movido = True   
                    break

            # Mover archivos que no coincidan a la carpeta "Otros"
            if not movido:
                carpeta_destino = os.path.join(carpeta_descargas, "Otros")
                os.makedirs(carpeta_destino, exist_ok=True)
                shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))

# Verificar si el script se ejecuta como principal
if __name__ == "__main__":
    organizar_descargas()
