# 📂 Organizador de Descargas en Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Estado](https://img.shields.io/badge/Estado-Activo-brightgreen)
![Licencia](https://img.shields.io/badge/Licencia-MIT-green)

Este proyecto contiene dos scripts en **Python** que ayudan a **mantener organizada la carpeta de Descargas** automáticamente, clasificando archivos en subcarpetas según su extensión (documentos, imágenes, vídeos, programas, etc.).

## ✨ Características
- Clasificación automática por tipo de archivo.  
- Carpetas creadas de manera dinámica si no existen.  
- Soporte para múltiples extensiones comunes.  
- Dos modos de uso disponibles:
  - **Versión 1** → ejecución manual.  
  - **Versión 2** → organización en tiempo real (monitoreo continuo).  

## 📌 Requisitos
- Python 3.x  
- Librerías usadas:
  - `os` (incluida en Python)  
  - `shutil` (incluida en Python)  
  - `watchdog` (solo en la versión 2 → instalar con `pip install watchdog`)  

## 🚀 Versiones

### 🔹 Versión 1 – Ejecución manual
Script: `organizar.py`

🔧 Cómo funciona:
- Recorre la carpeta `Descargas`.  
- Mueve cada archivo a su subcarpeta correspondiente.  
- Archivos sin categoría definida se mueven a `Otros`.  

▶️ **Ejecución**:
```bash
python organizarAutomatico.py

## Créditos

- **Autor:** Devjhona08

[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/devjhonatan08/)

## Soporte

Apoya mi trabajo y ayuda a que siga desarrollando herramientas y scripts como este. ¡Invítame un café! ☕

<a href="https://www.buymeacoffee.com/devjhonatan08" rel="nofollow"><img width="250" align="left">
![buy-me-a-coffe](https://github.com/user-attachments/assets/8c8f9e81-334e-469e-b25e-29888cfc9fcc)
</a>