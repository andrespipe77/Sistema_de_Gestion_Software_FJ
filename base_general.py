"""
Clase abstracta base para las entidades del sistema.
"""

from abc import ABC, abstractmethod

class EntidadBase(ABC):
    """
    Clase abstracta que obliga a implementar validaciones y representación.
    """

    @abstractmethod
    def validar(self):
        pass

    # CORREGIDO: Añadido __str__ abstracto para forzar implementación en todas las entidades
    @abstractmethod
    def __str__(self):
        pass
