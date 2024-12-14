from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
    isAdmin = models.BooleanField(default=False)


    def crearUsuario(self, nombre, email, contraseña, isAdmin=False):
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña
        self.is_admin = isAdmin
        self.save()

    def iniciarSesion(self, email, contraseña):
        usuario = Usuario.objects.filter(email=email, contraseña=contraseña).first()
        if usuario:
            return usuario
        return None

    def getNombre(self):
        return self.nombre

    def setNombre(self, value):
        self.nombre = value
        self.save()

    def getEmail(self):
        return self.email

    def setEmail(self, value):
        self.email = value
        self.save()

    def getContraseña(self):
        return self.contraseña

    def setContraseña(self, value):
        self.contraseña = value
        self.save()

class Admin(Usuario):
    class Meta:
        pass

    def administrarProducto(self, accion, producto):
        pass

    def administrarPedido(self, accion, pedido):
        pass
    
class Producto(models.Model):
    class Meta:
        pass

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=50)



    def agregar(self, admin, nombre, descripcion, precio, stock):
        pass

    def editar(self, admin, idProducto, nuevosDatos):
        pass

    def eliminar(self, admin, idProducto):
        pass

    def listarProductos(self, ):
        pass

    def buscarProductos(self, criterio):
        pass

    def getIdProducto(self, ):
        pass

    def setIdProducto(self, value):
        pass

    def getNombre(self, ):
        pass

    def setNombre(self, value):
        pass

    def getDescripcion(self, ):
        pass

    def setDescripcion(self, value):
        pass

    def getPrecio(self, ):
        pass

    def setPrecio(self, value):
        pass

    def getStock(self, ):
        pass

    def setStock(self, value):
        pass

    def getCategoria(self, ):
        pass

    def setCategoria(self, value):
        pass

class MetodoPago(models.Model):
    class Meta:
        pass

    tipo = models.CharField(max_length=50)
    detalles = models.TextField()


    def validarPago(self, ):
        pass

    def getTipo(self, ):
        pass

    def setTipo(self, value):
        pass

    def getDetalles(self, ):
        pass

    def setDetalles(self, value):
        pass


class Pedido(models.Model):
    class Meta:
        pass

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='PedidoProducto')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha = models.DateTimeField(auto_now_add=True)
    direccion_envio = models.CharField(max_length=255)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=50, default="Pendiente")


    def crearPedido(self, carrito):
        pass

    def calcularTotal(self, ):
        pass

    def actualizarEstado(self, admin, nuevoEstado):
        pass

    def verEstado(self, ):
        pass

    def notificarEstado(self, ):
        pass

    def getIdPedido(self, ):
        pass

    def setIdPedido(self, value):
        pass

    def getUsuario(self, ):
        pass

    def setUsuario(self, value):
        pass

    def getProductos(self, ):
        pass

    def setProductos(self, value):
        pass

    def getTotal(self, ):
        pass

    def setTotal(self, value):
        pass

    def getFecha(self, ):
        pass

    def setFecha(self, value):
        pass

    def getDireccionEnvio(self, ):
        pass

    def setDireccionEnvio(self, value):
        pass

    def getMetodoPago(self, ):
        pass

    def setMetodoPago(self, value):
        pass

    def getEstado(self, ):
        pass

    def setEstado(self, value):
        pass

class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    
class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='CarritoProducto')  

    def agregar_producto(self, producto, cantidad):
        pass

    def eliminar_producto(self, producto, cantidad):
        pass

    def vaciar_carrito(self):
        pass

    def listar_carrito(self):
        pass

    def realizar_pedido(self, direccion, metodo_pago):
        pass

    def get_usuario(self):
        return self.usuario

    def set_usuario(self, value):
        self.usuario = value
        self.save()

    def get_productos(self):
        return self.productos.all()

    def set_productos(self, value):
        self.productos.set(value)
        
class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
        
class Recibo(models.Model):
    class Meta:
        pass

    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    detalles = models.TextField(blank=True)


    def generarRecibo(self, ):
        pass

    def verRecibo(self, ):
        pass

    def getIdRecibo(self, ):
        pass

    def setIdRecibo(self, value):
        pass

    def getPedido(self, ):
        pass

    def setPedido(self, value):
        pass

    def getFechaEmision(self, ):
        pass

    def setFechaEmision(self, value):
        pass

    def getTotal(self, ):
        pass

    def setTotal(self, value):
        pass

    def getDetalles(self, ):
        pass

    def setDetalles(self, value):
        pass

