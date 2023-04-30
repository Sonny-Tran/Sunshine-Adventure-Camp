from tkinter import *
from Sunshine_Modules import functions
from tkcalendar import Calendar
from tkinter import messagebox
import tkinter.font as tkFont
root = Tk()

screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight() #Grabs device resolution

RATIO = 1
RATIO *= screen_width / 1920 # Since I'm programming on a 1920 x 1080 resolution screen, I use Ratio so that if some one else views this program with a 4k screen (3840 x 2160),
#The font would be twice as big, (RATIO *= 3840 / 1920 = 2)

title_font = tkFont.Font(family="Helvetica",size=int(30 * RATIO),weight="bold") #Making a preset Title Font so I don't need to type the same options.
buttons_font = tkFont.Font(family="Helvetica",size=int(12 * RATIO),weight="bold") #Making a perset Buttons Font so I don't need to type the options.
text_font = tkFont.Font(family="Helvetica", size=int(10 * RATIO), weight="bold")

root.title("Sunshine Adventure Camp")

root.grid_rowconfigure(1, weight=1)  #Configuring weight of row '1', that means that if there's extra space, anything placed in row 0 will take up all that extra space
root.grid_columnconfigure(0, weight=1)  #Same as above, but configuring column '0' instead.
root.grid_columnconfigure(1, weight=1)  #Same as above, but configuring column '1' instead.
    
frame1 = Frame(root, bg="green", padx = 15, pady = 15) 
entry_frame = Frame(root, bg="tan", padx=15, pady=15) #Setting up individual containers in overall window, can think of it like 'div' inside html
functional_buttons_frame = Frame(root, bg="purple", padx=15, pady=15)


functional_buttons_frame.grid_columnconfigure((0,2,4,6), weight=1) #Configuring frame2's grid layout column weight to be different, so now column 0, 2, and 4 will take as much space 
#as possible, pushing everything in column 1, 3 and 5 to the centre


# Displaying the frame1 in row 0 and column 0
frame1.grid(row=0, column=0, sticky="nsew", columnspan=2)
entry_frame.grid(row=1, column=0, sticky="nsew", columnspan=2)
functional_buttons_frame.grid(row=2, column=0, sticky="ew", columnspan=2)


# Widgets being placed inside 'frame1'
title = Label(frame1, text="Sunshine Adventure Camp", bg="green", font=title_font)


# Widgets being placed inside 'entry_frame'

#Leader's Label and Entry Box
Label(entry_frame, text="Leader's Name", font=text_font, bg="tan").grid(row=0, column=0, sticky='w', pady=(int(15 * RATIO)))
leader_name = Entry(entry_frame, width=20, font=text_font).grid(row=0, column=1, padx=(int(15 * RATIO), 0), pady=(int(15 * RATIO)))


#No. Group Members Label and Dropdown Menu
Label(entry_frame, text="No. Group Members", font=text_font, bg="tan").grid(row=0, column=2, padx=(int(40 * RATIO), 0), pady=(int(15 * RATIO)))
members = IntVar()
members.set(5)
group_member_entry = OptionMenu(entry_frame, members, "5", "6", "7", "8", "9", "10", )
group_member_entry.configure(width=12)
group_member_entry.grid(row=0, column=3, padx=(int(15 * RATIO), 0), pady=(int(15 * RATIO)), sticky="w")


#Weather Label and Dropdown Menu
Label(entry_frame, text="Weather Condition", font=text_font, bg="tan").grid(row=1, column=0, pady=(int(15 * RATIO)))
weather = StringVar()
weather_conditions = OptionMenu(entry_frame, weather, "Sunny", "Cloudy", "Raining", "Windy", "Storming", "Snowing")
weather_conditions.configure(width=12)
weather_conditions.grid(row=1, column=1, padx=(int(15 * RATIO), 0), pady=(int(15 * RATIO)))


#Location Label and Entry Point
Label(entry_frame, text="Location", font=text_font, bg="tan").grid(row=1, column=2, padx=(int(40 * RATIO), 0), pady=(int(15 * RATIO)), sticky="w")
location = Entry(entry_frame, width=20, font=text_font, bg="tan").grid(row=1, column=3,padx=(int(15 * RATIO), 0), pady=(int(15 * RATIO)))


# Widgets being placed inside 'functional_buttons_frame
quit_button = Button(functional_buttons_frame, text="Quit", bg="white", command=root.quit, width=int(10 * RATIO), height=1, font=buttons_font)
submit = Button(functional_buttons_frame, text="Submit", bg="white", command=functions.new_window, width=int(10 * RATIO), height=1, font=buttons_font)
entires_window = Button(functional_buttons_frame, text="View Entires", bg="white", command=functions.new_window, width=int(10 * RATIO), height=1, font=buttons_font)


title.pack()


quit_button.grid(row=0, column=5)
submit.grid(row=0, column=3)
entires_window.grid(row=0, column=1)


window_height = int(screen_height / 2) #Deciding window height based on screen size, so no matter what display, window will always take up 50%
window_width = int(screen_width / 3) #Deciding window width based on screen size, so no matter what display, window will always take up 50%%

margin_width = int(screen_width / 2 - window_width / 2) #Adding padding so window will always appear in the middle
margin_height = int(screen_height / 2 - window_height / 2) #Screen_height - Window_Height = Empty space on the side / 2 since we want the window to be in the middle

root.geometry(f'{window_width}x{window_height}+{margin_width}+{margin_height}') #Geometry of window in order : Win_X, Win_Y, PadX, PadY
root.resizable(False, False) #Can't resize window

x, y = entry_frame.grid_size()

print(x)
print(y)

mainloop()
