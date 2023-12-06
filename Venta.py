from tkinter import* 
from tkinter import ttk,messagebox
import ttkbootstrap as tb 
import sqlite3

class Ventana(tb.Window): 
    def __init__(self): 
        super().__init__()
        self.ventana_login()
    
    def ventana_login(self):
        
        self.frame_login= Frame(self)
        self.frame_login.pack()
        
        self.lblframe_login=LabelFrame(self.frame_login, text='Acceso')
        self.lblframe_login.pack(padx=10, pady=10)
        
        lbltitulo=ttk.Label(self.lblframe_login, text='inicio de sesion', font=('Arial',18))
        lbltitulo.pack(padx=10,pady=35)
        
        self.txt_usuario=ttk.Entry(self.lblframe_login, width=40,justify=CENTER)
        self.txt_usuario.pack(padx=10,pady=10)
        self.txt_clave=ttk.Entry(self.lblframe_login,width=40,justify=CENTER)
        self.txt_clave.pack(padx=10,pady=10)
        self.txt_clave.configure(show='z')
        btn_acceso=ttk.Button(self.lblframe_login, text='Log in',width=38,command=self.logueo)
        btn_acceso.pack(padx=10,pady=10)
    
    def ventana_menu(self):
        self.frame_left=Frame(self,width=200)
        self.frame_left.grid(row=0,column=0,sticky=NS)
        self.frame_center=Frame(self)
        self.frame_center.grid(row=0,column=1,sticky=NSEW)
        self.frame_right=Frame(self,width=400)
        self.frame_right.grid(row=0,column=2,sticky=NSEW)
        
        btn_productos=ttk.Button(self.frame_left,text='Productos',width=15)
        btn_productos.grid(row=0,column=0,padx=10,pady=10)
        btn_ventas=ttk.Button(self.frame_left,text='Ventas',width=15)
        btn_ventas.grid(row=1,column=0,padx=10,pady=10)
        btn_clientes=ttk.Button(self.frame_left,text='Clientes',width=15)
        btn_clientes.grid(row=2,column=0,padx=10,pady=10)
        btn_compras=ttk.Button(self.frame_left,text='Compras',width=15)
        btn_compras.grid(row=3,column=0,padx=10,pady=10)
        btn_usuarios=ttk.Button(self.frame_left,text='Usuarios',width=15,command=self.ventana_lista_usuarios)
        btn_usuarios.grid(row=4,column=0,padx=10,pady=10)
        btn_reportes=ttk.Button(self.frame_left,text='Reportes',width=15)
        btn_reportes.grid(row=5,column=0,padx=10,pady=10)
        btn_backup=ttk.Button(self.frame_left,text='Backup',width=15)
        btn_backup.grid(row=6,column=0,padx=10,pady=10)
        btn_restaurabd=ttk.Button(self.frame_left,text='Restaurar DB',width=15)
        btn_reportes.grid(row=7,column=0,padx=10,pady=10)
        
        lbl2=Label(self.frame_center,text='Aqui podremos las ventanas que creeemos')
        lbl2.grid(row=0,column=0,padx=10,pady=10)
        
        lbl3=Label(self.frame_right,text='Aqui podremos las busquedas para la venta')
        lbl3.grid(row=0,column=0,padx=10,pady=10)
    
    def logueo(self):
        
        try:
            miConexion=sqlite3.connect('Ventas.db')
            miCursor= miConexion.cursor()
            
            nombre_usuario=self.txt_usuario.get()
            clave_usuario=self.txt_clave.get()
            
            miCursor.execute("SELECT * FROM Usuarios WHERE Nombre=? AND Clave=?",(nombre_usuario,clave_usuario)) 
            datos_logueo=miCursor.fetchall()  
            if datos_logueo !="":
                for row in datos_logueo:
                    cod_usu=row[0]
                    nom_usu=row[1]
                    cla_usu=row[2]
                    rol_usu=row[3]
                if(nom_usu==self.txt_usuario.get() and cla_usu ==self.txt_clave.get()):
                     self.frame_login.pack_forget() #ocultamos la ventana de login
                     self.ventana_menu()
            
            miConexion.commit()
            miConexion.close()   
             
        except: 
              messagebox.showerror("Acceso","El usuario o clave son incorrectos") 
        
        #self.frame_login.pack_forget() #ocultamos la ventana de login #con esta linea de codigo habilitada deja pasar a cualquiera al sistema
        self.ventana_menu()#aqui abrimos nuestra ventana menu   
    
    def ventana_lista_usuarios(self):
        self.frame_lista_usuarios= Frame(self.frame_center)
        self.frame_lista_usuarios.grid(row=0, column=0,columnspan=2,sticky=NSEW)
        
        self.lblframe_botones_listusu=LabelFrame(self.frame_lista_usuarios)
        self.lblframe_botones_listusu.grid(row=0, column=0,padx=10,pady=10,sticky=NSEW)
        
        btn_nuevo_usuario= tb.Button(self.lblframe_botones_listusu, text='Nuevo', width=15,bootstyle="success",command=self.ventana_nuevo_usuario)
        btn_nuevo_usuario.grid(row=0,column=0, padx=5,pady=5)
        btn_modificar_usuario= tb.Button(self.lblframe_botones_listusu, text='Modificar', width=15,bootstyle="warning")
        btn_modificar_usuario.grid(row=0,column=1, padx=5,pady=5)
        btn_eliminar_usuario= tb.Button(self.lblframe_botones_listusu, text='Eliminar', width=15,bootstyle="danger")
        btn_eliminar_usuario.grid(row=0,column=2, padx=5,pady=5)   
        
        self.lblframe_busqueda_listusu=LabelFrame(self.frame_lista_usuarios)
        self.lblframe_busqueda_listusu.grid(row=1, column=0,padx=10,pady=10,sticky=NSEW)
        
        txt_busqueda_usuarios=ttk.Entry(self.lblframe_busqueda_listusu, width=95)
        txt_busqueda_usuarios.grid(row=0,column=0,padx=5,pady=5)
        
        #=====================Treeview===================
        
        self.lblframe_tree_listusu=LabelFrame(self.frame_lista_usuarios)
        self.lblframe_tree_listusu.grid(row=2, column=0,padx=10,pady=10,sticky=NSEW)
        
        columnas=("codigo", "nombre", "clave", "rol")
        
        self.tree_lista_usuarios= tb.Treeview(self.lblframe_tree_listusu, columns=columnas,
                                          height=17,show='headings',bootstyle='dark')
        self.tree_lista_usuarios.grid(row=0, column=0)
        
        self.tree_lista_usuarios.heading("codigo", text="Codigo", anchor=W)
        self.tree_lista_usuarios.heading("nombre", text="Nombre", anchor=W)
        self.tree_lista_usuarios.heading("clave", text="Clave", anchor=W)
        self.tree_lista_usuarios.heading("rol", text="Rol", anchor=W)
        self.tree_lista_usuarios['displaycolumns']=("codigo","nombre","rol")#para ocultar la clave solo apareceran codigo nombre y rol
        
        #Crear el scrolbar
        tree_scroll_listausu=tb.Scrollbar(self.frame_lista_usuarios, bootstyle='round-success')
        tree_scroll_listausu.grid(row=2, column=1)
        #Configurar el scrolbar
        tree_scroll_listausu.config(command=self.tree_lista_usuarios.yview)
        
        self.mostrar_usuarios()
              
    def mostrar_usuarios(self):
        try:
            miConexion=sqlite3.connect('Ventas.db')
            miCursor= miConexion.cursor()
            registros=self.tree_lista_usuarios.get_children()
            for elementos in registros:
                self.tree_lista_usuarios.delete(elementos)
            miCursor.execute("SELECT * FROM Usuarios") 
            datos=miCursor.fetchall()   
            for row in datos:
                self.tree_lista_usuarios.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3]))
            miConexion.commit()
            miConexion.close()   
             
        except: 
              messagebox.showerror("Lista de Usuario","Ocurrio un error al mostrar la lista de usuarios") 
        
    def ventana_nuevo_usuario(self):
        
        self.frame_nuevo_usuario=Toplevel(self)
        self.frame_nuevo_usuario.title('Nuevo Usuario')
        self.frame_nuevo_usuario.geometry('600x600')
        self.frame_nuevo_usuario.resizable(0,0)
        self.frame_nuevo_usuario.grab_set()
        
        lblframe_nuevo_usuario=LabelFrame(self.frame_nuevo_usuario)
        lblframe_nuevo_usuario.grid(row=0,column=0,sticky=NSEW,padx=10,pady=10)
        
        lbl_codigo_nuevo_usuario=Label(lblframe_nuevo_usuario, text='Codigo')
        lbl_codigo_nuevo_usuario.grid(row=0, column=0, padx=10,pady=10) 
        self.txt_codigo_nuevo_usuario=Entry(lblframe_nuevo_usuario, width=40)
        self.txt_codigo_nuevo_usuario.grid(row=0, column=1, padx=10,pady=10)
        
        lbl_nombre_nuevo_usuario=Label(lblframe_nuevo_usuario, text='Nombre')
        lbl_nombre_nuevo_usuario.grid(row=1, column=0, padx=10,pady=10) 
        self.txt_nombre_nuevo_usuario=Entry(lblframe_nuevo_usuario, width=40)
        self.txt_nombre_nuevo_usuario.grid(row=1, column=1, padx=10,pady=10)
        
        lbl_clave_nuevo_usuario=Label(lblframe_nuevo_usuario, text='Clave')
        lbl_clave_nuevo_usuario.grid(row=2, column=0, padx=10,pady=10) 
        self.txt_clave_nuevo_usuario=Entry(lblframe_nuevo_usuario, width=40)
        self.txt_clave_nuevo_usuario.grid(row=2, column=1, padx=10,pady=10)
        
        lbl_rol_nuevo_usuario=Label(lblframe_nuevo_usuario, text='Rol')
        lbl_rol_nuevo_usuario.grid(row=3, column=0, padx=10,pady=10) 
        self.txt_rol_nuevo_usuario=ttk.Combobox(lblframe_nuevo_usuario,values=('Administrador','Bodega','Vendedor'), width=38, state='readonly')
        self.txt_rol_nuevo_usuario.grid(row=3, column=1, padx=10,pady=10)
        self.txt_rol_nuevo_usuario.current(0)
        
        btn_guardar_nuevo_usuario=ttk.Button(lblframe_nuevo_usuario, text='Guardar',width=38,command=self.guardar_usuario)
        btn_guardar_nuevo_usuario.grid(row=4,column=1,padx=10,pady=10)   
        
        self.ultimo_usuario()
              
    def guardar_usuario(self): 
        if self.txt_codigo_nuevo_usuario.get()=="" or self.txt_nombre_nuevo_usuario.get()=="" or self.txt_clave_nuevo_usuario.get()=="":
            messagebox.showwarning('Guardando usuarios',"Algun campo no es valido por favor revise")  
            return    
        try:
            miConexion=sqlite3.connect('Ventas.db')
            miCursor= miConexion.cursor()
            datos_guardar_usuario=(self.txt_codigo_nuevo_usuario.get(),self.txt_nombre_nuevo_usuario.get(),
            self.txt_clave_nuevo_usuario.get(),self.txt_rol_nuevo_usuario.get()) #se guarda como una tupla
            miCursor.execute("INSERT INTO Usuarios VALUES(?,?,?,?)",datos_guardar_usuario) 
            messagebox.showinfo('Guardando Usuarios', "Usuario Guardado Correctamente")
            miConexion.commit()
            self.frame_nuevo_usuario.destroy() #cierra la ventana
            self.ventana_lista_usuarios()#cargamos la ventana para ver los cambios
            miConexion.close()   
             
        
        except sqlite3.Error as e:
            messagebox.showerror("Guardando Usuarios", f"Ocurrió un error al guardar usuarios: {str(e)}") 
           
    def ultimo_usuario(self):
         try:
            miConexion=sqlite3.connect('Ventas.db')
            miCursor= miConexion.cursor()
            miCursor.execute("SELECT MAX(Codigo) FROM Usuarios") 
            datos=miCursor.fetchone()
            for codusu in datos:
                if codusu==None:
                    self.ultusu=(int(1))
                    self.txt_codigo_nuevo_usuario.config(state=NORMAL)
                    self.txt_codigo_nuevo_usuario.insert(0, self.ultusu)
                    self.txt_codigo_nuevo_usuario.config(state='readonly')
                    break
                if codusu=="":
                    self.ultusu=(int(1))
                    self.txt_codigo_nuevo_usuario.config(state=NORMAL)
                    self.txt_codigo_nuevo_usuario.insert(0, self.ultusu)
                    self.txt_codigo_nuevo_usuario.config(state='readonly')
                    break                    
                else:           
                    self.ultusu=(int(codusu)+1)
                    self.txt_codigo_nuevo_usuario.config(state=NORMAL)
                    self.txt_codigo_nuevo_usuario.insert(0, self.ultusu)
                    self.txt_codigo_nuevo_usuario.config(state='readonly')
                    
            miConexion.commit()
            miConexion.close()        
         except: 
            messagebox.showerror("Acceso","El usuario o clave son incorrectos")  
               
        
         
        
        
        
        
def main(): 
    app=Ventana()
    app.title('Sistema de Ventas')
    app.state('zoomed')
    tb.Style('superhero')
    app.mainloop() 

if __name__=='__main__': 
    main()  