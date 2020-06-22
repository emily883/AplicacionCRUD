from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()


miframe=Frame(root)
miframe.pack()
miframe.config(width=300, height=300)
frame=Frame(root)
frame.pack()
barramenu=Menu(root)
root.config(menu=barramenu, width=300, height=300)


#___________________funciones _____________________

def salir():
    valor=messagebox.askokcancel("Salir", "Deseas salir de la aplicacion?")
    
    if valor==True:
       root.destroy()



def conectar():
    global micursor
    global miConexion
    miConexion=sqlite3.connect("ListaDePersonas")
    micursor=miConexion.cursor()
    messagebox.showinfo("Conexion", "Base de datos creada y conectada correctamente")


def crear():
    global micursor
    global miConexion
    valor=messagebox.askquestion("Crear", "Deseas crear la base de datos?")
  

    if valor=="yes":

        micursor.execute("CREATE TABLE PERSONAS (ID INTEGER,NOMBRE VARCHAR(50),PASSWORD VARCHAR(20),APELLIDO VARHCAR(20),DIRECCION VARCHAR(50), COMENTARIOS VARCHAR(100))")
        miConexion.commit()
        miConexion.close()
        messagebox.showinfo("Crear", "Tabla en base de datos creada exitosamente")


#______________________MENUS______________________________
borrar=Menu(barramenu, tearoff=0)
borrar.add_command(label="Borrar campos")

ayuda=Menu(barramenu, tearoff=0)
ayuda.add_command(label="Licencia")
ayuda.add_command(label="Acerca de...")

CRUD=Menu(barramenu, tearoff=0 )
CRUD.add_command(label="Crear", command=crear)
CRUD.add_command(label="Leer")
CRUD.add_command(label="Actualizar")
CRUD.add_command(label="Borrar")


BBDD=Menu(barramenu, tearoff=0)
BBDD.add_command(label="Conectar", command=conectar)
BBDD.add_command(label="Salir", command=salir)

barramenu.add_cascade(label="BBDD", menu=BBDD)
barramenu.add_cascade(label="Borrar", menu=borrar)
barramenu.add_cascade(label="CRUD", menu=CRUD)
barramenu.add_cascade(label="Ayuda", menu=ayuda)
#________________________________________________________________

#------------------Labels----------------------

Label(miframe ,text="ID").grid(row=0, column=1, padx=5, pady=4)
Label(miframe, text="Nombre").grid(row=1, column=1, padx=5, pady=4)
Label(miframe, text="Password").grid(row=2, column=1, padx=5, pady=4)
Label(miframe, text="Apellido").grid(row=3, column=1, padx=5, pady=4)
Label(miframe, text="Direccion").grid(row=4, column=1, padx=5, pady=4)
Label(miframe, text="Comentario").grid(row=5, column=1, padx=5, pady=4)

#----------------------------------------------------------------
aidi = Entry(miframe).grid(row=0, column=2, padx=5, pady=5)
nombre =Entry(miframe, justify = "center").grid(row=1, column=2, padx=5, pady=5)
contra = Entry(miframe, show="*", justify="center").grid(row=2, column=2, padx=5, pady=5)
apellido = Entry(miframe, justify="center").grid(row=3, column=2, padx=5, pady=5)
direccion = Entry(miframe).grid(row=4, column=2, padx=5, pady=5)
comentario = Text(miframe, width=16, height=5).grid(row=5, column=2, padx=5, pady=5)
'''
scrollvert=Scrollbar(miframe, command=comentario.yview).grid(row=5, column=3, sticky="nsew")
comentario.config(yscrollcommand=scrollvert.set)'''
#-----------------------botones 2 frame--------------------------------

crear=Button(frame, text="Crear", command=crear).grid(row=1, column=0, padx=7, pady=7)
leer=Button(frame, text="Leer").grid(row=1, column=1, padx=7, pady=7)
actualizar=Button(frame, text="Actualizar").grid(row=1, column=2, padx=7, pady=7)
eliminar=Button(frame, text="Eliminar").grid(row=1, column=3, padx=7, pady=7)

#-------------------------------------------------------------------------





root.mainloop()