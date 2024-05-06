import pygame
import pygame.freetype
import sys

ANCHO, ALTO = 900, 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
otra_ventana = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Futbolito") #Ventana y defincición de dimensiones
FPS = 60
#Colores
BLANCO = (255 ,255, 255)
NEGRO = (0, 0, 0)
NARANJA_OSCURO = (255, 140, 0)

#Figuras e Imagenes
rect = pygame.Rect(100, 100, 50, 50)
fondo = pygame.image.load('estadionacionalfre.png')#Imagen de fondo
fond2 = pygame.image.load('fondodecancha.png') #fondo de cancha
boton_rect = pygame.Rect(390, 300, 150, 50) # Botón

#Texto
pygame.font.init()
fuente = pygame.font.Font("C:/Windows/Fonts/arial.ttf", 36) #fuente del botón 
texto = fuente.render("JUGAR", True, BLANCO)

#Muestra el fondo2
def fondo2(fond2):
    tamaño2 = pygame.transform.scale(fond2, (900, 600))
    otra_ventana.blit(tamaño2, (0,0))
#Muestra el fondo1
def fondo1(fondo):#Tamaño 
    tamaño = pygame.transform.scale(fondo, (900, 600))
    PANTALLA.blit(tamaño, (0,0))
    
#Dibuja todo en pantalla 
def dibujar():
    PANTALLA.fill(BLANCO)
    fondo1(fondo)
    pygame.draw.rect(PANTALLA, NARANJA_OSCURO, boton_rect)
    texto_rect = texto.get_rect()
    texto_rect.center = boton_rect.center
    PANTALLA.blit(texto, texto_rect)
    pygame.display.update()  
    
def dibujar2():
    otra_ventana.fill(BLANCO)
    fondo2(fond2)
    pygame.display.flip()
    pygame.display.update()
    
#Función principal de lógica
def main():
    reloj = pygame.time.Clock() # Velocidad del loop
    correrv = True #Loop de la ventana
    correrv2 = False #Loop de la segunda ventana
    while correrv:
        reloj.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                correrv = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:# Verificar si se hizo clic dentro del botón
                if boton_rect.collidepoint(event.pos):#  (abrir otra ventana)
                    dibujar2()
                    while True: 
                        for event2 in pygame.event.get():
                            if event2.type == pygame.QUIT:#Logica para cerrar la ventana hasta que se abre la otra
                                return
                            elif event2.type == pygame.MOUSEBUTTONDOWN:
                             return
            dibujar()

if __name__ == "__main__": #Hace que la ventana permanezca abierta
    main()
