[app]
title =  
package.name = mibot_app
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,pyjnius,websockets,requests,numpy
orientation = portrait
icon.filename = mi_icono.png
android.archs = arm64-v8a, armeabi-v7a
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
