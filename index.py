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

    valor=messagebox.askquestion("Crear", "Deseas crear la tabla?")
  

    if valor=="yes":

        try:
      
            micursor.execute('''
                    CREATE TABLE PERSONAS (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NOMBRE VARCHAR(50),
                    PASSWORD VARCHAR(20),
                    APELLIDO VARCHAR(20),
                    DIRECCION VARCHAR(50),
                    COMENTARIOS VARCHAR(100))
                    ''')
         
            messagebox.showinfo("Crear", "Tabla en base de datos creada exitosamente")
            miConexion.commit()
            miConexion.close()
            

        except: 
            messagebox.showwarning("ATENCION", "LA BASE DE DATOS YA EXISTE")





def limpiarCampos():
    miID.set("")   
    Miname.set("") 
    passw.set("") 
    ape.set("") 
    dire.set("") 
    comment.set("")
    

def crear():
    global miConexion
    global micursor

    miConexion=sqlite3.connect("ListaDePersonas")
    micursor=miConexion.cursor()
    instrucciones="INSERT INTO PERSONAS VALUES('{0}', '{1}','{2}', '{3}','{4}', '{5}')".format(miID.get(), Miname.get(), passw.get(), ape.get(), dire.get(), comment.get())

    micursor.execute(instrucciones)

    miConexion.commit()


    miConexion.close()

    limpiarCampos()


def leer():
    miConexion=sqlite3.connect("ListaDePersonas")
    micursor=miConexion.cursor()
    lol="SELECT NOMBRE,PASSWORD, APELLIDO, DIRECCION, COMENTARIOS FROM PERSONAS WHERE ID={0}".format(miID.get())
   

    micursor.execute(lol)
    personitas=micursor.fetchall()

    for dato in personitas:  
            Miname.set(dato[0]) 
            passw.set(dato[1]) 
            ape.set(dato[2]) 
            dire.set(dato[3]) 
            comment.set(dato[4])


    miConexion.commit()
    miConexion.close()



def actualizar():
    miConexion=sqlite3.connect("ListaDePersonas")
    micursor=miConexion.cursor()

    actualizacion="UPDATE PERSONAS SET NOMBRE= '{0}', PASSWORD = '{1}', APELLIDO = '{2}', DIRECCION = '{3}', COMENTARIOS = '{4}' WHERE ID={5}".format(Miname.get(), passw.get(), ape.get(), dire.get(), comment.get(),miID.get())

    micursor.execute(actualizacion)
    
    miConexion.commit()
    miConexion.close()

def eliminar():
        miConexion=sqlite3.connect("ListaDePersonas")
        micursor=miConexion.cursor()


        borrao="DELETE FROM PERSONAS WHERE ID='{0}'".format(miID.get())

        micursor.execute(borrao)

        limpiarCampos()




        miConexion.commit()
        miConexion.close()




#______________________MENUS______________________________
borrar=Menu(barramenu, tearoff=0)
borrar.add_command(label="Borrar campos", command=limpiarCampos)

ayuda=Menu(barramenu, tearoff=0)
ayuda.add_command(label="Licencia")
ayuda.add_command(label="Acerca de...")

CRUD=Menu(barramenu, tearoff=0 )
CRUD.add_command(label="Crear", command=crear)
CRUD.add_command(label="Leer", command=leer)
CRUD.add_command(label="Actualizar", command=actualizar)
CRUD.add_command(label="Borrar", command=eliminar)


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
miID=StringVar()
Miname=StringVar()
passw=StringVar()
ape=StringVar()
dire=StringVar()
comment=StringVar()



aidi = Entry(miframe, textvariable=miID).grid(row=0, column=2, padx=5, pady=5)
nombre =Entry(miframe, justify = "center", textvariable=Miname).grid(row=1, column=2, padx=5, pady=5)
contra = Entry(miframe, show="*", justify="center", textvariable=passw).grid(row=2, column=2, padx=5, pady=5)
apellido = Entry(miframe, justify="center", textvariable=ape).grid(row=3, column=2, padx=5, pady=5)
direccion = Entry(miframe, textvariable=dire).grid(row=4, column=2, padx=5, pady=5)
comentario = Entry(miframe, textvariable=comment).grid(row=5, column=2, padx=5, pady=5)

'''
scrollvert=Scrollbar(miframe, command=comentario.yview).grid(row=5, column=3, sticky="nsew")
comentario.config(yscrollcommand=scrollvert.set)'''
#-----------------------botones 2 frame--------------------------------

crear=Button(frame, text="Crear", command=crear).grid(row=1, column=0, padx=7, pady=7)
leer=Button(frame, text="Leer", command=leer).grid(row=1, column=1, padx=7, pady=7)
actualizar=Button(frame, text="Actualizar", command= actualizar).grid(row=1, column=2, padx=7, pady=7)
eliminar=Button(frame, text="Eliminar", command=eliminar).grid(row=1, column=3, padx=7, pady=7)

#-------------------------------------------------------------------------





root.mainloop()