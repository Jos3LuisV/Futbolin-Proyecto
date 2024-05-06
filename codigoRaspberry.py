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

#variables
turno = 1
goles_locales = 0
goles_visita = 0
    
def juego(turno, goles_locales, goles_visita):
    print(turno)
    if turno == 1:
        n = 5
        gol = True
        led.value = True
        pitido()
        contador = 2
        led.value = False
        
        posicion = random.randint(1,3)
        
        while n>0:
            if paleta1.value == True and posicion == 1:
                gol = False
            if paleta2.value == True and posicion == 1:
                gol = False
            if paleta3.value == True and posicion == 2:
                gol = False
            if paleta4.value == True and posicion == 2:
                gol = False
            if paleta5.value == True and posicion == 3:
                gol = False
            if paleta6.value == True and posicion == 3:
                gol = False
                
            print(paleta1.value,paleta2.value, paleta3.value, paleta4.value, paleta5.value, paleta6.value)
                
            n = n-0.1
            time.sleep(0.1)
        
        if posicion == 1:
            led17.value = True
            led16.value = True
            time.sleep(3)
            led17.value=False
            led16.value=False
        if posicion == 2:
            led15.value = True
            led14.value = True
            time.sleep(3)
            led15.value=False
            led14.value=False
        if posicion == 3:
            led13.value = True
            led12.value = True
            time.sleep(3)
            led13.value=False
            led12.value=False
            
        if gol == True:
            #gol(posicion, tiro)
            goles_locales = goles_locales + 1
            haaland()
            haaland()
            haaland()
            turno = 2
        else:
            turno = 2
  
    if turno == 2:
        print(turno)
        n = 5
        gol = True
        pitido()
        contador = 1
        led2.value = True
        time.sleep(3)
        led2.value = False
        
        posicion = random.randint(1,3)
        
        while n>0:
            if paleta1.value == True and posicion == 1:
                gol = False
                n=0
            if paleta2.value == True and posicion == 1:
                gol = False
                n=0
            if paleta3.value == True and posicion == 2:
                gol = False
                n=0
            if paleta4.value == True and posicion == 2:
                gol = False
                n=0
            if paleta5.value == True and posicion == 3:
                gol = False
                n=0
            if paleta6.value == True and posicion == 3:
                gol = False
                n=0
                
            print(paleta1.value,paleta2.value, paleta3.value, paleta4.value, paleta5.value, paleta6.value)
                
            n = n-0.1
            time.sleep(0.1)
            
        if posicion == 1:
            led17.value = True
            led16.value = True
            time.sleep(3)
            led17.value=False
            led16.value=False
        if posicion == 2:
            led15.value = True
            led14.value = True
            time.sleep(3)
            led15.value=False
            led14.value=False
        if posicion == 3:
            led13.value = True
            led12.value = True
            time.sleep(3)
            led13.value=False
            led12.value=False
         
        if gol == True:
            goles_visita = goles_visita + 1
            haaland()
            haaland()
            haaland()
            turno = 1
        else:
            turno = 1