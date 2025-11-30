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
        button0 = ttk.Button(self, command=lambda:self.set_selected(0))
        button1 = ttk.Button(self, command=lambda:self.set_selected(1))
        button2 = ttk.Button(self, command=lambda:self.set_selected(2))
        button3 = ttk.Button(self, command=lambda:self.set_selected(3))
        button4 = ttk.Button(self, command=lambda:self.set_selected(4))
        button5 = ttk.Button(self, command=lambda:self.set_selected(5))
        button6 = ttk.Button(self, command=lambda:self.set_selected(6))
        button7 = ttk.Button(self, command=lambda:self.set_selected(7))
        button8 = ttk.Button(self, command=lambda:self.set_selected(8))
        button9 = ttk.Button(self, command=lambda:self.set_selected(9))
        button10 = ttk.Button(self, command=lambda:self.set_selected(10))
        button11 = ttk.Button(self, command=lambda:self.set_selected(11))
    def set_selected(self, button_num):
        self.selected_button = button_num

#create new app
app = Main()
app.new_page(Editor_Menu, "center")
#run main loop
app.mainloop()