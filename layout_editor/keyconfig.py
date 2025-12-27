'''  
    Library for working with .keyconfig files for Todo Pad

    File Format:
    Uses UTF-8 for unicode encoding

        Layer Name: U+0002 then 20 bytes
            Button Type: U+0011 then 1 byte. U for unicode, K for KMK
            Button Value: 1 byte storing size, then 1-4 bytes for data

            repeat for every required button
        repeat for every required layer
        
        End of text closing byte \x03
'''

#Lookup table for existing KMK values
KMK_data = {
    "a": "A",
    "b": "B",
    "c": "C",
    "d": "D",
    "e": "E",
    "f": "F",
    "g": "G",
    "h": "H",
    "i": "I",
    "j": "J",
    "k": "K",
    "l": "L",
    "m": "M",
    "n": "N",
    "o": "O",
    "p": "P",
    "q": "Q",
    "r": "R",
    "s": "S",
    "t": "T",
    "u": "U",
    "v": "V",
    "w": "W",
    "x": "X",
    "y": "Y",
    "z": "Z",
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
#get reverse of lookup table
EDITOR_data = {value: key for key, value in KMK_data.items()}

def write_storage_file(data, layers):
    '''Converts data into storage file to be saved'''
    final_string = b""
    #loop through layers
    for layer in layers:
        #add layer header byte
        final_string += b"\x02"
        #add first 20 bytes of layer name
        name = layers[layer].encode("utf-8")
        #add extra spaces to make it the required 20 bytes
        if len(name) < 20:
            name += ' '.encode("utf-8") * (20 -len(name))
        final_string += name[:20]
        #loop through and add buttons
        for button in data[layer].values():
            #add button header byte
            final_string += b"\x11"
            #shrink button to 1st charachter, and make caps if possible
            button_name = button.strip()
            #use lookup table to check if button is a KMK deafult button
            if button_name in KMK_data:
                #add k (KMK) type to final string
                final_string += "k".encode("utf-8")
                button_data = KMK_data[button_name].encode()
                #add bytes for button data length and data
                final_string += len(button_data).to_bytes(1, byteorder="little") #XIAO-RP2040-DIP is little endian
                #add button name
                final_string += button_data
            else:
                button_name = button_name[0] #ensure unicode charachter is 1 charachter
                #add u (Unicode) type to final string
                final_string += "u".encode("utf-8")
                #add bytes for button length and data
                button_data = button_name.encode("utf-8")
                final_string += len(button_data).to_bytes(1, byteorder="little") #XIAO-RP2040-DIP is little endian
                final_string += button_data
    #add closing byte
    final_string += b"\x03"
    return final_string
    
def read_storage_file(path):
    '''Reads .keyconfig file and returns button data'''
    #define button value storage and layer name storage
    layers = {}
    button_values = {}
    with open(path, "rb") as file:
        #read a few bytes at a time 
        while True:
            #check for layer or button header
            header = file.read(1)
            if header == b"\x02": # read layer
                button_values[len(layers)] = {} #add new row of buttons
                layers[len(layers)] = file.read(20).decode("utf-8").strip() #decode name
            elif header == b"\x11": #read button
                #get button type, size and value.
                button_type = file.read(1).decode("utf-8")
                button_size = int.from_bytes(file.read(1), "little")
                button_value = file.read(button_size).decode("utf-8")
                #read input value back from Editor Data
                if button_type == "k": #has a kmk value
                    button_values[len(layers) - 1][len(button_values[len(layers) - 1])] = EDITOR_data[button_value]
                else: #is just a unicode value
                    button_values[len(layers) - 1][len(button_values[len(layers) - 1])] = button_value

            elif header == b"\x03":
                break
    #return final dictionarys
    return layers, button_values
