import yt_dlp
import yt_dlp.YoutubeDL
import time
import os


class youtubeToStream():
    ARCHIVO = 1
    LINK = 2
    MP3 = "mp3"
    MP4 = "mp4"
    
    def __init__(self):
        pass

    def procesar_archivo_mp3(self, archivo, directorio):
        with open(archivo, "r") as archivo:
            if archivo.readable():
                for linea in archivo:
                    self.descarga_mp3(linea.strip(), directorio)
                    time.sleep(1)
            else:
                print(f"el archivo no puede ser leido")
        archivo.close()
        
    def procesar_archivo_mp4(self, archivo, directorio):
        with open(archivo, "r") as archivo:
            if archivo.readable():
                for linea in archivo:
                    self.descarga_mp4(linea.strip(), directorio)
                    time.sleep(1)
            else:
                print(f"el archivo no puede ser leido")
        archivo.close()

    def descarga_mp4(self, link, directorio):
        directorio = os.path.join(directorio, self.MP4)
        if not os.path.exists(directorio):
            os.mkdir(directorio)
            time.sleep(3)
        ydl_opts ={
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            },
           # 'format':'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]',
            'format':'bv[height<=360]+ba[ext=m4a]/b[ext=mp4]',
            'outtmpl':os.path.join(directorio, '%(title)s.mp4'),
            'quiet': False,
            'noplaylist': True,
            'socket_timeout': 30,
            'retries': 5,
            'fragment_retries': 10,
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as video_mp4:
                video_mp4.download([link])
                print(f" video descargado correctamente")
        except Exception as e:
            print(f"Hubo un problema al descargar: {e}")


    def descarga_mp3(self,link,directorio):
        directorio = os.path.join(directorio, self.MP3)
        if not os.path.exists(directorio):
            os.mkdir(directorio)
            time.sleep(4)

        ydl_opts ={
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            },
            'extract_audio': True,
            'format': 'bestaudio',
            'outtmpl': os.path.join(directorio, '%(title)s.mp3'),
            'socket_timeout': 30,
            'retries': 5,
            'fragment_retries': 10,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts ) as sound_mp3:
                informacion = sound_mp3.extract_info(link, download = True)
                titulo = informacion['title']
                sound_mp3.download(link)
                print(f" audio ${titulo} descargado correctamente")
        except Exception as e:
            print(f"Hubo un problema al descargar: {e}")