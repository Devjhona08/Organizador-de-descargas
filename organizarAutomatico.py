import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Función principal de organización
def organizar_descargas():
    carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")

    subcarpetas = {
        "Documentos": [".pdf", ".docx", ".xlsx", ".pptx", ".txt"],
        "Imágenes": [".jpg", ".jpeg", ".png", ".gif"],
        "Vídeos": [".mp4", ".mov", ".avi"],
        "Programas": [".exe", ".msi"],
        "Comprimidos": [".zip", ".rar", ".7z"],
        "Otros": []
    }

    for archivo in os.listdir(carpeta_descargas):
        ruta_archivo = os.path.join(carpeta_descargas, archivo)

        if os.path.isfile(ruta_archivo):
            extension = os.path.splitext(archivo)[1].lower()
            movido = False

            for subcarpeta, extensiones in subcarpetas.items():
                if extension in extensiones:
                    carpeta_destino = os.path.join(carpeta_descargas, subcarpeta)
                    os.makedirs(carpeta_destino, exist_ok=True)
                    shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
                    movido = True
                    break

            if not movido:
                carpeta_destino = os.path.join(carpeta_descargas, "Otros")
                os.makedirs(carpeta_destino, exist_ok=True)
                shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))

# Clase de manejo de eventos
class DescargasHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            organizar_descargas()

if __name__ == "__main__":
    ruta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
    event_handler = DescargasHandler()
    observer = Observer()
    observer.schedule(event_handler, ruta_descargas, recursive=False)
    print(f"Monitoreando la carpeta: {ruta_descargas}")
    try:
        observer.start()
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
