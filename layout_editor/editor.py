#import libraries
import tkinter as tk
from tkinter import filedialog, ttk
#import images
import assets

#functions for reading and writing to storage files
def write_storage_file(data):
    pass
def read_storage_file(path):
    pass





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
        menu_file.add_command(label='Main Menu', command=lambda: self.new_page(Editor_Menu))
        menu_file.add_command(label='Exit Program', command=lambda: self.destroy())
        menu_bar.add_cascade(menu=menu_file, label='File')
        #menu_bar.add_cascade(menu=menu_help, label='Help')
        #menu_bar.add_command(label='About', command=lambda: self.new_page(About_Page, 'n'))
        #get icon
        #self.icon = ImageTk.PhotoImage(image_storage.icon_image)
        #self.iconphoto(False, self.icon)
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
        #define buttons on keypad
        self.buttons = {}
        self.buttons[0] = ttk.Button(self, command=lambda:self.set_selected(0))
        self.buttons[0].grid(row=0, column = 0)
        self.buttons[1] = ttk.Button(self, command=lambda:self.set_selected(1))
        self.buttons[1].grid(row=0, column = 1)
        self.buttons[2] = ttk.Button(self, command=lambda:self.set_selected(2))
        self.buttons[2].grid(row=0, column = 2)
        self.buttons[3] = ttk.Button(self, command=lambda:self.set_selected(3))
        self.buttons[3].grid(row=0, column = 3)
        self.buttons[4] = ttk.Button(self, command=lambda:self.set_selected(4))
        self.buttons[4].grid(row=1, column = 0)
        self.buttons[5] = ttk.Button(self, command=lambda:self.set_selected(5))
        self.buttons[5].grid(row=1, column = 1)
        self.buttons[6] = ttk.Button(self, command=lambda:self.set_selected(6))
        self.buttons[6].grid(row=1, column = 2)
        self.buttons[7] = ttk.Button(self, command=lambda:self.set_selected(7))
        self.buttons[7].grid(row=1, column = 0)
        self.buttons[8] = ttk.Button(self, command=lambda:self.set_selected(8))
        self.buttons[8].grid(row=1, column = 3)
        self.buttons[9] = ttk.Button(self, command=lambda:self.set_selected(9))
        self.buttons[9].grid(row=2, column = 0)
        self.buttons[10] = ttk.Button(self, command=lambda:self.set_selected(10))
        self.buttons[10].grid(row=2, column = 1)
        self.buttons[11] = ttk.Button(self, command=lambda:self.set_selected(11))
        self.buttons[11].grid(row=2, column = 2)
        self.buttons[12] = ttk.Button(self, command=lambda:self.set_selected(11))
        self.buttons[12].grid(row=2, column = 3)
    def set_selected(self, button_num):
        #renable currently selected button
        self.buttons[self.selected_button].config(state=tk.NORMAL)
        self.selected_button = button_num
        self.buttons[self.selected_button].config(state=tk.DISABLED)

#create new app
app = Main()
app.new_page(Editor_Menu, "center")
#run main loop
app.mainloop()