from tkinter import* 
from tkinter import ttk,messagebox
import ttkbootstrap as tb 
import sqlite3

class Ventana(tb.Window): 
    def __init__(self): 
        super().__init__()
        self.ventana_login()
    
    def ventana_login(self): # ventana por donde uno se logea al sistma 
        
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
    
    def ventana_menu(self): #ventana menu donde se muestran las opciones 
        self.frame_left=Frame(self,width=200)
        self.frame_left.grid(row=0,column=0,sticky=NS)
        self.frame_center=Frame(self)
        self.frame_center.grid(row=0,column=1,sticky=NSEW)
        self.frame_right=Frame(self,width=400)
        self.frame_right.grid(row=0,column=2,sticky=NSEW)
        
        btn_productos=ttk.Button(self.frame_left,text='Productos',width=15, command=self.ventana_lista_productos)
        btn_productos.grid(row=0,column=0,padx=10,pady=10)
        btn_ventas=ttk.Button(self.frame_left,text='Ventas',width=15, command=self.ventana_lista_ventas)
        btn_ventas.grid(row=1,column=0,padx=10,pady=10)
        btn_clientes=ttk.Button(self.frame_left,text='Clientes',width=15)
        btn_clientes.grid(row=2,column=0,padx=10,pady=10)
        btn_compras=ttk.Button(self.frame_left,text='Compras',width=15,command= self.ventana_lista_compras)
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
    
    def logueo(self):#funcion que permite logearse con usuario y clave 
        
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
   
    #==============================USUARIOS=================================#
    def ventana_lista_usuarios(self): #ventana madre sobre la cual edificar el resto de los botones 
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
        
        self.txt_busqueda_usuarios=ttk.Entry(self.lblframe_busqueda_listusu, width=95)
        self.txt_busqueda_usuarios.grid(row=0,column=0,padx=5,pady=5)
        self.txt_busqueda_usuarios.bind('<Key>', self.buscar_usuarios)
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
              
    def mostrar_usuarios(self): # con esta funcion se llama a la BD y se muestra los datos contenidos en ella  es utilizada al final de la funcion que implenta cada boton
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
    
    def buscar_usuarios(self,event):
        try:
            miConexion=sqlite3.connect('Ventas.db')
            miCursor= miConexion.cursor()
            registros=self.tree_lista_usuarios.get_children()
            for elementos in registros:
                self.tree_lista_usuarios.delete(elementos)
            miCursor.execute("SELECT * FROM Usuarios WHERE Nombre LIKE ?",(self.txt_busqueda_usuarios.get()
                                                                           +'%',)) 
            datos=miCursor.fetchall()   
            for row in datos:
                self.tree_lista_usuarios.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3]))
            miConexion.commit()
            miConexion.close()   
             
        except: 
              messagebox.showerror("Busqueda de usuario","Ocurrio un error al buscar en la lista de usuarios") 
    
    def ventana_modificar_usuario(self):
        
        self.frame_modificar_usuario=Toplevel(self)
        self.frame_modificar_usuario.title('Nuevo Usuario')
        self.frame_modificar_usuario.geometry('600x600')
        self.frame_modificar_usuario.resizable(0,0)
        self.frame_modificar_usuario.grab_set() #para que no se permita hacer nada mientras la ventana esta abierta
        
        lblframe_modificar_usuario=LabelFrame(self.frame_nuevo_usuario)
        lblframe_modificar_usuario.grid(row=0,column=0,sticky=NSEW,padx=10,pady=10)
        
        lbl_codigo_modificar_usuario=Label(lblframe_modificar_usuario, text='Codigo')
        lbl_codigo_modificar_usuario.grid(row=0, column=0, padx=10,pady=10) 
        self.txt_codigo_modificar_usuario=Entry(lblframe_modificar_usuario, width=40)
        self.txt_codigo_modificar_usuario.grid(row=0, column=1, padx=10,pady=10)
        
        lbl_nombre_modificar_usuario=Label(lblframe_modificar_usuario, text='Nombre')
        lbl_nombre_modificar_usuario.grid(row=1, column=0, padx=10,pady=10) 
        self.txt_nombre_modificar_usuario=Entry(lblframe_modificar_usuario, width=40)
        self.txt_nombre_modificar_usuario.grid(row=1, column=1, padx=10,pady=10)
        
        lbl_clave_modificar_usuario=Label(lblframe_modificar_usuario, text='Clave')
        lbl_clave_modificar_usuario.grid(row=2, column=0, padx=10,pady=10) 
        self.txt_clave_modificar_usuario=Entry(lblframe_modificar_usuario, width=40)
        self.txt_clave_modificar_usuario.grid(row=2, column=1, padx=10,pady=10)
        
        lbl_rol_modificar_usuario=Label(lblframe_modificar_usuario, text='Rol')
        lbl_rol_modificar_usuario.grid(row=3, column=0, padx=10,pady=10) 
        self.txt_rol_modificar_usuario=ttk.Combobox(lblframe_modificar_usuario,values=('Administrador','Bodega','Vendedor'), width=38, state='readonly')
        self.txt_rol_modificar_usuario.grid(row=3, column=1, padx=10,pady=10)
        
        
        btn_guardar_modificar_usuario=ttk.Button(lblframe_modificar_usuario, text='Modificar',width=38,command=self.modificar_usuario)
        btn_guardar_modificar_usuario.grid(row=4,column=1,padx=10,pady=10)   
        
        #self.ultimo_usuario()
    
    #====================================PRODUCTOS==================================#         
    def ventana_lista_productos(self): #ventana madre sobre la cual edificar el resto de los botones 
        self.frame_lista_productos= Frame(self.frame_center)
        self.frame_lista_productos.grid(row=0, column=0,columnspan=2,sticky=NSEW)
        
        self.lblframe_botones_listpro=LabelFrame(self.frame_lista_productos)
        self.lblframe_botones_listpro.grid(row=0, column=0,padx=10,pady=10,sticky=NSEW)
        
        btn_nuevo_producto= tb.Button(self.lblframe_botones_listpro, text='Nuevo', width=15,bootstyle="success",command=self.ventana_nuevo_producto)
        btn_nuevo_producto.grid(row=0,column=0, padx=5,pady=5)
        
        btn_modificar_producto= tb.Button(self.lblframe_botones_listpro, text='Modificar', width=15,bootstyle="warning",command=self.ventana_modificar_usuario)
        btn_modificar_producto.grid(row=0,column=1, padx=5,pady=5)
        
        btn_eliminar_producto= tb.Button(self.lblframe_botones_listpro, text='Eliminar', width=15,bootstyle="danger")
        btn_eliminar_producto.grid(row=0,column=2, padx=5,pady=5)   
        
        self.lblframe_busqueda_listpro=LabelFrame(self.frame_lista_productos)
        self.lblframe_busqueda_listpro.grid(row=1, column=0,padx=10,pady=10,sticky=NSEW)
        
        self.txt_busqueda_producto=ttk.Entry(self.lblframe_busqueda_listpro, width=95)
        self.txt_busqueda_producto.grid(row=0,column=0,padx=5,pady=5)
        self.txt_busqueda_producto.bind('<Key>', self.buscar_producto)
        
        #=====================Treeview===================
        
        self.lblframe_tree_listpro=LabelFrame(self.frame_lista_productos)
        self.lblframe_tree_listpro.grid(row=2, column=0,padx=10,pady=10,sticky=NSEW)
        
        columnas=("codigo", "descripcion", "precio_pesos", "precio_dolar")
        
        self.tree_lista_productos= tb.Treeview(self.lblframe_tree_listpro, columns=columnas,
                                          height=17,show='headings',bootstyle='dark')
        self.tree_lista_productos.grid(row=0, column=0)
        
        self.tree_lista_productos.heading("codigo", text="Codigo", anchor=W)
        self.tree_lista_productos.heading("descripcion", text="Descripcion", anchor=W)
        self.tree_lista_productos.heading("precio_pesos", text="Precio Pesos", anchor=W)
        self.tree_lista_productos.heading("precio_dolar", text="Precio dolar", anchor=W)
        #self.tree_lista_productos['displaycolumns']=("codigo","descripcion","precio pesos","precio dolar")#para ocultar la clave solo apareceran codigo nombre y rol# sirve para ocultar toda la ventana 
        
        #Crear el scrolbar
        tree_scroll_listpro=tb.Scrollbar(self.frame_lista_productos, bootstyle='round-success')
        tree_scroll_listpro.grid(row=2, column=1)
        #Configurar el scrolbar
        tree_scroll_listpro.config(command=self.tree_lista_productos.yview)
        
        self.mostrar_productos()
              
    def mostrar_productos(self): # con esta funcion se llama a la BD y se muestra los datos contenidos en ella  es utilizada al final de la funcion que implenta cada boton
        try:
            miConexion=sqlite3.connect('Ventas.db')
            miCursor= miConexion.cursor()
            registros=self.tree_lista_productos.get_children()
            for elementos in registros:
                self.tree_lista_productos.delete(elementos)
            miCursor.execute("SELECT * FROM Productos") 
            datos=miCursor.fetchall()   
            for row in datos:
                self.tree_lista_productos.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3]))
            miConexion.commit()
            miConexion.close()   
             
        except: 
              messagebox.showerror("Lista de Producto","Ocurrio un error al mostrar la lista de productos")
    
    def ventana_nuevo_producto(self):
        
        self.frame_nuevo_producto=Toplevel(self)
        self.frame_nuevo_producto.title('Nuevo Producto')
        self.frame_nuevo_producto.geometry('600x600')
        self.frame_nuevo_producto.resizable(0,0)
        self.frame_nuevo_producto.grab_set()
        
        lblframe_nuevo_producto=LabelFrame(self.frame_nuevo_producto)
        lblframe_nuevo_producto.grid(row=0,column=0,sticky=NSEW,padx=10,pady=10)
        
        lbl_codigo_nuevo_producto=Label(lblframe_nuevo_producto, text='Codigo')
        lbl_codigo_nuevo_producto.grid(row=0, column=0, padx=10,pady=10) 
        self.txt_codigo_nuevo_producto=Entry(lblframe_nuevo_producto, width=40)
        self.txt_codigo_nuevo_producto.grid(row=0, column=1, padx=10,pady=10)
        
        lbl_descripcion_nuevo_producto=Label(lblframe_nuevo_producto, text='Descripcion')
        lbl_descripcion_nuevo_producto.grid(row=1, column=0, padx=10,pady=10) 
        self.txt_descripcion_nuevo_producto=Entry(lblframe_nuevo_producto, width=40)
        self.txt_descripcion_nuevo_producto.grid(row=1, column=1, padx=10,pady=10)
        
        lbl_precio_pesos_nuevo_producto=Label(lblframe_nuevo_producto, text='Precio pesos')
        lbl_precio_pesos_nuevo_producto.grid(row=2, column=0, padx=10,pady=10) 
        self.txt_precio_pesos_nuevo_producto=Entry(lblframe_nuevo_producto, width=40)
        self.txt_precio_pesos_nuevo_producto.grid(row=2, column=1, padx=10,pady=10)
        
        lbl_precio_dolar_nuevo_producto=Label(lblframe_nuevo_producto, text='Precio dolar')
        lbl_precio_dolar_nuevo_producto.grid(row=3, column=0, padx=10,pady=10) 
        self.txt_precio_dolar_nuevo_producto=Entry(lblframe_nuevo_producto, width=40)
        self.txt_precio_dolar_nuevo_producto.grid(row=3, column=1, padx=10,pady=10)
        
        
        btn_guardar_nuevo_producto=ttk.Button(lblframe_nuevo_producto, text='Guardar',width=38,command=self.guardar_producto)
        btn_guardar_nuevo_producto.grid(row=4,column=1,padx=10,pady=10)   
        
        #LLAMADA A LA FUNCION ULTIMO_PRODUCTO HAY QUE IMPLEMENTAR
        
    def guardar_producto(self): 
        if self.txt_codigo_nuevo_producto.get()=="" or self.txt_descripcion_nuevo_producto.get()=="" or self.txt_precio_pesos_nuevo_producto.get()=="" or self.txt_precio_dolar_nuevo_producto.get()=="":
            
            messagebox.showwarning('Guardando usuarios',"Algun campo no es valido por favor revise")  
            return    
        try:
            miConexion=sqlite3.connect('Ventas.db')
            miCursor= miConexion.cursor()
            datos_guardar_producto=(self.txt_codigo_nuevo_producto.get(),self.txt_descripcion_nuevo_producto.get(),
            self.txt_precio_pesos_nuevo_producto.get(),self.txt_precio_dolar_nuevo_producto.get()) #se guarda como una tupla
            miCursor.execute("INSERT INTO Productos VALUES(?,?,?,?)",datos_guardar_producto) 
            messagebox.showinfo('Guardando Producto', "Producto Guardado Correctamente")
            miConexion.commit()
            self.frame_nuevo_producto.destroy() #cierra la ventana
            self.ventana_lista_productos()#cargamos la ventana para ver los cambios
            miConexion.close()   
             
        
        except sqlite3.Error as e:
            messagebox.showerror("Guardando Producto", f"Ocurrió un error al guardar usuarios: {str(e)}") 
                              
    def buscar_producto(self,event): #FUNCION PARA BUSCAR PRODUCTOS
        try:
            miConexion=sqlite3.connect('Ventas.db')
            miCursor= miConexion.cursor()
            registros=self.tree_lista_productos.get_children()
            for elementos in registros:
                self.tree_lista_productos.delete(elementos)
            miCursor.execute("SELECT * FROM Productos WHERE Descripcion LIKE ?",(self.txt_busqueda_producto.get()
                                                                           +'%',)) 
            datos=miCursor.fetchall()   
            for row in datos:
                self.tree_lista_productos.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3]))
            miConexion.commit()
            miConexion.close()   
             
        except: 
              messagebox.showerror("Busqueda de producto","Ocurrio un error al buscar en la lista de productos")
    
    def ventana_modificar_producto(self):
        
        self.frame_modificar_producto=Toplevel(master=self)
        self.frame_modificar_producto.title('Modificar Producto')
        #self.frame_modificar_producto.geometry('400x450')
        #self.frame_modificar_producto.resizable(0,0)
        self.frame_modificar_producto.grab_set()
        
        lblframe_modificar_producto=tb.LabelFrame(master=self.frame_modificar_producto,text='Modificar Producto')
        lblframe_modificar_producto.pack(padx=15,pady=15)
        
        lbl_codigo_modificar_producto=Label(lblframe_modificar_producto, text='Codigo')
        lbl_codigo_modificar_producto.grid(row=0, column=0, padx=10,pady=10) 
        self.txt_codigo_modificar_producto=Entry(lblframe_modificar_producto, width=40)
        self.txt_codigo_modificar_producto.grid(row=0, column=1, padx=10,pady=10)
        
        lbl_descripcion_modificar_producto=Label(lblframe_modificar_producto, text='Descripcion')
        lbl_descripcion_modificar_producto.grid(row=1, column=0, padx=10,pady=10) 
        self.txt_descripcion_modificar_producto=Entry(lblframe_modificar_producto, width=40)
        self.txt_descripcion_modificar_producto.grid(row=1, column=1, padx=10,pady=10)
        
        lbl_precio_pesos_modificar_producto=Label(lblframe_modificar_producto, text='Precio pesos')
        lbl_precio_pesos_modificar_producto.grid(row=2, column=0, padx=10,pady=10) 
        self.txt_precio_pesos_modificar_producto=Entry(lblframe_modificar_producto, width=40)
        self.txt_precio_pesos_modificar_producto.grid(row=2, column=1, padx=10,pady=10)
        
        lbl_precio_dolar_modificar_producto=Label(lblframe_modificar_producto, text='Precio dolar')
        lbl_precio_dolar_modificar_producto.grid(row=3, column=0, padx=10,pady=10) 
        self.txt_precio_dolar_modificar_producto=Entry(lblframe_modificar_producto, width=40)
        self.txt_precio_dolar_modificar_producto.grid(row=3, column=1, padx=10,pady=10)
        
        
        btn_modificar_producto=tb.Button(master=lblframe_modificar_producto, text='Modificar', width=38, bootstyle='success')
        btn_modificar_producto.grid(row=7,column=1,padx=10,pady=10)
        self.ent_nombre_modificar_producto.focus()   
        
              
    #=================================VENTAS=================================#
    def ventana_lista_ventas(self): #ventana madre sobre la cual edificar el resto de los botones 
        self.frame_lista_ventas= Frame(self.frame_center)
        self.frame_lista_ventas.grid(row=0, column=0,columnspan=2,sticky=NSEW)
        
        self.lblframe_botones_listven=LabelFrame(self.frame_lista_ventas)
        self.lblframe_botones_listven.grid(row=0, column=0,padx=10,pady=10,sticky=NSEW)
        
        btn_nuevo_venta= tb.Button(self.lblframe_botones_listven, text='Nuevo', width=15,bootstyle="success",command=self.ventana_nueva_venta)
        btn_nuevo_venta.grid(row=0,column=0, padx=5,pady=5)
        btn_modificar_venta= tb.Button(self.lblframe_botones_listven, text='Modificar', width=15,bootstyle="warning")
        btn_modificar_venta.grid(row=0,column=1, padx=5,pady=5)
        btn_eliminar_venta= tb.Button(self.lblframe_botones_listven, text='Eliminar', width=15,bootstyle="danger")
        btn_eliminar_venta.grid(row=0,column=2, padx=5,pady=5)   
        
        self.lblframe_busqueda_listven=LabelFrame(self.frame_lista_productos)
        self.lblframe_busqueda_listven.grid(row=1, column=0,padx=10,pady=10,sticky=NSEW)
        
        txt_busqueda_venta=ttk.Entry(self.lblframe_busqueda_listven, width=95)
        txt_busqueda_venta.grid(row=0,column=0,padx=5,pady=5)
        
        #=====================Treeview===================
        
        self.lblframe_tree_listven=LabelFrame(self.frame_lista_ventas)
        self.lblframe_tree_listven.grid(row=2, column=0,padx=10,pady=10,sticky=NSEW)
        
        columnas=("codigo","cantidad", "descripcion", "precio_pesos", "fecha")
        
        self.tree_lista_ventas= tb.Treeview(self.lblframe_tree_listven, columns=columnas,
                                          height=17,show='headings',bootstyle='dark')
        self.tree_lista_ventas.grid(row=0, column=0)
        
        self.tree_lista_ventas.heading("codigo", text="Codigo", anchor=W)
        self.tree_lista_ventas.heading("cantidad", text="Cantidad", anchor=W)
        self.tree_lista_ventas.heading("descripcion", text="Descripcion", anchor=W)
        self.tree_lista_ventas.heading("precio_pesos", text="Precio Pesos", anchor=W)
        self.tree_lista_ventas.heading("fecha", text="Fecha", anchor=W)
        #self.tree_lista_productos['displaycolumns']=("codigo","descripcion","precio pesos","precio dolar")#para ocultar la clave solo apareceran codigo nombre y rol# sirve para ocultar toda la ventana 
        
        #Crear el scrolbar
        tree_scroll_listven=tb.Scrollbar(self.frame_lista_ventas, bootstyle='round-success')
        tree_scroll_listven.grid(row=2, column=1)
        #Configurar el scrolbar
        tree_scroll_listven.config(command=self.tree_lista_ventas.yview)
        
        self.mostrar_ventas()
              
    def mostrar_ventas(self): # con esta funcion se llama a la BD y se muestra los datos contenidos en ella  es utilizada al final de la funcion que implenta cada boton
        try:
            miConexion=sqlite3.connect('Ventas.db')
            miCursor= miConexion.cursor()
            registros=self.tree_lista_ventas.get_children()
            for elementos in registros:
                self.tree_lista_ventas.delete(elementos)
            miCursor.execute("SELECT * FROM Ventas") 
            datos=miCursor.fetchall()   
            for row in datos:
                self.tree_lista_ventas.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3]))
            miConexion.commit()
            miConexion.close()   
             
        except: 
              messagebox.showerror("Lista de Ventas","Ocurrio un error al mostrar la lista de ventas")            
        
    def ventana_nueva_venta(self):
        
        self.frame_nueva_venta=Toplevel(self)
        self.frame_nueva_venta.title('Nueva Venta')
        self.frame_nueva_venta.geometry('600x600')
        self.frame_nueva_venta.resizable(0,0)
        self.frame_nueva_venta.grab_set()
        
        lblframe_nueva_venta=LabelFrame(self.frame_nueva_venta)
        lblframe_nueva_venta.grid(row=0,column=0,sticky=NSEW,padx=10,pady=10)
        
        lbl_codigo_nueva_venta=Label(lblframe_nueva_venta, text='Codigo')
        lbl_codigo_nueva_venta.grid(row=0, column=0, padx=10,pady=10) 
        self.txt_codigo_nueva_venta=Entry(lblframe_nueva_venta, width=40)
        self.txt_codigo_nueva_venta.grid(row=0, column=1, padx=10,pady=10)
        
        lbl_cantidad_nueva_venta=Label(lblframe_nueva_venta, text='Cantidad')
        lbl_cantidad_nueva_venta.grid(row=1, column=0, padx=10,pady=10) 
        self.txt_cantidad_nueva_venta=Entry(lblframe_nueva_venta, width=40)
        self.txt_cantidad_nueva_venta.grid(row=1, column=1, padx=10,pady=10)
        
        lbl_descripcion_nueva_venta=Label(lblframe_nueva_venta, text='Descripcion')
        lbl_descripcion_nueva_venta.grid(row=2, column=0, padx=10,pady=10) 
        self.txt_descripcion_nueva_venta=Entry(lblframe_nueva_venta, width=40)
        self.txt_descripcion_nueva_venta.grid(row=2, column=1, padx=10,pady=10)
        
        lbl_precio_pesos_nueva_venta=Label(lblframe_nueva_venta, text='Precio pesos')
        lbl_precio_pesos_nueva_venta.grid(row=3, column=0, padx=10,pady=10) 
        self.txt_precio_pesos_nueva_venta=Entry(lblframe_nueva_venta, width=40)
        self.txt_precio_pesos_nueva_venta.grid(row=3, column=1, padx=10,pady=10)
        
        lbl_fecha_nueva_venta=Label(lblframe_nueva_venta, text='Fecha')
        lbl_fecha_nueva_venta.grid(row=4, column=0, padx=10,pady=10) 
        self.txt_fecha_nueva_venta=Entry(lblframe_nueva_venta, width=40)
        self.txt_fecha_nueva_venta.grid(row=4, column=1, padx=10,pady=10)
        
        btn_guardar_nueva_venta=ttk.Button(lblframe_nueva_venta, text='Guardar',width=38,command=self.guardar_venta)
        btn_guardar_nueva_venta.grid(row=5,column=1,padx=10,pady=10)   
        
        #LLAMADA A LA FUNCION ULTIMO_PRODUCTO HAY QUE IMPLEMENTAR    
 
    def guardar_venta(self): 
        if self.txt_codigo_nueva_venta.get()=="" or self.txt_cantidad_nueva_venta.get()=="" or self.txt_descripcion_nueva_venta.get()=="" or self.txt_precio_pesos_nueva_venta.get()=="" or self.txt_fecha_nueva_venta.get()=="":
            
            messagebox.showwarning('Guardando ventas',"Algun campo no es valido por favor revise")  
            return    
        try:
            miConexion=sqlite3.connect('Ventas.db')
            miCursor= miConexion.cursor()
            datos_guardar_venta=(self.txt_codigo_nueva_venta.get(), self.txt_cantidad_nueva_venta.get(),self.txt_descripcion_nueva_venta.get(),self.txt_precio_pesos_nueva_venta.get(),self.txt_fecha_nueva_venta.get()) #se guarda como una tupla
            miCursor.execute("INSERT INTO Ventas VALUES(?,?,?,?,?)",datos_guardar_venta) 
            messagebox.showinfo('Guardando Venta', "Venta Guardada Correctamente")
            miConexion.commit()
            self.frame_nueva_venta.destroy() #cierra la ventana
            self.ventana_lista_ventas()#cargamos la ventana para ver los cambios
            miConexion.close()   
             
        
        except sqlite3.Error as e:
            messagebox.showerror("Guardando Venta", f"Ocurrió un error al guardar venta: {str(e)}")     

#========================================COMPRAS======================================#
    def ventana_lista_compras(self): #ventana madre sobre la cual edificar el resto de los botones 
        self.frame_lista_compras= Frame(self.frame_center)
        self.frame_lista_compras.grid(row=0, column=0,columnspan=2,sticky=NSEW)
        
        self.lblframe_botones_listcom=LabelFrame(self.frame_lista_compras)
        self.lblframe_botones_listcom.grid(row=0, column=0,padx=10,pady=10,sticky=NSEW)
        
        btn_nueva_compra= tb.Button(self.lblframe_botones_listcom, text='Nuevo', width=15,bootstyle="success")
        btn_nueva_compra.grid(row=0,column=0, padx=5,pady=5)
        btn_modificar_compra= tb.Button(self.lblframe_botones_listcom, text='Modificar', width=15,bootstyle="warning")
        btn_modificar_compra.grid(row=0,column=1, padx=5,pady=5)
        btn_eliminar_compra= tb.Button(self.lblframe_botones_listcom, text='Eliminar', width=15,bootstyle="danger")
        btn_eliminar_compra.grid(row=0,column=2, padx=5,pady=5)   
        
        self.lblframe_busqueda_listcom=LabelFrame(self.frame_lista_compras)
        self.lblframe_busqueda_listcom.grid(row=1, column=0,padx=10,pady=10,sticky=NSEW)
        
        txt_busqueda_compra=ttk.Entry(self.lblframe_busqueda_listcom, width=95)
        txt_busqueda_compra.grid(row=0,column=0,padx=5,pady=5)
        
        #=====================Treeview===================
        
        self.lblframe_tree_listcom=LabelFrame(self.frame_lista_compras)
        self.lblframe_tree_listcom.grid(row=2, column=0,padx=10,pady=10,sticky=NSEW)
        
        columnas=("codigo","cantidad", "descripcion", "precio_pesos","precio dolar", "fecha")
        
        self.tree_lista_compras= tb.Treeview(self.lblframe_tree_listcom, columns=columnas,
                                          height=17,show='headings',bootstyle='dark')
        self.tree_lista_compras.grid(row=0, column=0)
        
        self.tree_lista_compras.heading("codigo", text="Codigo", anchor=W)
        self.tree_lista_compras.heading("cantidad", text="Cantidad", anchor=W)
        self.tree_lista_compras.heading("descripcion", text="Descripcion", anchor=W)
        self.tree_lista_compras.heading("precio_pesos", text="Precio Pesos", anchor=W)
        self.tree_lista_compras.heading("precio_dolar", text="Precio Dolar", anchor=W)
        self.tree_lista_compras.heading("fecha", text="Fecha", anchor=W)
        #self.tree_lista_productos['displaycolumns']=("codigo","descripcion","precio pesos","precio dolar")#para ocultar la clave solo apareceran codigo nombre y rol# sirve para ocultar toda la ventana 
        
        #Crear el scrolbar
        tree_scroll_listcom=tb.Scrollbar(self.frame_lista_compras, bootstyle='round-success')
        tree_scroll_listcom.grid(row=2, column=1)
        #Configurar el scrolbar
        tree_scroll_listcom.config(command=self.tree_lista_compras.yview)
        
        self.mostrar_compras()
        
    def mostrar_compras(self): # con esta funcion se llama a la BD y se muestra los datos contenidos en ella  es utilizada al final de la funcion que implenta cada boton
        try:
            miConexion=sqlite3.connect('Ventas.db')
            miCursor= miConexion.cursor()
            registros=self.tree_lista_compras.get_children()
            for elementos in registros:
                self.tree_lista_compras.delete(elementos)
            miCursor.execute("SELECT * FROM Compras") 
            datos=miCursor.fetchall()   
            for row in datos:
                self.tree_lista_compras.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3],row[4],row[5]))
            miConexion.commit()
            miConexion.close()   
             
        except: 
              messagebox.showerror("Lista de Compras","Ocurrio un error al mostrar la lista de compras")            
    
        
def main(): 
    app=Ventana()
    app.title('Sistema de Ventas')
    app.state('zoomed')
    tb.Style('superhero')
    app.mainloop() 

if __name__=='__main__': 
    main() 
