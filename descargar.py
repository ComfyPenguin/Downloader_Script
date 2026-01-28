import subprocess
import sys

def verificar_e_instalar_dependencias():
    """
    Verifica si están instalados los paquetes necesarios y los instala si faltan.
    """
    dependencias = {
        'inquirer': 'inquirer',
        'yt-dlp': 'yt-dlp'
    }
    
    falta_alguna = False
    dependencias_faltantes = []
    
    # Primero verificar cuáles faltan
    for paquete, nombre_pip in dependencias.items():
        try:
            # Intentar importar inquirer
            if paquete == 'inquirer':
                __import__(paquete)
            # Verificar yt-dlp ejecutándolo
            elif paquete == 'yt-dlp':
                resultado = subprocess.run(['yt-dlp', '--version'], 
                                         capture_output=True, 
                                         text=True)
                if resultado.returncode != 0:
                    raise Exception("yt-dlp no está disponible")
            
        except (ImportError, Exception):
            falta_alguna = True
            dependencias_faltantes.append((paquete, nombre_pip))
    
    # Solo mostrar mensajes si falta algo
    if falta_alguna:
        print("Verificando dependencias...")
        
        for paquete, nombre_pip in dependencias_faltantes:
            print(f"⚠️  {paquete} no está instalado. Instalando...")
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', nombre_pip])
                print(f"✅ {paquete} instalado exitosamente")
            except subprocess.CalledProcessError:
                print(f"❌ Error al instalar {paquete}")
                print(f"Por favor, instala manualmente con: pip install {nombre_pip}")
                sys.exit(1)
        
        print("✅ Todas las dependencias están listas!\n")

def descargar_youtube(url, formato):
    """
    Descarga un video de YouTube en la máxima calidad y lo convierte al formato indicado.
    
    :param url: Enlace del video de YouTube
    :param formato: mp3, mp4 o mkv
    """
    if formato not in ["mp3", "mp4", "mkv"]:
        raise ValueError("Formato no válido. Usa: mp3, mp4 o mkv")

    # Comando base
    comando = ["yt-dlp", "-f", "bestvideo+bestaudio/best"]

    if formato == "mp3":
        # Extraer solo audio y convertir a mp3
        comando += ["--extract-audio", "--audio-format", "mp3", "-o", "%(title)s.%(ext)s"]
    else:
        # Descargar en video y convertir al formato deseado
        comando += ["--merge-output-format", formato, "-o", "%(title)s.%(ext)s"]

    comando.append(url)
    
    # Ejecutar y manejar errores
    try:
        resultado = subprocess.run(comando, check=True, capture_output=True, text=True)
        print(resultado.stdout)
        print("✅ Descarga completada exitosamente!")
    except subprocess.CalledProcessError as e:
        print("❌ Error al descargar el video:")
        print(e.stderr)

def descargar_twitter(url, formato):
    """
    Descarga un video de Twitter/X en el formato indicado.
    
    :param url: Enlace del video de Twitter/X
    :param formato: mp3, mp4 o gif
    """
    if formato not in ["mp3", "mp4", "gif"]:
        raise ValueError("Formato no válido. Usa: mp3, mp4 o gif")

    # Comando base
    comando = ["yt-dlp"]

    if formato == "mp3":
        # Extraer solo audio y convertir a mp3
        comando += ["--extract-audio", "--audio-format", "mp3", "-o", "%(title)s.%(ext)s"]
    elif formato == "gif":
        # Descargar video y convertir a gif
        comando += ["-o", "%(title)s.%(ext)s", "--recode-video", "gif"]
    else:
        # Descargar en mp4
        comando += ["-f", "best", "-o", "%(title)s.%(ext)s"]

    comando.append(url)

    # Ejecutar y manejar errores
    try:
        resultado = subprocess.run(comando, check=True, capture_output=True, text=True)
        print(resultado.stdout)
        print("✅ Descarga completada exitosamente!")
    except subprocess.CalledProcessError as e:
        print("❌ Error al descargar el video:")
        print(e.stderr)

if __name__ == "__main__":
    # Verificar e instalar dependencias primero
    verificar_e_instalar_dependencias()
    
    # Importar inquirer después de asegurar que está instalado
    import inquirer
    
    # Bucle principal para mantener el programa activo
    while True:
        try:
            # Selector de fuente
            preguntas_fuente = [
                inquirer.List('fuente',
                             message="\033[96m¿Qué quieres descargar?\033[0m",
                             choices=['YouTube', 'Twitter/X'],
                             ),
            ]
            respuesta_fuente = inquirer.prompt(preguntas_fuente)
            
            fuente = respuesta_fuente['fuente']

            # Selector de formato según la fuente
            if fuente == "YouTube":
                preguntas_formato = [
                    inquirer.List('formato',
                                 message="\033[96mElige el formato para YouTube\033[0m",
                                 choices=['mp3', 'mp4', 'mkv'],
                                 ),
                ]
            else:  # Twitter/X
                preguntas_formato = [
                    inquirer.List('formato',
                                 message="\033[96mElige el formato para Twitter/X\033[0m",
                                 choices=['mp3', 'mp4', 'gif'],
                                 ),
                ]
            
            respuesta_formato = inquirer.prompt(preguntas_formato)
            
            # Si el usuario cancela, volver al menú principal
            if respuesta_formato is None:
                continue
                
            formato = respuesta_formato['formato']

            # Solicitar URL
            url = input("Ingresa la URL del video: ").strip()
            
            # Si no se ingresa URL, volver al menú
            if not url:
                print("⚠️ No se ingresó ninguna URL. Volviendo al menú...\n")
                continue

            # Descargar según la fuente
            if fuente == "YouTube":
                descargar_youtube(url, formato)
            else:
                descargar_twitter(url, formato)
            
            print("\n" + "="*50 + "\n")  # Separador visual

        except KeyboardInterrupt:
            sys.exit(0)
        except Exception as e:
            print(f"❌ Ocurrió un error: {e}")
            print("\nVolviendo al menú principal...\n")
