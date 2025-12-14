import asyncio
import threading
import json
import base64
import cv2
from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import websockets

# CONFIGURACIÓN
WS_URI = "wss://signaling-server-ec5v.onrender.com"

class AndroidEmisor(App):
    def build(self):
        self.img_widget = Image()
        self.capture = cv2.VideoCapture(0)
        # Iniciar el bucle de red en un hilo separado
        threading.Thread(target=self.start_async_loop, daemon=True).start()
        # Actualizar la interfaz de la app
        Clock.schedule_interval(self.update_ui, 1.0 / 30.0)
        return self.img_widget

    def update_ui(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # Convertir para mostrar en pantalla del celular
            buf = cv2.flip(frame, 0).tostring()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.img_widget.texture = texture
            self.last_frame = frame

    def start_async_loop(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.run_client())

    async def run_client(self):
        while True:
            try:
                async with websockets.connect(WS_URI) as ws:
                    await ws.send("android_device")
                    while True:
                        if hasattr(self, 'last_frame'):
                            # Codificar imagen para enviar al servidor
                            _, buffer = cv2.imencode('.jpg', self.last_frame, [int(cv2.IMWRITE_JPEG_QUALITY), 40])
                            b64_str = base64.b64encode(buffer).decode('utf-8')
                            payload = {"type": "FRAME", "cam": b64_str, "scr": None}
                            await ws.send(json.dumps(payload))
                        await asyncio.sleep(0.1)
            except Exception as e:
                print(f"Error: {e}")
                await asyncio.sleep(5)

if __name__ == '__main__':
    AndroidEmisor().run()