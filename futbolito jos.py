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
def abrir_ventana6():
    global ventana6, ventana6fondo, sclBarra6, imagen_actual6, imagen_label6
    
    def actualizar_imagen6():
        global ventana6, ventana6fondo, sclBarra6, imagen_actual6, imagen_label6
        while True:
            valor_actual6 = sclBarra6.get()  # Obtener el valor actual del Scale
            if valor_actual6 < 100:
                imagen_actual6 = PhotoImage(file='halaand.png')
            elif valor_actual6 < 200:
                imagen_actual6 = PhotoImage(file='porcionzon.png')
            else:
                imagen_actual6 = PhotoImage(file='sonjugador.png')
            imagen_label6.configure(image=imagen_actual6)  # Actualizar la imagen en la ventana
            ventana6.update()  # Actualizar la ventana
            time.sleep(0.1)
            
    ventana6 = Toplevel()
    ventana6.title("Seleccion de jugadores")
    ventana6.geometry("900x400")
    ventana6.resizable(False,False)
    
    ventana6fondo = PhotoImage(file='fondodejuego.png')
    fondov6_label = Label(ventana6, image=ventana6fondo)
    fondov6_label.place(x=0, y=0)
    
    valor6 = IntVar()
    sclBarra6 = Scale(ventana6, label="Jugador", orient=HORIZONTAL, from_=0, to=300, tickinterval=100, length=200, variable=valor6)
    sclBarra6.place(x=10, y=10)
    
    
    imagen_actual6 = PhotoImage(file='halaand.png')
    imagen_label6 = Label(ventana6, image=imagen_actual6)
    imagen_label6.place(x=350, y=100)
    
    hilo_actualizacion6 = threading.Thread(target=actualizar_imagen6)
    hilo_actualizacion6.daemon = True
    hilo_actualizacion6.start()
    
    btneg = Button(ventana6, text= "SELECCIONAR PORTERO", font=("Impact", 10),bg= "black", fg="white", command= abrir_ventana4)
    btneg.place(x=700,y= 350)
   
    ventana6.mainloop()

def abrir_ventana5():
    global ventana5, ventana5fondo, sclBarra5, imagen_actual5, imagen_label5
    
    def actualizar_imagen5():
        global ventana5, ventana5fondo, sclBarra, imagen_actual5, imagen_label5
        while True:
            valor_actual5 = sclBarra5.get()  # Obtener el valor actual del Scale
            if valor_actual5 < 400:
                imagen_actual5 = PhotoImage(file='elbicho.png')
            elif valor_actual5 < 500:
                imagen_actual5 = PhotoImage(file='salvatierra.png')
            else:
                imagen_actual5 = PhotoImage(file='igsantos.png')
            imagen_label5.configure(image=imagen_actual5)  # Actualizar la imagen en la ventana
            ventana5.update()  # Actualizar la ventana
            time.sleep(0.1)
            
    ventana5 = Toplevel()
    ventana5.title("Seleccion de jugadores")
    ventana5.geometry("900x400")
    ventana5.resizable(False,False)
    
    ventana5fondo = PhotoImage(file='fondodejuego.png')
    fondov5_label = Label(ventana5, image=ventana5fondo)
    fondov5_label.place(x=0, y=0)
    
    valor5 = IntVar()
    sclBarra5 = Scale(ventana5, label="Jugador", orient=HORIZONTAL, from_=300, to=600, tickinterval=100, length=200, variable=valor5)
    sclBarra5.place(x=10, y=10)
    
    
    imagen_actual5 = PhotoImage(file='elbicho.png')
    imagen_label5 = Label(ventana5, image=imagen_actual5)
    imagen_label5.place(x=350, y=100)
    
    hilo_actualizacion5 = threading.Thread(target=actualizar_imagen5)
    hilo_actualizacion5.daemon = True
    hilo_actualizacion5.start()
    
    btneg = Button(ventana5, text= "SELECCIONAR PORTERO", font=("Impact", 10),bg= "black", fg="white", command= abrir_ventana4)
    btneg.place(x=700,y= 350)
    ventana5.mainloop()


def abrir_ventana4():
    global ventana4, ventana4fondo, imagen2_label, sclBarra2, imagen_actual2
    
    def actualizar_imagen2():
        global imagen2_label, sclBarra2, imagen_actual2
        while True:
            valor_actual2 = sclBarra2.get()
            if valor_actual2 < 100:
                imagen_actual2 = PhotoImage(file='navas.png')
            elif valor_actual2 <200:
                imagen_actual2 = PhotoImage(file= 'portero2.png')
            else:
                imagen_actual2 = PhotoImage(file= 'patrick.png')
            imagen2_label.config(image= imagen_actual2)
            ventana4.update()
            time.sleep(0.1)
    
    ventana4 = Toplevel()
    ventana4.title("Juego")
    ventana4.geometry("900x400")
    ventana4.resizable(False,False)
    
    ventana4fondo = PhotoImage(file='fondodejuego.png')
    fondov4_label = Label(ventana4, image=ventana4fondo)
    fondov4_label.place(x=0, y=0)
    
    valor2 = IntVar()
    sclBarra2 = Scale(ventana4, label="Portero", orient= HORIZONTAL, from_=0, to= 300,tickinterval=100 , length=200, variable= valor2 )
    sclBarra2.place(x= 10, y=10)
    
    imagen_actual2= PhotoImage(file='navas.png')
    imagen2_label = Label(ventana4, image= imagen_actual2)
    imagen2_label.place(x=400, y=100)
    
    hilo_actualizacion2 = threading.Thread(target=actualizar_imagen2)
    hilo_actualizacion2.daemon = True
    hilo_actualizacion2.start()
    
    btn = Button(ventana4, text= "JUGAR" ,font=("Impact", 10),bg= "black", fg="white", command= ventana_juego)
    btn.place(x=700,y= 350)
    ventana4.mainloop()

   


def abrir_ventana3():
    global ventana3, ventana3fondo, sclBarra, imagen_actual, imagen_label
    
    def actualizar_imagen():
        global ventana3, ventana3fondo, sclBarra, imagen_actual, imagen_label
        while True:
            valor_actual = sclBarra.get()  # Obtener el valor actual del Scale
            if valor_actual < 100:
                imagen_actual = PhotoImage(file='brayan.png')
            elif valor_actual < 200:
                imagen_actual = PhotoImage(file='messi.png')
            else:
                imagen_actual = PhotoImage(file='alfredito.png')
            imagen_label.configure(image=imagen_actual)  # Actualizar la imagen en la ventana
            ventana3.update()  # Actualizar la ventana
            time.sleep(0.1)
            
    ventana3 = Toplevel()
    ventana3.title("Seleccion de jugadores")
    ventana3.geometry("900x400")
    ventana3.resizable(False,False)
    
    ventana3fondo = PhotoImage(file='fondodejuego.png')
    fondov3_label = Label(ventana3, image=ventana3fondo)
    fondov3_label.place(x=0, y=0)
    
    valor = IntVar()
    sclBarra = Scale(ventana3, label="Jugador", orient=HORIZONTAL, from_=0, to=300, tickinterval=100, length=200, variable=valor)
    sclBarra.place(x=10, y=10)
    
    
    imagen_actual = PhotoImage(file='brayan.png')
    imagen_label = Label(ventana3, image=imagen_actual)
    imagen_label.place(x=350, y=100)
    
    hilo_actualizacion = threading.Thread(target=actualizar_imagen)
    hilo_actualizacion.daemon = True
    hilo_actualizacion.start()
    
    btneg = Button(ventana3, text= "SELECCIONAR PORTERO", font=("Impact", 10),bg= "black", fg="white", command= abrir_ventana4)
    btneg.place(x=700,y= 350)
    
    ventana3.mainloop()
    
