import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Definir el retraso como constante
DELAY = 0.1

# Definir los botones como constantes
BTN_GP15 = board.GP15 # AbrirScreenBrush
BTN_GP14 = board.GP14 # Tecla B
BTN_GP13 = board.GP13 # Tecla A
BTN_GP12 = board.GP12 # Tecla R
BTN_GP11 = board.GP11 # Tecla ` o SHIFT

# Inicializar teclado
teclado = Keyboard(usb_hid.devices)

# Función para configurar botones
def configure_button(pin):
    button = digitalio.DigitalInOut(pin)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.DOWN
    return button

# Configurar botones
btn_screenbrush = configure_button(BTN_GP15)
btn_key_brush = configure_button(BTN_GP14)
btn_key_arrow = configure_button(BTN_GP13)
btn_key_retangle = configure_button(BTN_GP12)
btn_key_lintern = configure_button(BTN_GP11)

# Función para manejar las pulsaciones de teclas
def press_and_release(keyboard, *keycodes):
    keyboard.press(*keycodes)
    time.sleep(DELAY)
    keyboard.release(*keycodes)

# Bucle principal
while True:
    if btn_screenbrush.value:
        print("btn_screenbrush")
        press_and_release(teclado, Keycode.OPTION, Keycode.TAB)
    if btn_key_brush.value:
        print("btn_key_brush")
        press_and_release(teclado, Keycode.B)
    if btn_key_arrow.value:
        print("btn_key_arrow")
        press_and_release(teclado, Keycode.A)
    if btn_key_retangle.value:
        print("btn_key_retangle")
        press_and_release(teclado, Keycode.R)
    if btn_key_lintern.value:
        print("btn_key_lintern")
        press_and_release(teclado, Keycode.LEFT_SHIFT)
    time.sleep(DELAY)
