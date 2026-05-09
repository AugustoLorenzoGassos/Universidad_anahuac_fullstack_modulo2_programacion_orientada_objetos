import hashlib
import datetime

# MIXINS
class AuditableMixin:
    """Añade capacidad de auditoría"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._historial_cambios = []
    
    def _registrar_cambio(self, campo, valor_anterior, valor_nuevo):
        """Registra cambios en los atributos"""
        registro = {
            'timestamp': datetime.datetime.now(),
            'campo': campo,
            'anterior': valor_anterior,
            'nuevo': valor_nuevo
        }
        self._historial_cambios.append(registro)
    
    def obtener_historial(self):
        """Devuelve el historial de cambios"""
        return self._historial_cambios.copy()


class ActivableMixin:
    """Añade capacidad de activar/desactivar"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._activo = True
    
    @property
    def activo(self):
        return self._activo
    
    def activar(self):
        if not self._activo:
            self._activo = True
            return f"{self} activado"
        return f"{self} ya estaba activo"
    
    def desactivar(self):
        if self._activo:
            self._activo = False
            return f"{self} desactivado"
        return f"{self} ya estaba desactivado"


# CLASE PRINCIPAL
class Usuario(AuditableMixin, ActivableMixin):
    """Usuario del sistema con auditoría y activación"""
    
    def __init__(self, username, email, password):
        super().__init__()
        self.username = username
        self._email = None
        self.__password_hash = None
        
        # Usar setters
        self.email = email
        self.__set_password(password)
    
    @property
    def email(self):
        """Getter del email"""
        return self._email
    
    @email.setter
    def email(self, valor):
        """Setter del email con validación"""
        if '@' not in valor or '.' not in valor.split('@')[1]:
            raise ValueError("Email inválido")
        
        anterior = self._email
        self._email = valor
        
        if anterior is not None:
            self._registrar_cambio('email', anterior, valor)
     
    def __set_password(self, password):
        """Método privado para establecer password"""
        if len(password) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        
        self.__password_hash = hashlib.sha256(password.encode()).hexdigest()
        self._registrar_cambio('password', '***', '***')
    
    def cambiar_password(self, password_actual, password_nueva):
        """Cambia la contraseña"""
        if not self.verificar_password(password_actual):
            raise ValueError("Contraseña actual incorrecta")
        
        self.__set_password(password_nueva)
        return "✅ Contraseña cambiada exitosamente"
    
    def verificar_password(self, password):
        """Verifica si la contraseña es correcta"""
        hash_ingresado = hashlib.sha256(password.encode()).hexdigest()
        return hash_ingresado == self.__password_hash
    
    def __str__(self):
        estado = "🟢" if self.activo else "🔴"
        return f"{estado} Usuario: {self.username} ({self.email})"