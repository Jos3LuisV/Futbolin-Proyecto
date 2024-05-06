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
    
def fracaso():
    # Parámetros del sonido de fracaso
    frecuencia_fracaso = 1000  # Frecuencia del sonido de fracaso en Hz
    duracion_fracaso = 0.1  # Duración de cada tono del fracaso en segundos
    
    # Generar el sonido de fracaso
    # Repetir el patrón tres veces
    simpleio.tone(buzzer, frecuencia_fracaso, duration=duracion_fracaso)  # Reproducir tono de fracaso
        
    simpleio.tone(buzzer, frecuencia_fracaso, duration=duracion_fracaso+0.2)  # Reproducir tono de fracaso
        
    simpleio.tone(buzzer, frecuencia_fracaso, duration=duracion_fracaso+0.2)  # Reproducir tono de fracaso
    
def palo():
    # Parámetros del golpe a metal
    frecuencia_golpe = 3000  # Frecuencia del golpe en Hz
    duracion_golpe = 0.05  # Duración del golpe en segundos
    
    # Generar el sonido del golpe a metal
    simpleio.tone(buzzer, frecuencia_golpe, duration=duracion_golpe)
        
    
#variables
turno = 1
goles_locales = 0
goles_visita = 0
    
def juego(turno, goles_locales, goles_visita):
    print(turno)
    if turno == 1:
        n = 3
        gol = False
        led.value = True
        pitido()
        contador = 2
        led.value = False
        
        posicion = random.randint(1,3)
        
        while n>0:
            if paleta1.value == True:
                gol = True
                palo()
                led.value = True
                
                if posicion == 1:
                    gol = False
            if paleta2.value == True:
                gol = True
                palo()
                led.value = True
                
                if posicion == 1:
                    gol = False
            if paleta3.value == True:
                gol = True
                palo()
                led.value = True
                
                if posicion == 2:
                    gol = False
            if paleta4.value == True:
                gol = True
                palo()
                led.value = True
                
                if posicion == 2:
                    gol = False
            if paleta5.value == True:
                gol = True
                palo()
                led.value = True
                
                if posicion == 3:
                    gol = False
            if paleta6.value == True:
                gol = True
                palo()
                led.value = True
                
                if posicion == 3:
                    gol = False
                
            print(paleta1.value,paleta2.value, paleta3.value, paleta4.value, paleta5.value, paleta6.value)
            
            n = n-0.1
            time.sleep(0.1)
            led.value=False
        
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
            led17.value=True
            led16.value=True
            led15.value=True
            led14.value=True
            led13.value=True
            led12.value=True
            haaland()
            haaland()
            haaland()
            led17.value=False
            led16.value=False
            led15.value=False
            led14.value=False
            led13.value=False
            led12.value=False
            turno = 2
        else:
            fracaso()
            time.sleep(5)
            turno = 2
  
    if turno == 2:
        print(turno)
        n = 3
        gol = False
        contador = 1
        led2.value = True
        pitido()
        led2.value = False
        
        posicion = random.randint(1,3)
        
        while n>0:
            if paleta1.value == True:
                gol = True
                palo()
                led2.value = True
                
                if posicion == 1:
                    gol = False
            if paleta2.value == True:
                gol = True
                palo()
                led2.value = True
                
                if posicion == 1:
                    gol = False
            if paleta3.value == True:
                gole = True
                palo()
                led2.value = True
                
                if posicion == 2:
                    gol = False
            if paleta4.value == True:
                gol = True
                palo()
                led2.value = True
            
                if posicion == 2:
                    gol = False
            if paleta5.value == True:
                gol = True
                palo()
                led2.value = True
                
                if posicion == 3:
                    gol = False
            if paleta6.value == True:
                gol = True
                palo()
                led2.value = True
                if posicion == 3:
                    gol = False
                
            print(paleta1.value,paleta2.value, paleta3.value, paleta4.value, paleta5.value, paleta6.value)
                
            n = n-0.1
            time.sleep(0.1)
            led2.value=False
            
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
            led17.value=True
            led16.value=True
            led15.value=True
            led14.value=True
            led13.value=True
            led12.value=True
            haaland()
            haaland()
            haaland()
            led17.value=False
            led16.value=False
            led15.value=False
            led14.value=False
            led13.value=False
            led12.value=False
            turno = 1
        else:
            fracaso()
            time.sleep(5)
            turno = 1
            

pitido()
time.sleep(5)   
while True:
    juego(turno, goles_locales, goles_visita)
    
    
#Intento de ftp... no funciona a pesar de que teoricamente esta bien
#import adafruit_requests as requests   # Biblioteca para realizar solicitudes HTTP y FTP

# Establecer la URL del servidor FTP
#ftp_url = "ftp://user1:Emvjdm10*@192.168.0.162/Users/emora/OneDrive%20-%20Estudiantes%20ITCR/Escritorio/server"

# Crear un objeto de sesión FTP
#ftp = requests.Session(ftp_url)

# Subir un archivo al servidor FTP
#with open("servidor_txt.txt", "rb") as archivo:
 #   ftp.put(ftp_url, archivo, "archivo_en_servidor.txt")


# Cerrar la sesión FTP
#ftp.close()