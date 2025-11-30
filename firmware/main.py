#import board io stuff
import board
import busio
import os

#import KMK stuff
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry #no images will be used
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.modules.layers import Layers

#set up keyboard object
keyboard = KMKKeyboard()
keyboard.diode_orientation = DiodeOrientation.COL2ROW 
keyboard.col_pins = (board.GP03, board.GP04, board.GP02, board.GP01)
keyboard.row_pins = (board.GP26, board.GP27, board.GP28, board.GP29)

#set up screen
#Don't forget to download circuitpy library for screen
i2c_bus = busio.I2C(board.GP_07, board.GP_06)
driver = SSD1306(i2c=i2c_bus)
display = Display(display=driver)

keyboard.extensions.append(display)
if os.path.exists("keys.keyconfig"):
    keymap = []
    layer_names = []
    #read from keys.config
    k_header = "k".encode("utf-8")
    u_header = "u".encode("utf-8")
    with open("keys.keyconfig", "rb") as file:
        #read a few bytes at a time 
        while True:
            try:
                #check for layer or button header
                header = file.read(1)
                if header == b"\0x2": # read layer
                    keymap.append([])
                    layer_names.append(file.read(20).decode("utf-8"))
                    #top row of buttons is same for all
                    keymap.append([KC.LCTL, KC.NO, KC.NO, KC.TO(len(layer_names))])
                elif header == b"\x11": #read button
                    #add new button row if required
                    if len(keymap[-1]) == 4:
                        keymap.append([])
                    #get button type, size and value
                    button_type = file.read(1)
                    button_size = int.from_bytes(file.read(1), "little")
                    button_value = file.read(button_size).decode("utf-8")
                    #do action based on button type
                    if button_type == k_header:
                        keymap[-1].append(KC.get(button_value, KC.TRANS))
                    elif button_type == u_header:
                        keymap[-1].append()
            except:
                break
        #update final layer switch to loop back to the begining
        keymap[-1][0][3] = KC.TO(0)
    #update display
    display.entries = [
            TextEntry(text="Todo Pad", x=0, y=0),
            TextEntry(text="Mode: Keyboard", x=0, y=16),
            TextEntry(text="Layer: 1", x=0, y=32),
    ]
#if no keys.keyconfig, default to empty keyboard
else:
    keyboard.keymap = [
        [
            KC.TRANS, KC.TRANS, KC.TRANS, KC.TRANS,
            KC.TRANS, KC.TRANS, KC.TRANS, KC.TRANS,
            KC.TRANS, KC.TRANS, KC.TRANS, KC.TRANS,
            KC.TRANS, KC.TRANS, KC.TRANS, KC.TRANS,
        ]
    ]
    #update display
    display.entries = [
        TextEntry(text="Todo Pad", x=0, y=0),
        TextEntry(text="Mode: Keyboard", x=0, y=16),
        TextEntry(text="Install keys.keyconfig to continue", x=0, y=32),
    ]
#run main loop
if __name__ == '__main__':
    keyboard.go()