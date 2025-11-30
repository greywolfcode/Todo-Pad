'''  
    Library for working with .keyconfig files for Todo Pad

    File Format:
    Uses UTF-8 for unicode encoding

        Layer Name: U+0002 then 20 bytes
            Button Type: U+0011 then 1 byte. U for unicode, K for KMK
            Button Value: 1 byte storing size, then 1-4 bytes for data

            repeat for every required button
        repeate for every required layer
'''

#Lookup table for existing KMK values
KMK_data = {
    "A": "A",
    "B": "B",
    "C": "C",
    "B": "B",
    "D": "D",
    "E": "E",
    "F": "F",
    "G": "G",
    "H": "H",
    "I": "I",
    "J": "J",
    "K": "K",
    "L": "L",
    "M": "M",
    "N": "N",
    "O": "O",
    "P": "P",
    "Q": "Q",
    "R": "R",
    "S": "S",
    "T": "T",
    "U": "U",
    "V": "V",
    "W": "W",
    "X": "X",
    "Y": "Y",
    "Z": "Z",
    "0": "N0",
    "1": "N1",
    "2": "N2",
    "3": "N3",
    "4": "N4",
    "5": "N5",
    "6": "N6",
    "7": "N7",
    "8": "N8",
    "9": "N9",
    "!": "N0",
    "@": "N1",
    "#": "N2",
    "$": "N3",
    "%": "N4",
    "^": "N5",
    "&": "N6",
    "*": "N7",
    "(": "N8",
    ")": "N9",
    "enter": "ENT",
    "escape": "ESC",
    "backspace": "BSPC",
    "tab": "TAB",
    "space": "SPC",
    "capslock": "CAPS",
    "f1": "F1",
    "f2": "F2",
    "f3": "F3",
    "f4": "F4",
    "f5": "F5",
    "f6": "F6",
    "f7": "F7",
    "f8": "F8",
    "f9": "F8",
    "f10": "F10",
    "f11": "F11",
    "f12": "F12",
    "f13": "F13",
    "f14": "F14",
    "f15": "F15",
    "f16": "F16",
    "f17": "F17",
    "f18": "F18",
    "f19": "F19",
    "f20": "F20",
    "f21": "F21",
    "f22": "F22",
    "f23": "F23",
    "f24": "F24",
    "printscreen": "PSCR",
    "scrollock": "SCLK",
    "pause": "BRK",
    "insert": "INS",
    "home": "HOME",
    "pageup": "PGUP",
    "right": "RGHT",
    "left": "LEFT",
    "down": "DOWN",
    "up": "UP",
    "numlock": "NLCK",
    "lockingcaps": "LCAP",
    "lockingnum": "LNUM",
    "lockingscroll": "LSCR",
    "leftcontrol": "LCTL",
    "leftshift": "LSFT",
    "leftalt": "LALT",
    "leftgui": "LGUI",
    "rightcontrol": "RCTL",
    "rightshift": "RSFT",
    "rightalt": "RALT",
    "rightgui": "RGUI",
}

def write_storage_file(data, layers):
    '''Converts data into storage file to be saved'''

    final_string = b""

    #loop through layers
    for layer in layers:
        #add layer header byte
        final_string += b"\x02"
        #add first 20 bytes of layer name
        name = layers[layer].encode("utf-8")
        #add extra spac3es to make it the required 20 bytes
        if len(name) < 20:
            name += ' '.encode("utf-8") * (20 -len(name))
        final_string += name[:20]
        #loop through and add buttons
        for button in data[layer]:
            #add button header byte
            final_string += b"\x11"
            #shrink button to 1st charachter, and make caps if possible
            button_name = data[layer][button][0].upper()
            #use lookup table to check if button is a KMK deafult button
            if button_name in KMK_data:
                #add k type to final string
                final_string += "k".encode("utf-8")
                button_data = KMK_data[button_name].encode()
                #add bytes for button data length and data
                final_string += len(button_data).to_bytes(1, byteorder="little") #XIAO-RP2040-DIP is little endian
                final_string += button_data
            else:
                #add u type to final string
                final_string += "u".encode("utf-8")
                #add bytes for button length and data
                button_data = button_name.encode("utf-8")
                final_string += len(button_data).to_bytes(1, byteorder="little") #XIAO-RP2040-DIP is little endian
                final_string += button_data
    return final_string
    
def read_storage_file(path):
    '''Reads .keyconfig file and returns button data'''
    pass