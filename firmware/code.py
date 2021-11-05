#pylint: disable = line-too-long
import os
import time
import board
import neopixel
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from pykey.keycode import PK_Keycode as KC
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Hardware definition: GPIO where RGB LED is connected.
pixel_pin = board.A3
num_pixels = 87
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)


# Hardware definition: Switch Matrix Setup.
keys = keypad.KeyMatrix(
    row_pins=(board.GP24, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18),
    column_pins=(board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6,
                 board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13,
				 board.GP19, board.GP20, board.GP21),
    columns_to_anodes=True,
)


# CONFIGURABLES ------------------------

MACRO_FOLDER = '/layers'


# CLASSES AND FUNCTIONS ----------------

class Layer:
    """ Class representing a layer, for which we have a set
        of macro sequences or keycodes"""
    def __init__(self, layerdata):
        self.name = layerdata['name']
        self.macros = layerdata['macros']


# Neopixel update function
def update_pixels(color):
    for i in range(num_pixels):
        pixels[i] = color
    pixels.show()


# INITIALIZATION -----------------------

# Load all the macro key setups from .py files in MACRO_FOLDER
layers = []

files = os.listdir(MACRO_FOLDER)
files.sort()
for filename in files:
    print(filename)
    if filename.endswith('.py'):
        try:
            module = __import__(MACRO_FOLDER + '/' + filename[:-3])
            layers.append(Layer(module.layer))
        except (SyntaxError, ImportError, AttributeError, KeyError, NameError,
                IndexError, TypeError) as err:
            print(err)
            pass

if not layers:
    print('NO MACRO FILES FOUND')
    while True:
        pass

layer_count = len(layers)
# print(layer_count)

def get_active_layer(layer_keys_pressed, layer_count):
    tmp = 0
    if len(layer_keys_pressed)>0:
        for layer_id in layer_keys_pressed:
            if layer_id > tmp: # use highest layer number
                tmp = layer_id
    if tmp >= layer_count:
        tmp = layer_count-1
    return tmp


# setup variables
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
active_keys = []
not_sleeping = True
layer_index = 0

while not_sleeping:
    key_event = keys.events.get()
    if key_event:
        key_number = key_event.key_number

        # keep track of keys being pressed for layer determination
        if key_event.pressed:
            active_keys.append(key_number)
        else:
            active_keys.remove(key_number)

        # reset the layers and identify which layer key is pressed.
        layer_keys_pressed = []
        for active_key in active_keys:
            group = layers[0].macros[active_key][2]
            for item in group:
                if isinstance(item, int):
                    if (item >= KC.LAYER_0) and (item <= KC.LAYER_F) :
                        layer_keys_pressed.append(item - KC.LAYER_0)
        layer_index = get_active_layer(layer_keys_pressed, layer_count)
        # print(layer_index)
        # print(layers[layer_index].macros[key_number][1])
        group = layers[layer_index].macros[key_number][2]
        color = layers[layer_index].macros[key_number][0]
        if key_event.pressed:
            update_pixels(color)
            for item in group:
                if isinstance(item, int):
                    keyboard.press(item)
                else:
                    keyboard_layout.write(item)
        else:
            for item in group:
                if isinstance(item, int):
                    if item >= 0:
                        keyboard.release(item)
            update_pixels(0x000000)
    time.sleep(0.002)
