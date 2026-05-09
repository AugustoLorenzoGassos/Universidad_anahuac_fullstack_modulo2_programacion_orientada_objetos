class Producto:
    """Producto con propiedades validadas"""
    
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self._precio = None
        self._stock = None
        
        # Usar los setters para validación inicial
        self.precio = precio
        self.stock = stock
    
    @property
    def precio(self):
        """Getter del precio"""
        return self._precio
    
    @precio.setter
    def precio(self, valor):
        """Setter del precio con validación"""
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        if valor > 1_000_000:
            raise ValueError("El precio es demasiado alto")
        self._precio = valor
    
    @property
    def stock(self):
        """Getter del stock"""
        return self._stock
    
    @stock.setter
    def stock(self, valor):
        """Setter del stock con validación"""
        if valor < 0:
            raise ValueError("El stock no puede ser negativo")
        self._stock = valor
    
    @property
    def valor_inventario(self):
        """Propiedad calculada (solo lectura)"""
        return self._precio * self._stock
    
    @property
    def disponible(self):
        """Propiedad calculada"""
        return self._stock > 0
    
producto_1=Producto("laptop",1000,110)
print(producto_1.valor_inventario)