#import board io stuff
import board
import busio

#import KMK stuff
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry #no images will be used
from kmk.extensions.display.ssd1306 import SSD1306

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

display.entries = [
    TextEntry(text="Todo Pad", x=0, y=0),
    TextEntry(text="Mode: Keyboard", x=0, y=16),
    TextEntry(text="Layer: 1", x=0, y=32),
]
keyboard.extensions.append(display)

#run main loop
if __name__ == '__main__':
    keyboard.go()