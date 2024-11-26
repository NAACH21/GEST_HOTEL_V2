import sys
import os

def resource_path(relative_path):
    """Obtiene la ruta absoluta de los recursos para el ejecutable o script."""
    base_path = getattr(sys, '_MEIPASS', os.path.abspath(".idea"))
    return os.path.join(base_path, relative_path)