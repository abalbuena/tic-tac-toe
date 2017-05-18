"""Módulo que contiene las definiciones de los controladores."""
class ControladorMenuPrincipal:
    """Controla la interacción en el menú principal"""

    def __init__(self, interfaz):
        """Inicializacón del controlador"""
        self.interfaz = interfaz

    def menu_principal(self):
        """Muestra el menú principal y maneja la opción seleccionada"""
        opcion_seleccionada = self.interfaz.menu_principal()
        print("El usuario eligió... {0}", opcion_seleccionada)
        