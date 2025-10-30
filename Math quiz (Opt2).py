# Tutorial 1
import tkinter as tk
from tkinter import Menu

# root window
root = tk.Tk()
root.title('Menu Demo')

# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)

# add a menu  item to the menu
file_menu.add_command(
    label="Exit",
    command=root.destroy
)

# add the File menu to the menubar
menubar.add_cascade(
    label="File",
    menu=file_menu
)

root.mainloop()

# Tutorial 2
from tkinter import Tk, Menu

# root window
root = Tk()
root.geometry('320x150')
root.title('Menu Demo')

# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create the file_menu
file_menu = Menu(
    menubar,
    tearoff=0
)

# add menu items to the File menu
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Close')
file_menu.add_separator()  # Corrected typo here

# add Exit menu item
file_menu.add_command(
    label='Exit',
    command=root.destroy
)

# add the File menu to the menubar
menubar.add_cascade(
    label="File",
    menu=file_menu
)

# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

# add the Help menu to the menubar
menubar.add_cascade(
    label="Help",
    menu=help_menu
)

root.mainloop()

# Tutorial 3
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def _init_(self):
        super()._init_()
        self.geometry("320x80")
        self.title("Tkinter OptionMenu Widget")

        # initialize data
        self.languages = ('Python', 'Javascript', 'Java', 'Swift', 'GoLang', 'C#', 'C++', 'Scala')

        # set up variable
        self.option_var = tk.StringVar(self)

        # create widget
        self.create_widgets()

    def create_widgets(self):
        # padding for widgets using the grid layout
        paddings = {'padx': 5, 'pady': 5}

        # label
        label = ttk.Label(self, text='Select your most favourite language:')
        label.grid(column=0, row=0, sticky=tk.W, **paddings)

        # option menu
        option_menu = ttk.OptionMenu(
            self,
            self.option_var,
            self.languages[0],
            *self.languages,
            command=self.option_changed)

        option_menu.grid(column=1, row=1, sticky=tk.W, **paddings)

        # output label
        self.output_label = ttk.Label(self, foreground='red')
        self.output_label.grid(column=0, row=1, sticky=tk.W, **paddings)

    def option_changed(self, *args):
        self.output_label['text'] = f'You selected: {self.option_var.get()}'

if __name__ == "__main__":
    app = App()
    app.mainloop()

# Tutorial 4
# Import tkinter library
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame or window
win = Tk()

# Set the geometry of tkinter frame
win.geometry("750x250")


# Define a new function to open the window
def open_win():
    new = Toplevel(win)
    new.geometry("750x250")
    new.title("New Window")

    # Create a label in the New Window
    Label(new, text="Hey Howdy?", font=('Helvetica 17 bold')).pack(pady=30)


# Create a label
Label(win, text="Click the below button to open a New Window", font=('Helvetica 17 bold')).pack(pady=30)

# Create a button to open a New Window
ttk.Button(win, text="Open", command=open_win).pack()

win.mainloop()

# Tutorial 5
import tkinter as tk

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):
    def _init_(self, *args, **kwargs):
        tk.Tk._init_(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def _init_(self, parent, controller):
        tk.Frame._init_(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = tk.Button(self, text="Visit Page 2", command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):
    def _init_(self, parent, controller):
        tk.Frame._init_(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two", command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):
    def _init_(self, parent, controller):
        tk.Frame._init_(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One", command=lambda: controller.show_frame(PageOne))
        button2.pack()


app = SeaofBTCapp()
app.mainloop()

# Tutorial 6
import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Initialize frames to an empty dictionary
        self.frames = {}

        # Iterating through a tuple consisting of the different layouts
        for F in (StartPage, Page1, Page2):
            frame = F(container, self)

            # Initialize frame of that object from
            # StartPage, Page1, Page2 respectively
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # To display the current frame passed as a parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# First window frame StartPage
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Label of StartPage
        label = ttk.Label(self, text="StartPage", font=LARGEFONT)

        # Putting the grid in its place by using grid
        label.grid(row=0, column=4, padx=10, pady=10)

        # Button to show frame Page1
        button1 = ttk.Button(self, text="Page 1", command=lambda: controller.show_frame(Page1))

        # Putting the button in its place by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # Button to show frame Page2
        button2 = ttk.Button(self, text="Page 2", command=lambda: controller.show_frame(Page2))

        # Putting the button in its place by using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# Second window frame Page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Page 1", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # Button to show frame StartPage
        button1 = ttk.Button(self, text="StartPage", command=lambda: controller.show_frame(StartPage))

        # Putting the button in its place by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # Button to show frame Page2
        button2 = ttk.Button(self, text="Page 2", command=lambda: controller.show_frame(Page2))

        # Putting the button in its place by using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# Third window frame Page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # Button to show frame Page1
        button1 = ttk.Button(self, text="Page 1", command=lambda: controller.show_frame(Page1))

        # Putting the button in its place by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # Button to show frame StartPage
        button2 = ttk.Button(self, text="StartPage", command=lambda: controller.show_frame(StartPage))

        # Putting the button in its place by using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# Driver code
app = tkinterApp()
app.mainloop()

# Quick Test
# Import tkinter library
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame or window
win = Tk()

# Set the geometry of tkinter frame
win.geometry("750x250")


# Define a new function to open the window
def open_win():
    new = Toplevel(win)
    new.geometry("750x250")
    new.title("New Window")

    # Create a label in the New Window
    Label(new, text="Hey Howdy?", font=('Helvetica 17 bold')).pack(pady=30)


# Create a label
Label(win, text="Click the below button to open a New Window", font=('Helvetica 17 bold')).pack(pady=30)

# Create a button to open a New Window
ttk.Button(win, text="Open", command=open_win).pack()

# Create a button to open a New Window
ttk.Button(win, text="Close", command=open_win).pack()

win.mainloop()
