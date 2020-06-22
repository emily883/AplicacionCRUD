from tkinter import *
from tkinter import messagebox

root=Tk()


miframe=Frame(root)
miframe.pack()
miframe.config(width=300, height=300)
frame=Frame(root).pack()

#___________________funciones _____________________

def salir():
    valor=messagebox.askokcancel("Salir", "Deseas salir de la aplicacion?")
    
    if valor==True:
       root.destroy()

barramenu=Menu(root)
root.config(menu=barramenu, width=300, height=300)

#______________________MENUS______________________________
borrar=Menu(barramenu, tearoff=0)
borrar.add_command(label="Borrar campos")

ayuda=Menu(barramenu, tearoff=0)
ayuda.add_command(label="Licencia")
ayuda.add_command(label="Acerca de...")

CRUD=Menu(barramenu, tearoff=0 )
CRUD.add_command(label="Crear")
CRUD.add_command(label="Leer")
CRUD.add_command(label="Actualizar")
CRUD.add_command(label="Borrar")


BBDD=Menu(barramenu, tearoff=0)
BBDD.add_command(label="Conectar")
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
'''
comentario = Text(miframe, width=16, height=5).grid(row=5, column=2, padx=5, pady=5)
scrollvert=Scrollbar(miframe, command=comentario.yview).grid(row=5, column=3, sticky="nsew")
'''
#-----------------------botones 2 frame--------------------------------

crear=Button(frame, text="Crear").grid(row=1, column=1)




root.mainloop()