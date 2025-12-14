[app]
# Esto hace que el nombre sea "invisible" o transparente en el menú
title =  

# Nombre interno técnico (no se ve en el celu)
package.name = app_transparente
package.domain = org.cliente

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Las librerías que necesita tu código
requirements = python3,kivy,pyjnius,websockets,requests,numpy

orientation = portrait

# EL ICONO: Asegurate de que tu imagen se llame exactamente mi_icono.png
icon.filename = mi_icono.png

android.archs = arm64-v8a, armeabi-v7a
android.api = 31
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1