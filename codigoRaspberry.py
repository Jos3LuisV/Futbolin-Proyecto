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