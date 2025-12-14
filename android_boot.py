from jnius import autoclass
from android.runnable import run_on_ui_thread

# Esto le dice a Android que cuando el sistema arranque, despierte la app
def start_at_boot():
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Intent = autoclass('android.content.Intent')
    # Configuración interna de Android para auto-arranque