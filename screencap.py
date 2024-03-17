import vlc
import time
import os

# Ruta al video que deseas reproducir en VLC
video_path = "D:/downloads/video.mp4"

# Configurar VLC
# Desactivar la pista de subtítulos
args = ['--no-xlib', '--no-spu']
vlc_instance = vlc.Instance('--no-xlib')
player = vlc_instance.media_player_new()
media = vlc_instance.media_new(video_path)

player.set_media(media)

# Silenciar el audio
player.audio_set_mute(True)

# Iniciar la reproducción del video
player.play()

# Intervalo de tiempo entre capturas de pantalla (en segundos)
intervalo = 1.5

# Directorio donde se guardarán las capturas de pantalla
directorio_salida = "C:/images"
if not os.path.exists(directorio_salida):
    os.makedirs(directorio_salida)

try:
    while True:
        # Verificar el estado de reproducción del video
        if player.get_state() == vlc.State.Ended:
            print("El video ha terminado de reproducirse.")
            break

        # Obtener el tiempo actual del video en segundos
        tiempo_actual = player.get_time() / 1000  # Convertir a segundos
        minutos = int(tiempo_actual // 60)
        segundos = int(tiempo_actual % 60)

        # Tomar una captura de pantalla usando VLC
        ruta_salida = os.path.join(directorio_salida, f"{minutos:02d}_{segundos:02d}.png")
        player.video_take_snapshot(0, ruta_salida, 0, 0)

        print(f"Captura de pantalla guardada: {ruta_salida}")

        # Esperar al siguiente intervalo de tiempo
        time.sleep(intervalo)

except KeyboardInterrupt:
    # Detener la reproducción y salir del bucle si se presiona Ctrl+C
    player.stop()
