from tkinter import *
from tkinter import messagebox  


class functions:
    def button_press_test(): #Function to pop up message box saying that user pressed the button
        messagebox.showinfo('You Clicked The Button!', "Here's an apple Buddy.")

    def new_window():
        try:
            global root2
            if root2.winfo_exists():   # python will raise an exception there if variable doesn't exist
                pass
            else:
                root2 = Toplevel()
                screen_width, screen_height = root2.winfo_screenwidth(), root2.winfo_screenheight() #Grabs device resolution
                window_height = int(screen_height / 2) #Deciding window height based on screen size, so no matter what display, window will always take up 50%
                window_width = int(screen_width / 3) #Deciding window width based on screen size, so no matter what display, window will always take up 50%%
                margin_width = int(screen_width / 2 - window_width / 2) #Adding padding so window will always appear in the middle
                margin_height = int(screen_height / 2 - window_height / 2) #Screen_height - Window_Height = Empty space on the side / 2 since we want the window to be in the middle

                root2.geometry(f'{window_width}x{window_height}+{margin_width}+{margin_height}') #Geometry of window in order : Win_X, Win_Y, PadX, PadY
                root2.resizable(False, False) #Can't resize window
            
        except NameError:               # exception? we are now here.  
            root2 = Toplevel()

            screen_width, screen_height = root2.winfo_screenwidth(), root2.winfo_screenheight() #Grabs device resolution
            window_height = int(screen_height / 2) #Deciding window height based on screen size, so no matter what display, window will always take up 50%
            window_width = int(screen_width / 3) #Deciding window width based on screen size, so no matter what display, window will always take up 50%%
            margin_width = int(screen_width / 2 - window_width / 2) #Adding padding so window will always appear in the middle
            margin_height = int(screen_height / 2 - window_height / 2) #Screen_height - Window_Height = Empty space on the side / 2 since we want the window to be in the middle

            root2.geometry(f'{window_width}x{window_height}+{margin_width}+{margin_height}') #Geometry of window in order : Win_X, Win_Y, PadX, PadY
            root2.resizable(False, False) #Can't resize window
        root2.title("Sunshine Adventure Camp Entries")



