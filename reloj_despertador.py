import time
import random
import webbrowser
from datetime import datetime

class Alarm():  # Reloj despertador que reproduce un video a la hora indicada
    def __init__(self, alarm_time):
        self.alarm_time = alarm_time

    def set_alarm(self, alarm_time):
        self.alarm_time = alarm_time
        """Establece la alarma y espera hasta que llegue el momento indicado."""
        print(f"Alarma configurada para las {alarm_time}")
        while True:
            current_time = datetime.now().strftime('%H:%M') # Formato HH:MM (24 horas)
            if current_time == alarm_time:
                print("¡Video Aleatorio!")
                VideoPlayer.play_random_youtube_video()
                break
            time.sleep(1)

class VideoPlayer():

    URL_FILE_PATH = 'youtube_links.txt'

    def __init__(self, file_path):
        self.file_path = file_path


    def load_youtube_links():
        """Carga las URLs de un archivo de texto."""
        with open(VideoPlayer.URL_FILE_PATH, 'r') as file:
            links = [line.strip() for line in file if line.strip()]
        return links

    @staticmethod
    def play_random_youtube_video():
        # Ruta del archivo que contiene las URLs de YouTube
        """Reproduce un video aleatorio de YouTube."""
        links = VideoPlayer.load_youtube_links()
        if links:
            chosen_link = random.choice(links)
            webbrowser.open(chosen_link)
        else:
            print("El archivo de enlaces está vacío o no se pudo cargar correctamente.")

if __name__ == "__main__":
    alarm_time = input("Ingresa la hora de la alarma (HH:MM): ")
    alarm_clock = Alarm(alarm_time)
    alarm_clock.set_alarm(alarm_time)