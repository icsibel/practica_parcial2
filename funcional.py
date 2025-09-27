from collections import deque

#clase articulo para mi futuro carrito
class Articulo:
    def __init__(self, id, nombre, categoria, existencias, preciou, estado=True):
        self.id=id
        self.nombre=nombre
        self.categoria=categoria
        self.existencias= existencias
        self.preciou=preciou
        self.estado=estado

    def activo(self):
        if self.estado==True and self.existencias>0:
            return True
        return False

# clase solo para registrar un cliente HU00001
class Registro_Cliente:
    def __init__(self,cedula , nombre):
        self.cedula=cedula
        self.nombre= nombre 

#clase productos a comprar de HU00002
class Producto: 
    def __init__(self,idArt, nombreArt, categoriaArt, cantidadArt, preciouArt):
        self.idArt=idArt
        self.nombreArt=nombreArt
        self.categoriaArt=categoriaArt
        self.cantidadArt=cantidadArt
        self.preciouArt=preciouArt
    
    #cantidad por precio de cada produto
    def subtotal(self):
        subtotal= self.cantidadArt * self.preciouArt
        return subtotal
    
#clase ventas de HU00002
class Venta:
    def __init__(self, cliente, producto):
        self.cliente=cliente
        self.producto=producto

    def total_vender(self):
        total=0
        for x in self.producto:
            total+= x.subtotal()
        return total

#clase grandota para las acciones
class Supermercado:
    def __init__(self):
        self.turno=deque() #colita
        self.carrito=[] 
        self.clientes_atendidos=[] #pila
        self.productos=[] #inventario
        self.ventas=[]
        self.nuevoid= 1 #para que aumente
        self.categorias=[]
    
    #para HU00002 Y HU00004 porque no sabia donde ponerla, agregar articulo a inventario
    def agregar_articulo(self):
        nombre= input("ingrese nombre del articulo, solo letras y espacios porfis: ")
        categoria= input("ingrese la cetegoria del articulo, solo letras y espacios porfis: ")
        existencias= int(input("ingrese las existencias del articulo; "))
        preciou= int(input("ingrese precio del articulo, solo numeros porfis: "))
        articulo=Articulo(self.nuevoid, nombre, categoria,existencias,preciou, True)
        self.productos.append(articulo)
        self.nuevoid += 1
     
        if categoria not in self.categorias:
            self.categorias.append(categoria)

        print("producto agregado")

    def dar_baja(self):
        art_id_elim=int(input("ingre el id del articulo a elimninar, porfis: "))
        for x in self.productos:
            if art_id_elim == x.id:
                x.estado=False
                print(f"articulo dado de bajajajaj {x.id} con nombre {x.nombre}")
                return
        print("no se encontro un articulo con este id")
    
    def mostrar_inventario(self):
        if len(self.productos) == 0:
            print ("inventario solito")
            return
        for x in self.productos:
            if x.estado==True:
                estado= "activo" 
            else:
                estado="inactivo"
            print("")
            print(f"productos en inventario: \n {x.id} - {x.nombre } - {x.categoria } -  {x.preciou } - {estado}")
            print("")

    def buscar_articulo(self, idArt):
        for x in self.productos:
            if idArt == x.id:
                return x
        print("no se encontro un articulo con este id")
        return None
            

    #de H0001 tomar turno y con clase Registro_cliente y ver la colita
    def tomar_turno(self):
        cedula=int(input("porfavorcito ingrese su cedula: "))
        nombre=input("porfavorcito ingrese su nomnbre: ")
        registro_cliente=Registro_Cliente(cedula, nombre)
        self.turno.append(registro_cliente) #appemde de la colita
        print(f"cliente {nombre} registro un turno... ¡¡BIENVENIDO!!")

    def ver_turno(self): #ver colita
        if len(self.turno) == 0:
            print ("no hay turnos en colita")
            return 
        for x in self.turno:
            print("")
            print(f"turnos en cola: \n {x.nombre}")
            print("") 
    
    #de HU0002 con clase Producto
    def atencion_cliente(self):
        if len(self.turno) == 0:
            print ("no hay turnos en colita")
            return 
        cliente= self.turno.popleft() #mi remove de la colita
        print(f"cliente {cliente.nombre} sera atendido YA")
         
        
        #funcion dentro de mi funcion para mi carrito porque por fuera no funciona porque es de un mismo cliente y no de cualquier otro cliente
        def ver_carrito():
            if len(self.carrito) == 0:
                print ("no hay productos en el carrito")
                return
            for x in self.carrito:
                print("")
                print(f"productos en carrito: \n {x.idArt} - {x.nombreArt } - {x.categoriaArt } - {x.cantidadArt } - {x.preciouArt } subtotal: {x.subtotal()}")
                print("")

        #menu de atencion al usuario de HU00002
        while True:
            print("opciones a realizar: \n 1. agregar articulo \n 2. adescartar ultimo articulo \n 3. ver el carrito \n 4. finalizar compra \n 5. salir sin comprar")
            opcion = input("Seleccione opción: ")
            match opcion:
                case "1": 
                    idArt= int(input("ingrese id del articulo a agregar: "))
                    art=self.buscar_articulo(idArt)
                    if art is None:
                        print("articulo no existe")
                        continue
                    if not art.activo(): #de la funcion activo
                        print("Artículo no disponible")
                        continue 
                    cantidad=int(input("ingrese la cantidad del articulo: "))
                    if cantidad <= 0:
                        print("La cantidad debe ser mayor a 0")
                        continue
                    if cantidad > art.existencias:
                        print(f"cantidad insuficiente. productos disponibles: {art.existencias}.")
                        continue
                    producto=Producto(art.id, art.nombre, art.categoria, cantidad, art.preciou)
                    self.carrito.append(producto)
                    print("producto agregado")
                case "2":
                    if len(self.carrito) >0:
                        eliminar=self.carrito.pop()#eliminar de mi pila
                        print("se descarto el producto" + eliminar.nombre)
                    else:
                        print("carrito vacio")
                case "3":
                    ver_carrito()
                case "4":
                    if len(self.carrito) == 0:
                        print ("no hay productos en el carrito")
                        continue
                    venta=Venta(cliente, self.carrito[:] ) #clase venta
                    for x in self.carrito:
                        art=self.buscar_articulo(x.idArt)
                        if art is not None:
                            art.existencias -= x.cantidadArt
                    self.ventas.append(venta)
                    self.clientes_atendidos.append(cliente) #lista de clientes atndidos
                    print("venta registrada")
                    return 
                case "5":
                    print("cliente sin comprar.")
                    self.clientes_atendidos.append(cliente)
                    return
                case _:
                    print("opcion invalida")
    
    #para HU00003 Estado de la colita
    def ver_cola_pila(self):
        print(f"pendientes: {len(self.turno)}")
        print(f"atendidos:  {len(self.clientes_atendidos)}")
        total_dia = 0
        for x in self.ventas:
            total_dia += x.total_vender()
        print(f"ventas del día : {total_dia}")

