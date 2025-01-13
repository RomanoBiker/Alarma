import time
import random
import webbrowser
from datetime import datetime

# Ruta del archivo que contiene las URLs de YouTube
URL_FILE_PATH = 'youtube_links.txt'

def load_youtube_links(file_path):
    """Carga las URLs de un archivo de texto."""
    with open(file_path, 'r') as file:
        links = [line.strip() for line in file if line.strip()]
    return links

def set_alarm(alarm_time):
    """Establece la alarma y espera hasta que llegue el momento indicado."""
    print(f"Alarma configurada para las {alarm_time}")
    while True:
        current_time = datetime.now().strftime('%H:%M') # Formato HH:MM (24 horas)
        if current_time == alarm_time:
            print("¡Hora de despertar!")
            play_random_youtube_video()
            break
        time.sleep(1)

def play_random_youtube_video():
    """Reproduce un video aleatorio de YouTube."""
    links = load_youtube_links(URL_FILE_PATH)
    if links:
        chosen_link = random.choice(links)
        webbrowser.open(chosen_link)
    else:
        print("El archivo de enlaces está vacío o no se pudo cargar correctamente.")

if __name__ == "__main__":
    alarm_time = input("Ingresa la hora de la alarma (HH:MM): ")
    set_alarm(alarm_time)
