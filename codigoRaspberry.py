#Librerías en general
import time
import board
import digitalio
import random
import simpleio
import analogio

#Librerías necesarias para conectar a internet
import os, ssl, socketpool, wifi

#Comprobar que se obtuvo con getenv() la "test_variable" del archivo settings.toml
print(os.getenv("test_variable"))

#Obtener la ssid y la contraseña
ssid = os.getenv("WIFI_SSID")
password = os.getenv("WIFI_PASSWORD")

#Conectar a internet
wifi.radio.connect(os.getenv("WIFI_SSID"), os.getenv("WIFI_PASSWORD"))
print("conectado exitosamente")

#Paletas

paleta1 = digitalio.DigitalInOut(board.GP12)
paleta1.direction = digitalio.Direction.INPUT

paleta2 = digitalio.DigitalInOut(board.GP11)
paleta2.direction = digitalio.Direction.INPUT

paleta3 = digitalio.DigitalInOut(board.GP10)
paleta3.direction = digitalio.Direction.INPUT

paleta4 = digitalio.DigitalInOut(board.GP9)
paleta4.direction = digitalio.Direction.INPUT

paleta5 = digitalio.DigitalInOut(board.GP8)
paleta5.direction = digitalio.Direction.INPUT

paleta6 = digitalio.DigitalInOut(board.GP7)
paleta6.direction = digitalio.Direction.INPUT

#LEDS de los jugadores

led = digitalio.DigitalInOut(board.GP27)
led.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.GP26)
led2.direction = digitalio.Direction.OUTPUT

#led de la porteria

led17 = digitalio.DigitalInOut(board.GP0)
led17.direction = digitalio.Direction.OUTPUT

led16 = digitalio.DigitalInOut(board.GP1)
led16.direction = digitalio.Direction.OUTPUT

led15 = digitalio.DigitalInOut(board.GP2)
led15.direction = digitalio.Direction.OUTPUT

led14 = digitalio.DigitalInOut(board.GP3)
led14.direction = digitalio.Direction.OUTPUT

led13 = digitalio.DigitalInOut(board.GP19)
led13.direction = digitalio.Direction.OUTPUT

led12 = digitalio.DigitalInOut(board.GP18)
led12.direction = digitalio.Direction.OUTPUT

# Potenciometro y su botón

pot = analogio.AnalogIn(board.GP28)
min_value = 0
max_value = 65535

boton = digitalio.DigitalInOut(board.GP5)
boton.direction = digitalio.Direction.INPUT

#lee el valor del potenciometro
def leer_potenciometro():
    return pot.value

# define un valor dependiendo de la lectura
def mapear_valor(valor):
    if valor <(max_value / 3) and boton.value == True:
        return 1
    if valor < ((max_value /3 )*2) and boton.value == True:
        return 2
    if valor > ((max_value /3 )*2) and boton.value == True:
        return 3

#buzzer

# Configurar el zumbador (buzzer)
buzzer = board.GP4

# Tocar la canción
def haaland():
    # Definir las frecuencias y duraciones para simular un aplauso
    aplauso_frecuencias = [400, 500, 600, 700, 800, 900, 1000]  # Frecuencias del aplauso
    aplauso_duraciones = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]  # Duraciones del aplauso
    
    # Reproducir el aplauso
    for freq, dur in zip(aplauso_frecuencias, aplauso_duraciones):
        simpleio.tone(buzzer, freq, duration=dur) #sonido
        time.sleep(0.05)  # Esperar un breve período entre cada sonido
        
        
def pitido():
    frecuencia_pitido = 3000  # Frecuencia del pitido en Hz
    duracion_pitido = 1    # Duración del pitido en segundos
    simpleio.tone(buzzer, frecuencia_pitido, duration=duracion_pitido) #sonido

