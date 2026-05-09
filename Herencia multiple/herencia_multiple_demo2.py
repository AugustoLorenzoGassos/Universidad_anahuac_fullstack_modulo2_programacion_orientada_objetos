import datetime
import json

class TimestampMixin:
    """Mixin que añade timestamps de creación y modificación"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
    def touch(self):
        """Actualiza el timestamp de modificación"""
        self.updated_at = datetime.datetime.now()


class SerializableMixin:
    """Mixin que añade capacidad de serialización JSON"""
    
    def to_dict(self):
        """Convierte el objeto a diccionario"""
        return {
            key: str(value) if isinstance(value, datetime.datetime) else value
            for key, value in self.__dict__.items()
        }
    
    def to_json(self):
        """Convierte el objeto a JSON"""
        return json.dumps(self.to_dict(), indent=2)


class ValidacionMixin:
    """Mixin para validación de datos"""
    
    def es_valido(self):
        """Verifica que los atributos requeridos existan"""
        campos_requeridos = getattr(self, 'CAMPOS_REQUERIDOS', [])
        
        for campo in campos_requeridos:
            if not hasattr(self, campo) or getattr(self, campo) is None:
                return False
        return True


# Clase que usa múltiples Mixins
class Articulo(TimestampMixin, SerializableMixin, ValidacionMixin):
    """Artículo de blog con capacidades añadidas por Mixins"""
    
    CAMPOS_REQUERIDOS = ['titulo', 'autor', 'contenido']
    
    def __init__(self, titulo, autor, contenido):
        super().__init__()  # Importante: llama a __init__ de los Mixins
        self.titulo = titulo
        self.autor = autor
        self.contenido = contenido
    
    def __str__(self):
        return f"Artículo: '{self.titulo}' por {self.autor}"
    
articulo_1 = Articulo("Programación orientada a obgetos","René","herencia múltiple")

print(articulo_1.touch())