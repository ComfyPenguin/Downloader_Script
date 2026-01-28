# Descargador de Videos con YT-DLP

Script interactivo en Python para descargar videos de **YouTube** o **Twitter/X** en múltiples formatos.

## Formatos Disponibles

### YouTube

- **MP3** - Solo audio en formato MP3
- **MP4** - Video en formato MP4
- **MKV** - Video en formato MKV (alta calidad)

### Twitter/X

- **MP3** - Solo audio en formato MP3
- **MP4** - Video en formato MP4
- **GIF** - Convertir video a GIF animado

## Requisitos

- Python 3.6 o superior

El script verifica e instala automáticamente:

- `inquirer` - Para el menú interactivo
- `yt-dlp` - Para descargar los videos

**Solo necesitas instalar manualmente**, python y pip si no los tienes.

[Python](https://www.python.org/downloads/)

Una vez instalado Python, pip viene incluido.

## Uso

### En Windows

1. Abre una terminal (cmd o PowerShell).
2. Navega o mueve el script `descargar.py` a la carpeta donde quieres que se guarden los videos descargados.
3. Ejecuta el script:
   - Mediante cmd:

    ```cmd
    python descargar.py
    ```

   - Simplemente haciendo doble clic en `descargar.py` si tienes Python asociado a archivos `.py`.
4. El video se descargará en la carpeta actual con el título original.

### En Linux

1. Ejecuta el script:

   ```bash
   python descargar.py
   ```

2. El video se descargará en la carpeta actual con el título original

## Ejemplo de Uso

```text
¿De dónde quieres descargar?
  > YouTube
    Twitter/X

Elige el formato para YouTube
    mp3
  > mp4
    mkv

Ingresa la URL del video: https://www.youtube.com/watch?v=...

Descarga completada exitosamente!
```

## Notas Técnicas

- Los videos de YouTube se descargan en la **máxima calidad disponible**
- Los archivos se guardan con el título original del video
- Compatible con Windows y Linux
