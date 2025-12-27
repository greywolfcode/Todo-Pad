#import libraries
import tkinter as tk
from tkinter import filedialog, ttk
#import images
import assets
#import methods for working with keyconfig files
import keyconfig

#main class, inherites main window from tkinter
class Main(tk.Tk):
    def __init__(self):
        #intisalise parent class
        super().__init__()
        #add title
        self.title("Todo Pad Layout Editor")
        self.current_frame = None
        #add menu bar
        self.option_add('*tearOff', False)
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)
        menu_file = tk.Menu(menu_bar)
        #menu_help = tk.Menu(menu_bar)
        menu_file.add_command(label='Open File', command=lambda: self.current_frame.load_file())
        menu_file.add_command(label='Save File', command=lambda: self.current_frame.save_file())
        menu_file.add_command(label='Exit Program', command=lambda: self.destroy())
        menu_bar.add_cascade(menu=menu_file, label='File')
        #menu_bar.add_cascade(menu=menu_help, label='Help')
        #menu_bar.add_command(label='About', command=lambda: self.new_page(About_Page, 'n'))
        #get icon
        self.icon = tk.PhotoImage(data=assets.icon)
        self.iconphoto(False, self.icon)
        #start maxamized
        self.state('zoomed')
    def new_page(self, new_frame, anchor, *args, **kwargs):
        if self.current_frame != None:
            self.current_frame.destroy()
        self.current_frame = new_frame(self, *args, **kwargs)
        self.current_frame.pack(anchor=anchor, expand=True)
#main editor menu
class Editor_Menu(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        #run parent init
        super().__init__(parent)
        self.parent = parent
        #main frame for storing macropad diagram
        self.macropad = ttk.Frame(self)
        self.selected_button = 0
        self.current_layer = 0
        self.layers = {
            0: "Layer 1",
            1: "Layer 2",
            2: "Layer 3",
        }
        #storage for button values. stores button values inside value for each layer
        self.button_values = {
            0: {
                0: " ",
                1: " ",
                2: " ",
                3: " ",
                4: " ",
                5: " ",
                6: " ",
                7: " ",
                8: " ",
                9: " ",
                10: " ",
                11: " ",            
                },
            1: {
                0: " ",
                1: " ",
                2: " ",
                3: " ",
                4: " ",
                5: " ",
                6: " ",
                7: " ",
                8: " ",
                9: " ",
                10: " ",
                11: " ",
               },
            2: {
                0: " ",
                1: " ",
                2: " ",
                3: " ",
                4: " ",
                5: " ",
                6: " ",
                7: " ",
                8: " ",
                9: " ",
                10: " ",
                11: " ",
            },
        }
        #Modifaction buttons
        self.modifers = ttk.Frame(self)
        self.layer_label = ttk.Label(self.modifers, text="Current Layer: ")
        self.layer_label.grid(row=0, column=0)
        #define layer name input box
        self.layer_value = tk.StringVar()
        self.layer_value.set("Layer 1")
        self.layer_name_input = ttk.Entry(self.modifers, textvariable=self.layer_value)
        self.layer_name_input.grid(row=0, column=2)
        #add enter key event
        self.layer_name_input.bind('<Return>', lambda x: self.layer_return())
        self.layer_buttons = ttk.Button(self.modifers, text="Change Layer", command=lambda: self.change_layer())
        self.layer_buttons.grid(row = 0, column = 3)
        self.modifers.pack()
        #define buttons on keypad
        self.buttons = {}
        self.buttons[0] = ttk.Button(self.macropad, command=lambda:self.set_selected(0))
        self.buttons[0].grid(row=0, column = 0)
        self.buttons[1] = ttk.Button(self.macropad, command=lambda:self.set_selected(1))
        self.buttons[1].grid(row=0, column = 1)
        self.buttons[2] = ttk.Button(self.macropad, command=lambda:self.set_selected(2))
        self.buttons[2].grid(row=0, column = 2)
        self.buttons[3] = ttk.Button(self.macropad, command=lambda:self.set_selected(3))
        self.buttons[3].grid(row=0, column = 3)
        self.buttons[4] = ttk.Button(self.macropad, command=lambda:self.set_selected(4))
        self.buttons[4].grid(row=1, column = 0)
        self.buttons[5] = ttk.Button(self.macropad, command=lambda:self.set_selected(5))
        self.buttons[5].grid(row=1, column = 1)
        self.buttons[6] = ttk.Button(self.macropad, command=lambda:self.set_selected(6))
        self.buttons[6].grid(row=1, column = 2)
        self.buttons[7] = ttk.Button(self.macropad, command=lambda:self.set_selected(7))
        self.buttons[7].grid(row=1, column = 3)
        self.buttons[8] = ttk.Button(self.macropad, command=lambda:self.set_selected(8))
        self.buttons[8].grid(row=2, column = 0)
        self.buttons[9] = ttk.Button(self.macropad, command=lambda:self.set_selected(9))
        self.buttons[9].grid(row=2, column = 1)
        self.buttons[10] = ttk.Button(self.macropad, command=lambda:self.set_selected(10))
        self.buttons[10].grid(row=2, column = 2)
        self.buttons[11] = ttk.Button(self.macropad, command=lambda:self.set_selected(11))
        self.buttons[11].grid(row=2, column = 3)
        self.macropad.pack()
        #define button id input box
        self.entry_label = ttk.Label(self, text='Current Value:')
        self.entry_label.pack()
        self.button_value = tk.StringVar()
        self.entry_box = ttk.Entry(self, textvariable=self.button_value)
        self.entry_box.bind('<Return>', lambda x: self.button_return())
        self.entry_box.pack()
        #define save button
        self.save_button = ttk.Button(self, text ="Save File", command=lambda:self.save_file())
        self.save_button.pack()
    def reset_button(self):
        #renable currently selected button
        self.buttons[self.selected_button].config(state=tk.NORMAL)
        #save current layer
        self.save_button_value()
    def set_selected(self, button_num):
        self.reset_button()
        #update current button number
        self.selected_button = button_num
        #disable new button
        self.buttons[self.selected_button].config(state=tk.DISABLED)
        #change current text
        self.button_value.set(self.button_values[self.current_layer][button_num])
        #move cursor back to entry box
        self.entry_box.focus_set()
    def save_file(self):
        #get file path
        filename = filedialog.asksaveasfilename(defaultextension=".keyconfig", filetypes=(("Key Configuration Files", ".keyconfig"), ("All Files", ".*")))
        if filename != "":
            data = keyconfig.write_storage_file(self.button_values, self.layers)
            #write data to file
            with open(filename, "wb") as file:
                file.write(data)
    def load_file(self):
        #get file name
        filename = filedialog.askopenfilename(defaultextension=".keyconfig", filetypes=(("Key Configuration Files", ".keyconfig"), ("All Files", ".*")))
        #cehck if file was selected
        if filename == "":
            return
        #read file
        self.layers, self.button_values = keyconfig.read_storage_file(filename)
        #set default text
        self.current_layer = 0
        self.button_value.set(self.button_values[self.current_layer][0])
        self.layer_value.set(self.layers[self.current_layer])
        #set button names
        for num in range(0, 12):
            self.buttons[num].config(text=self.button_values[self.current_layer][num])
        self.set_selected(0)
    def change_layer(self):
        #save current name
        self.layers[self.current_layer] = self.layer_value.get()
        #save current button value
        self.save_button_value()
        #switch layer
        if self.current_layer >= 2:
            self.current_layer = 0
        else:
            self.current_layer += 1
        #update layer name
        self.layer_value.set(self.layers[self.current_layer])
        #set selected button to current button to reset the button value
        self.button_value.set(self.button_values[self.current_layer][self.selected_button])
        #update button names
        for num in range(0, 12):
            self.buttons[num].config(text=self.button_values[self.current_layer][num])
        #move cursor back to entry box
        self.entry_box.focus_set()
    def save_button_value(self):
        self.button_values[self.current_layer][self.selected_button] = self.button_value.get()
        #update button text to be its value
        self.buttons[self.selected_button].config(text=self.button_value.get())
    def layer_return(self):
        self.focus_set()
    def button_return(self):
        if self.selected_button == 11:
            self.set_selected(0)
        else:
            self.set_selected(self.selected_button + 1)

#create new app
app = Main()
app.new_page(Editor_Menu, "center")
#run main loop
app.mainloop()