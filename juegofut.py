from tkinter import*
import pygame
import threading
import time
import random
from tkinter import messagebox
from PIL import Image, ImageTk

pygame.mixer.init() #Funcionamiento de música
pygame.mixer.music.load('song.mp3')
ventanaprincipal_app = None

def iniciar_musica():
    pygame.mixer.music.play()
def detener_musica():
    pygame.mixer.music.stop()
def ajustar_volumen(valor):
    pygame.mixer.music.set_volume(float(valor) / 100)

def ventana_configuracion():
      ventana_configuracion = Toplevel()
      ventana_configuracion.title("Configuración")
      ventana_configuracionfondo = PhotoImage(file= 'estadiofondoac.png' )
      ventana_configuracion.geometry("600x320")
      ventana_configuracion.resizable(False,False)
      ventana_configuracionfondo =Label(ventana_configuracion, image= ventana_configuracionfondo)
      ventana_configuracionfondo.place(x=0, y=0)
      
      
      def iniciar_musica():
         pygame.mixer.music.play()
      def detener_musica():
         pygame.mixer.music.stop()
      def ajustar_volumen(valor):
         pygame.mixer.music.set_volume(float(valor) / 100)
      iniciar_musica()
      
      boton_iniciar = Button(ventana_configuracion, text="Iniciar Música", command=iniciar_musica,  font=("BatmanForeverAlternate", 8),bg= "black", fg="white")
      boton_detener = Button(ventana_configuracion, text="Detener Música", command=detener_musica, font=("BatmanForeverAlternate", 8),bg= "black", fg="white")
      volumen_label = Label(ventana_configuracion, text="Parametros de Volumen", font=("BatmanForeverAlternate", 10),bg= "black", fg="white")
      volumen_control = Scale(ventana_configuracion, from_=0, to=100, orient=HORIZONTAL, command=ajustar_volumen,bg= "black",fg="white")
      boton_iniciar.place(x=200, y=50)
      boton_detener.place(x=200,y=100)
      volumen_label.place(x=200,y=150)
      volumen_control.place(x=200,y=200)
      
      iniciar_musica()
      pygame.mixer.music.play(-1)
      ventana_configuracion.mainloop()

def ventana_acerca():
    ventana_acerca = Toplevel()
    ventana_acerca.title ("Acerca de")
    fondoventana_acerca = PhotoImage(file='fondac.png')
    ventana_acerca.geometry("700x700")
    ventana_acerca.resizable(False,False)
    labelfondoventana_acerca =Label(ventana_acerca, image= fondoventana_acerca)
    labelfondoventana_acerca.place(x=0, y=0, relwidth=1, relheight=1)
    
    # Información del autor
    informacion_autor = """
    Nombres: José Luis Vargas   Nombre: Jafte José Díaz Morales
    Carnet : 2023058736              Carnet: 2023053249
    Asignatura: Fundamentos de Sistemas Computacionales
    Año: 2024
    Carrera (CE): Ingeniería en Computadores
    Profesor: Luis Alberto Chavarria Zamora 
    País de Producción: Costa Rica
    Versión del Programa: python version 3.11.5
    
    """
        # Etiqueta para mostrar la información del autor
    label_informacion = Label(ventana_acerca, text=informacion_autor, font=("Arial", 14), bg="black", fg="white", justify="left")
    label_informacion.place(x=40, y=20)
    
    label_fotodelprogramador = Label(ventana_acerca, text="FOTOGRAFÍAs DE LOS PROGRAMADORES", font=("SquareFont", 14), bg="black", fg="white", justify="left")
    label_fotodelprogramador.place(x=40, y=250)
    
    imagen_autor = Image.open('josefoto.jpeg')  
    imagen_autor = ImageTk.PhotoImage(imagen_autor)
    imagen_label = Label(ventana_acerca, image=imagen_autor, bg="black")
    imagen_label.place(x=40, y=300)
    
    imagen_autor2 = Image.open('jafetfoto.jpeg')  
    imagen_autor2 = ImageTk.PhotoImage(imagen_autor2)
    imagen_label = Label(ventana_acerca, image=imagen_autor2, bg="black")
    imagen_label.place(x=400, y=300)


    # Botón para cerrar la ventana
    boton_volver_inicio = Button(ventana_acerca, text="Cerrar", bg="black", fg="white", command=ventana_acerca.destroy)
    boton_volver_inicio.place(x=750,y=10)
        
        
        
    ventana_acerca.mainloop()

#Diccionario
imagenesjugadores = {
    1: 'alfredito.png',
    2: 'brayan.png',
    3: 'elbicho.pnf',
    4: 'halaand.png',
    5:  'messi.png',
    6: 'salvatierra.png',
    7: 'patrick.png',
    8: 'navas.png',
    9: 'portero2.png'
} 



        
   
def ventana2():
    ventana2 = Toplevel()
    ventana2.title("Seleccion de equipos")
    ventana2fondo = PhotoImage(file= 'fondodejuego.png')
    ventana2.geometry("900x384")
    ventana2.resizable(False, False)
    fondov2_label = Label(ventana2, image= ventana2fondo)
    fondov2_label.place(x=0, y=0,relwidth=1, relheight=1 )
    
    tituloprincipal_label = Label(ventana2, text="SELECIONE UN EQUIPO", font=("Impact", 30),bg= "black", fg="white")
    tituloprincipal_label.place(relx=0.01, rely=0.01)
    
     # Cargar las imágenes de los botones
    imagen1 = PhotoImage(file="sapri.png")
    imagen2 = PhotoImage(file="real.png")
    imagen3 = PhotoImage(file="equipochino.png")
    
    # Crear los botones con las imágenes
    boton1 = Button(ventana2, image=imagen1, command= abrir_ventana3)
    boton1.place(x=100, y=100)
    boton2 = Button(ventana2, image=imagen2, command= abrir_ventana5)
    boton2.place(x=320, y=100)
    boton3 = Button(ventana2, image=imagen3, command= abrir_ventana6)
    boton3.place(x=550, y=100)
    
    
    
    ventana2.mainloop()

class EstadisticasApp2:
    def __init__(self, root, archivo_datos):
        self.root = root
        self.root.title("Estadísticas de Equipos")
        self.root.geometry("400x200")

        self.archivo_datos = archivo_datos

        self.equipo1_stats = {"Anotaciones": 0, "Tiros fallados": 0, "Tiros perdidos por tiempo": 0}
        self.equipo2_stats = {"Anotaciones": 0, "Tiros fallados": 0, "Tiros perdidos por tiempo": 0}

        self.stats_frame1 =LabelFrame(root, text="Visitante")
        self.stats_frame1.grid(row=0, column=0, padx=10, pady=5)
        self.stats_frame2 =LabelFrame(root, text="Casa")
        self.stats_frame2.grid(row=0, column=1, padx=10, pady=5)

        self.actualizar_estadisticas()

        self.reiniciar_button1 =Button(self.stats_frame1, text="Reiniciar Estadísticas", command=self.reiniciar_estadisticas_visitante)
        self.reiniciar_button1.grid(row=3, column=0, padx=10, pady=5)

        self.reiniciar_button2 =Button(self.stats_frame2, text="Reiniciar Estadísticas", command=self.reiniciar_estadisticas_casa)
        self.reiniciar_button2.grid(row=3, column=0, padx=10, pady=5)

        self.timer_label =Label(root, text="Tiempo: 0")
        self.timer_label.grid(row=1, columnspan=2, pady=5)

        # Inicia el temporizador en un hilo aparte
        self.tiempo = 0
        self.tiempo_activo = True
        self.timer_thread = threading.Thread(target=self.contador_tiempo)
        self.timer_thread.start()

        # Inicia el hilo para leer el archivo de datos en tiempo real
        self.datos_thread = threading.Thread(target=self.leer_datos_archivo)
        self.datos_thread.start()

    def actualizar_estadisticas(self):
        self.stats_frame1.grid_forget()
        self.stats_frame1 =LabelFrame(self.root, text="Visitante")
        self.stats_frame1.grid(row=0, column=0, padx=10, pady=5)

        self.stats_frame2.grid_forget()
        self.stats_frame2 =LabelFrame(self.root, text="Casa")
        self.stats_frame2.grid(row=0, column=1, padx=10, pady=5)

        for i, (equipo, stats) in enumerate(zip(["Visitante", "Casa"], [self.equipo1_stats, self.equipo2_stats]), start=1):
            for j, (stat, valor) in enumerate(stats.items(), start=1):
                Label(self.stats_frame1 if equipo == "Visitante" else self.stats_frame2, text=f"{stat}: {valor}").grid(row=j, column=i, padx=5, pady=2)

    def reiniciar_estadisticas_visitante(self):
        self.equipo1_stats = {"Anotaciones": 0, "Tiros fallados": 0, "Tiros perdidos por tiempo": 0}
        self.actualizar_estadisticas()

    def reiniciar_estadisticas_casa(self):
        self.equipo2_stats = {"Anotaciones": 0, "Tiros fallados": 0, "Tiros perdidos por tiempo": 0}
        self.actualizar_estadisticas()

    def contador_tiempo(self):
        while self.tiempo_activo:
            self.tiempo += 1
            self.tiempo%= 6
            self.timer_label.config(text=f"Tiempo: {self.tiempo}")
            time.sleep(1)

    def leer_datos_archivo(self):
        while self.tiempo_activo:
            with open(self.archivo_datos, 'r') as archivo:
                for linea in archivo:
                    datos_equipo1, datos_equipo2 = linea.strip().split(',')
                    anotaciones1, tiros_fallados1, tiros_perdidos1 = map(int, datos_equipo1.split())
                    anotaciones2, tiros_fallados2, tiros_perdidos2 = map(int, datos_equipo2.split())

                    self.equipo1_stats["Anotaciones"] = anotaciones1
                    self.equipo1_stats["Tiros fallados"] = tiros_fallados1
                    self.equipo1_stats["Tiros perdidos por tiempo"] = tiros_perdidos1

                    self.equipo2_stats["Anotaciones"] = anotaciones2
                    self.equipo2_stats["Tiros fallados"] = tiros_fallados2
                    self.equipo2_stats["Tiros perdidos por tiempo"] = tiros_perdidos2

                    self.actualizar_estadisticas()
            time.sleep(5)  # Espera 5 segundos antes de volver a leer el archivo
def casa():
    
    casa = Tk()
    app = EstadisticasApp2(casa, "datos.txt")
    casa.mainloop()

class EstadisticasApp:
    def __init__(self, root, archivo_datos):
        self.root = root
        self.root.title("Estadísticas de Equipos")
        self.root.geometry("400x200")

        self.archivo_datos = archivo_datos

        self.equipo1_stats = {"Anotaciones": 0, "Tiros fallados": 0, "Tiros perdidos por tiempo": 0}
        self.equipo2_stats = {"Anotaciones": 0, "Tiros fallados": 0, "Tiros perdidos por tiempo": 0}

        self.stats_frame1 = LabelFrame(root, text="Equipo 1")
        self.stats_frame1.grid(row=0, column=0, padx=10, pady=5)
        self.stats_frame2 = LabelFrame(root, text="Equipo 2")
        self.stats_frame2.grid(row=0, column=1, padx=10, pady=5)

        self.actualizar_estadisticas()

        self.reiniciar_button1 = Button(self.stats_frame1, text="Reiniciar Estadísticas", command=self.reiniciar_estadisticas_equipo1)
        self.reiniciar_button1.grid(row=3, column=0, padx=10, pady=5)

        self.reiniciar_button2 = Button(self.stats_frame2, text="Reiniciar Estadísticas", command=self.reiniciar_estadisticas_equipo2)
        self.reiniciar_button2.grid(row=3, column=0, padx=10, pady=5)

        self.timer_label = Label(root, text="Tiempo: 0")
        self.timer_label.grid(row=1, columnspan=2, pady=5)

        # Inicia el temporizador en un hilo aparte
        self.tiempo = 0
        self.tiempo_activo = True
        self.timer_thread = threading.Thread(target=self.contador_tiempo)
        self.timer_thread.start()

        # Inicia el hilo para leer el archivo de datos en tiempo real
        self.datos_thread = threading.Thread(target=self.leer_datos_archivo)
        self.datos_thread.start()

    def actualizar_estadisticas(self):
        self.stats_frame1.grid_forget()
        self.stats_frame1 = LabelFrame(self.root, text="Equipo 1")
        self.stats_frame1.grid(row=0, column=0, padx=10, pady=5)

        self.stats_frame2.grid_forget()
        self.stats_frame2 = LabelFrame(self.root, text="Equipo 2")
        self.stats_frame2.grid(row=0, column=1, padx=10, pady=5)

        for i, (equipo, stats) in enumerate(zip(["Equipo 1", "Equipo 2"], [self.equipo1_stats, self.equipo2_stats]), start=1):
            for j, (stat, valor) in enumerate(stats.items(), start=1):
                Label(self.stats_frame1 if equipo == "Equipo 1" else self.stats_frame2, text=f"{stat}: {valor}").grid(row=j, column=i, padx=5, pady=2)

    def reiniciar_estadisticas_equipo1(self):
        self.equipo1_stats = {"Anotaciones": 0, "Tiros fallados": 0, "Tiros perdidos por tiempo": 0}
        self.actualizar_estadisticas()

    def reiniciar_estadisticas_equipo2(self):
        self.equipo2_stats = {"Anotaciones": 0, "Tiros fallados": 0, "Tiros perdidos por tiempo": 0}
        self.actualizar_estadisticas()

    def contador_tiempo(self):
        while self.tiempo_activo:
            self.tiempo += 1
            self.tiempo%= 6
            self.timer_label.config(text=f"Tiempo: {self.tiempo}")
            time.sleep(1)

    def leer_datos_archivo(self):
        while self.tiempo_activo:
            with open(self.archivo_datos, 'r') as archivo:
                for linea in archivo:
                    datos_equipo1, datos_equipo2 = linea.strip().split(',')
                    anotaciones1, tiros_fallados1, tiros_perdidos1 = map(int, datos_equipo1.split())
                    anotaciones2, tiros_fallados2, tiros_perdidos2 = map(int, datos_equipo2.split())

                    self.equipo1_stats["Anotaciones"] = anotaciones1
                    self.equipo1_stats["Tiros fallados"] = tiros_fallados1
                    self.equipo1_stats["Tiros perdidos por tiempo"] = tiros_perdidos1

                    self.equipo2_stats["Anotaciones"] = anotaciones2
                    self.equipo2_stats["Tiros fallados"] = tiros_fallados2
                    self.equipo2_stats["Tiros perdidos por tiempo"] = tiros_perdidos2

                    self.actualizar_estadisticas()
            time.sleep(5)  # Espera 5 segundos antes de volver a leer el archivo



def visitante():
    visitante = Tk()
    app = EstadisticasApp(visitante, "datos.txt")
    visitante.mainloop()

# Diccionario de imágenes de jugadores
imagenesjugadores = {
    1: 'alfredito.png',
    2: 'brayan.png',
    3: 'elbicho.pnf',
    4: 'halaand.png',
    5: 'messi.png',
    6: 'salvatierra.png',
    7: 'patrick.png',
    8: 'navas.png',
    9: 'portero2.png'
}
 

    

def ventana_juego():
   
    def girar_moneda():
        resultado = random.choice(["Cara", "Cruz"])
        if resultado == "Cara":
            imagen_cara()
        else:
            imagen_cruz()

# Función para mostrar la animación de la cara
    def imagen_cara():
        imagen1 = Image.open("cara1.png")
        imagen2 = Image.open("cara2.png")
        imagen3 = Image.open("cara3.png")

        imagenes = [imagen1, imagen2, imagen3]
        mostrar_animacion(imagenes)

# Función para mostrar la animación de la cruz
    def imagen_cruz():
        imagen1 = Image.open("C:\\Users\\equid\\Documents\\Fundamentos\\project\\moneda1.png")
        imagen2 = Image.open("C:\\Users\\equid\\Documents\\Fundamentos\\project\\moneda2.png")
        imagen3 = Image.open("C:\\Users\\equid\\Documents\\Fundamentos\\project\\moneda3.png")

        imagenes = [imagen1, imagen2, imagen3]
        mostrar_animacion(imagenes)

# Función para mostrar la animación basada en una lista de imágenes
    def mostrar_animacion(lista_imagenes):
        ventana = Toplevel()
        ventana.title("Animación")
        ventana.geometry("200x200")

        label = Label(ventana)
        label.pack()

    # Función para cambiar la imagen en el label
        def cambiar_imagen(index):
            imagen = ImageTk.PhotoImage(lista_imagenes[index])
            label.config(image=imagen)
            label.image = imagen
            ventana.after(1000, lambda: cambiar_imagen((index + 1) % len(lista_imagenes)))

    # Iniciar la animación
        cambiar_imagen(0)
        
    def resultado():
        opciones = ["Casa", "Visitante"]
        resultado_texto = random.choice(opciones)
        label_resultado.config(text=resultado_texto)
    
    ventana = Toplevel()
    ventana.title("juego")
    ventana.geometry("600x384")
    ventana.resizable(False, False) 
    boton_girar = Button(ventana, text="Girar", command= girar_moneda,)
    boton_girar.pack()
    label_resultado = Label(ventana, text="", font=("Arial", 18))
    label_resultado.pack()
    boton_resultado = Button(ventana, text="Resultado", command=resultado)
    boton_resultado.pack()
    label_2resultado = Label(ventana, text="Continue según el resultado", font=("Impact", 18))
    label_2resultado.place(x=150, y=200)
    boton_resultado = Button(ventana, text="Casa", command=casa)
    boton_resultado.place(x= 10, y= 300)
    boton_resultado = Button(ventana, text="Visitante", command=visitante)
    boton_resultado.place(x= 500, y=300)
    



def ventanaprincipal():#Funcion de la ventana principal
    
    ventana_principal = Tk()
    ventana_principal.title("Futbolito") #Nombre
    fondoprincipal = PhotoImage(file='portadainicial.png') #Fondo
    ventana_principal.geometry("756x422") #Tamaño
    ventana_principal.resizable(False, False)
    fondo_label = Label(ventana_principal, image=fondoprincipal)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
      
    tituloprincipal_label = Label(ventana_principal, text="FUTBOLITO", font=("Impact", 36),bg= "black", fg="white")
    tituloprincipal_label.place(relx=0.01, rely=0.01)

    #Botones de ventanas
    btn_ventana1 = Button(ventana_principal, text="JUGAR", font=("Impact",15),bg= "black", fg="white" ,command= ventana2, )
    btn_ventana1.place(x= 350, y= 250)

    btn_ventana2 = Button(ventana_principal, text="ACERCA DE",font=("Impact",15) ,bg= "black", fg="white",command= ventana_acerca)
    btn_ventana2.place(x= 350, y= 300)

    btn_ventana3 = Button(ventana_principal, text="CONFIGURACIÓN", font=("Impact",15) ,bg= "black", fg="white", command= ventana_configuracion )
    btn_ventana3.place(x= 350, y= 350)

    ventana_principal.mainloop()
ventanaprincipal()



