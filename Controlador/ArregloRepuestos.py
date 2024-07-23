from connection import conexion

class ArregloRepuestos:
    def __init__(self):
        self.productos = []
        self.cargar()  

    def cargar(self):
        try:
            cursor = conexion.cursor()
            sSql = f"SELECT * FROM Inventario"
            cursor.execute(sSql)
            
            print(cursor.fetchall())
        except FileNotFoundError:
            print("No se pudo traer la informacion de la tabla Inventario")

    def grabar(self):
        pass

    def tamanoArregloProducto(self):
        return len(self.productos)

    def adicionaProducto(self, producto):
        self.productos.append(producto)

    def devolverProducto(self, indice):
        return self.productos[indice]

    def buscarProducto(self, codigo):
        for i in range(len(self.productos)):
            if self.productos[i].getCodigo() == codigo:
                return i
        return -1

    def eliminarProducto(self, indice):
        del self.productos[indice]
        self.grabar()