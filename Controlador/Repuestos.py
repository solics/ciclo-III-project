class Repuestos:
    # Método constructor
    def __init__(self,codigo, nombre, marca, categoria, stockActual, precioCompra, precioVenta):

        self.__codigo = codigo
        self.__nombre = nombre
        self.__marca = marca
        self.__Categoria = categoria
        self.__stockActual = stockActual
        self.__precioCompra = precioCompra
        self.__precioVenta = precioVenta

    # Métodos de acceso get y set

    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre
    
    def getMarca(self):
        return self.__marca
    
    def getCategoria(self):
        return self.__Categoria
    
    def getStockActual(self):
        return self.__stockActual
    
    def getPrecioCompra(self):
        return self.__precioCompra
    
    def getPrecioVenta(self):
        return self.__precioVenta

    def setCodigo(self, codigo):
        self.__codigo = codigo
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def setMarca (self, marca):
        self.__marca = marca
    
    def setCategoria(self, categoria):
        self.__Categoria = categoria
    
    def setStockActual(self, stockActual):
        self.__stockActual = stockActual
    
    def setPrecioCompra (self, precioCompra):
        self.__precioCompra = precioCompra
    
    def setPrecioVenta(self, precioVenta):
        self.__precioVenta = precioVenta