El sistema permite procesar cualquier URL de YouTube proporcionada por el usuario, transformando el contenido automáticamente a formatos descargables MP3 (audio) o MP4 (video).


### 🚀 Características
- **Soporte Universal:** Acepta cualquier enlace de YouTube.
- **Conversión Dual:** Transforma el video en tiempo real a:
  - 🎵 **MP3** (Alta calidad de audio).
  - 🎥 **MP4** (Video optimizado).


 Flujo de Conversión

El proceso se divide en tres etapas clave:

Entrada (Input): El usuario asigna la URL del video de YouTube en la interfaz.
Procesamiento: El sistema valida el enlace y procesa el flujo de datos.
Salida (Output): La aplicación transforma el contenido y entrega un archivo final en formato MP3 o MP4.



⚙️ Configuración del Entorno
Para que la transformación de YouTube a MP3/MP4 funcione correctamente, el sistema requiere de herramientas de procesamiento de señales y manejo de flujos de video.

📋 Requisitos Previos
Antes de ejecutar la aplicación, asegúrate de tener instalado:

FFmpeg: Herramienta esencial para la transcodificación de audio y video. Sin ella, el sistema no podrá unir las pistas de audio y video o convertir a MP3.

PowerShell
winget install ffmpeg

Mac
brew install ffmpeg

Ubuntu 
sudo apt update
sudo apt install ffmpeg


yt-dlp : El motor encargado de extraer la información de la URL de YouTube.

Entorno de ejecución: Python 3.13).