from tkinter import *
from tkcalendar import *  # Need "pip install tkcalendar"
from tkinter import messagebox
import tkinter.font as tkFont
root = Tk()
dateEntry = "Date"
row_num = 0

screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight() #Grabs device resolution

# Window Geometry Calculations
window_height = int(screen_height / 3) # Deciding window height based on screen size, so no matter what display, window will always take up 50%
window_width = int(screen_width / 3) # Deciding window width based on screen size, so no matter what display, window will always take up 50%%

margin_width = int(screen_width / 2 - window_width / 2) # Adding padding so window will always appear in the middle
margin_height = int(screen_height / 2 - window_height / 2) # Screen_height - Window_Height = Empty space on the side / 2 since we want the window to be in the middle

def append_entries():
        print("Appended")
    
def hide():
    root2.withdraw()

def delete_row():
    global row_num
    row_number = row_num_entry.get() # Obtains the number inside the row box
    print(row_number)
    if row_number == "0":
        messagebox.showerror(title="Row Error", message="Cannot delete row 0")
    else:
        Label(root2, text="      ").grid(column=0, row=row_number)
        Label(root2, text="                ").grid(column=1, row=row_number)
        Label(root2, text="                ").grid(column=2, row=row_number)
        Label(root2, text="                ").grid(column=3, row=row_number)
        Label(root2, text="                ").grid(column=4, row=row_number)
        Label(root2, text="                               ").grid(column=5, row=row_number)
        Label(root2, text="                ").grid(column=6, row=row_number)
        Label(root2, text="                ").grid(column=7, row=row_number)
        row_num = row_num - 1


def print_entries():
    global row_num
    for entry in allEntries:
        row_num = row_num + 1
        Label(root2, text=row_num, width=5).grid(column=0, row=row_num, sticky=W, padx=(0, 5))
        Label(root2, text=entry[0], width=12).grid(column=1, row=row_num, sticky=W)
        Label(root2, text=entry[1], width=10).grid(column=2, row=row_num, sticky=W)
        Label(root2, text=entry[2], width=10).grid(column=3, row=row_num, sticky=W)
        Label(root2, text=entry[3], width=10).grid(column=4, row=row_num, sticky=W)
        Label(root2, text=entry[4], width=10).grid(column=5, row=row_num, sticky=W) 
        Label(root2, text=entry[5], width=12).grid(column=6, row=row_num, sticky=W)
        Label(root2, text=entry[6], width=10).grid(column=7, row=row_num, sticky=W)
        

def new_window():
    try:
        global root2
        global row_num_entry
        
        if root2.winfo_exists():   # python will raise an exception there if variable doesn't exist
            root2.deiconify()
            pass
        else:
            root2 = Toplevel()
            # Root2 Iconify Button / Bottom Row

            row_num_entry = Entry(root2, font=buttons_font, bg="white", width=int(2 * RATIO))
            row_num_entry.grid(row=100, column=2, padx=5, pady=15)
            del_button = Button(root2, font=buttons_font, text="Delete", bg="white", width=int(5 * RATIO), command=delete_row)
            del_button.grid(row=100, column=3)


            hide_button = Button(root2, bg="white", text="Hide", font=buttons_font, width=int(10 * RATIO), command=hide)
            hide_button.grid(row=100, column=5)
            # Entries Frame
            Label(root2, text="0", width=5).grid(column=0, row=0, sticky=W, padx=(0, 5))
            Label(root2, text="Leader's Name", width=12).grid(column=1, row=0, sticky=W)
            Label(root2, text="Location", width=10).grid(column=2, row=0, sticky=W)
            Label(root2, text="Member", width=10).grid(column=3, row=0, sticky=W)
            Label(root2, text="Weather", width=10).grid(column=4, row=0, sticky=W)
            Label(root2, text= "Date",  width=10).grid(column=5, row=0, sticky=W) 
            Label(root2, text="Staying/Moving", width=12).grid(column=6, row=0, sticky=W)
            Label(root2, text= "Day/Night", width=10).grid(column=7, row=0, sticky=W)

    except:  # exception 
            root2 = Toplevel()
            # Root2 Iconify Button / Bottom Row

            row_num_entry = Entry(root2, font=buttons_font, bg="white", width=int(2 * RATIO))
            row_num_entry.grid(row=100, column=2, padx=5, pady=15)
            del_button = Button(root2, font=buttons_font, text="Delete", bg="white", width=int(5 * RATIO), command=delete_row)
            del_button.grid(row=100, column=3)


            hide_button = Button(root2, bg="white", text="Hide", font=buttons_font, width=int(10 * RATIO), command=hide)
            hide_button.grid(row=100, column=5)
            # Entries Frame
            Label(root2, text="0", width=5).grid(column=0, row=0, sticky=W, padx=(0, 5))
            Label(root2, text="Leader's Name", width=12).grid(column=1, row=0, sticky=W)
            Label(root2, text="Location", width=10).grid(column=2, row=0, sticky=W)
            Label(root2, text="Member", width=10).grid(column=3, row=0, sticky=W)
            Label(root2, text="Weather", width=10).grid(column=4, row=0, sticky=W)
            Label(root2, text= "Date",  width=10).grid(column=5, row=0, sticky=W) 
            Label(root2, text="Staying/Moving", width=12).grid(column=6, row=0, sticky=W)
            Label(root2, text= "Day/Night", width=10).grid(column=7, row=0, sticky=W)

    root2.geometry(f'{window_width}x{window_height}+{margin_width}+{margin_height}') #Geometry of window in order : Win_X, Win_Y, PadX, PadY
    root2.resizable(False, False) #Can't resize window
    root2.title("Sunshine Adventure Camp Entries")



def pickDate(): # Command for calender to show up
    def dateEntrySet():
        global dateEntry
        dateEntry = cal.selection_get()
        date.set(dateEntry)
        calendarWindow.destroy()
        print(dateEntry)

    calendarWindow = Toplevel() #Creates a separate window
    calendarWindow.geometry(f'280x200+{margin_width}+{margin_height}') # window geometry
    

    cal = Calendar(calendarWindow, selectmode="day", year=2023, month=4, day=30) # Calendar
    cal.pack()
    Button(calendarWindow, text="Choose Date", command=dateEntrySet, width=18).pack()



RATIO = 1
RATIO *= screen_width / 1920 # Since I'm programming on a 1920 x 1080 resolution screen, I use Ratio so that if some one else views this program with a 4k screen (3840 x 2160),
#The font would be twice as big, (RATIO *= 3840 / 1920 = 2)

title_font = tkFont.Font(family="Helvetica",size=int(24 * RATIO),weight="bold") #Making a preset Title Font so I don't need to type the same options.
buttons_font = tkFont.Font(family="Helvetica",size=int(12 * RATIO),weight="bold") #Making a perset Buttons Font so I don't need to type the options.
text_font = tkFont.Font(family="Helvetica", size=int(10 * RATIO), weight="bold")

root.title("Sunshine Adventure Camp")

root.grid_rowconfigure(1, weight=1)  #Configuring weight of row '1', that means that if there's extra space, anything placed in row 0 will take up all that extra space
root.grid_columnconfigure(0, weight=1)  #Same as above, but configuring column '0' instead.
root.grid_columnconfigure(1, weight=1)  #Same as above, but configuring column '1' instead.
    
frame1 = Frame(root, bg="green", padx = 15, pady = 1) 
entry_frame = Frame(root, bg="tan", padx=15,) #Setting up individual containers in overall window, can think of it like 'div' inside html
functional_buttons_frame = Frame(root, bg="purple", padx=15, pady=15)


functional_buttons_frame.grid_columnconfigure((0,2,4,6), weight=1) #Configuring frame2's grid layout column weight to be different, so now column 0, 2, and 4 will take as much space 
#as possible, pushing everything in column 1, 3 and 5 to the centre


# Displaying the frame1 in row 0 and column 0
frame1.grid(row=0, column=0, sticky="nsew", columnspan=2)
entry_frame.grid(row=1, column=0, sticky="nsew", columnspan=2)
functional_buttons_frame.grid(row=2, column=0, sticky="ew", columnspan=2)


# Widgets being placed inside 'frame1'
title = Label(frame1, text="Sunshine Adventure Camp", bg="green", font=title_font).pack()


# Widgets being placed inside 'entry_frame'

#Leader's Label and Entry Box
Label(entry_frame, text="Leader's Name", font=text_font, bg="tan").grid(row=0, column=0, sticky='e', pady=(int(15 * RATIO)))
leader_name = Entry(entry_frame, width=int(18 * RATIO), font=text_font)
leader_name.grid(row=0, column=1, padx=(int(15 * RATIO), 0), pady=(int(15 * RATIO)), sticky='w')


# No. Group Members Label and Dropdown Menu
Label(entry_frame, text="No.Group Members", font=text_font, bg="tan").grid(row=0, column=2, padx=(int(30 * RATIO), 0), pady=(int(15 * RATIO)))
members = IntVar()
members.set(5)
group_member_entry = OptionMenu(entry_frame, members, "5", "6", "7", "8", "9", "10", )
group_member_entry.configure(width=int(14 * RATIO))
group_member_entry.grid(row=0, column=3, padx=(int(15 * RATIO), 0), pady=(int(15 * RATIO)), sticky="w")


# Weather Label and Dropdown Menu
Label(entry_frame, text="Weather Condition", font=text_font, bg="tan").grid(row=1, column=0, pady=(int(15 * RATIO)))
weathers = StringVar()
weathers.set("Sunny")
weather_conditions = OptionMenu(entry_frame, weathers, "Sunny", "Cloudy", "Raining", "Windy", "Storming", "Snowing")
weather_conditions.configure(width=int(14 * RATIO))
weather_conditions.grid(row=1, column=1, padx=(int(15 * RATIO), 0), pady=(int(15 * RATIO)), sticky="w")


# Location Label and Entry Point
Label(entry_frame, text="Location", font=text_font, bg="tan").grid(row=1, column=2, padx=(int(30 * RATIO), 0), pady=(int(15 * RATIO)), sticky="e")
location_entry = Entry(entry_frame, width=int(18 * RATIO), font=text_font)
location_entry.grid(row=1, column=3, pady=(int(15 * RATIO)),padx=(int(15 * RATIO), 0), sticky="w")


# Calender Selector and Label
date_label = Label(entry_frame, text="Date", font=text_font, bg="tan").grid(row=2, column=0, sticky="e")
date = StringVar()
date.set("Pick A Date")
entry_date = Button(entry_frame, textvariable=date, width=int(17 * RATIO), command=pickDate)
entry_date.grid(row=2, column=1, sticky="w", padx=(int(15 * RATIO)))


# Staying/Moving Dropdown
Label(entry_frame, text="Staying/Moving", font=text_font, bg="tan").grid(row=2, column=2, padx=(int(30 * RATIO), 0), pady=(int(15 * RATIO)), sticky="e")
staying_or_moving = StringVar()
staying_moving_entry = OptionMenu(entry_frame, staying_or_moving, "Moving", "Staying")
staying_moving_entry.configure(width=int(14 * RATIO))
staying_moving_entry.grid(row=2, column=3,padx=(int(15 * RATIO)), pady=(int(15 * RATIO)), sticky="w")


# Day and Night Dropdown
Label(entry_frame, text="Day/Night", font=text_font, bg="tan").grid(row=3, column=0, pady=(int(15 * RATIO)), sticky="e")
day_night_time = StringVar()
day_night = OptionMenu(entry_frame, day_night_time, "Day", "Night")
day_night.configure(width=int(14 * RATIO))
day_night.grid(row=3, column=1,padx=(int(15 * RATIO)), pady=(int(10 * RATIO)), sticky="w")



def submit():
    while True:
        global row_num
        name = leader_name.get()
        location = location_entry.get()
        member = members.get()
        weather = weathers.get()
        staying_moving = staying_or_moving.get()
        day_night = day_night_time.get()

        for i in name:
            num_true = i.isnumeric()

        if name == "":
            messagebox.showerror(title="Name Error", message="Please Enter a Name")
            break
        elif num_true == True:
            messagebox.showerror(title="Name Integer Error", message="There's an Integer in the Name")
            break

        if location == "":
            messagebox.showerror(title="Location Error", message="Please Enter a Location")
            break

        if dateEntry == "Date":
            messagebox.showerror(title="Date Error", message="Please Select a Date")
            break

        if staying_moving == "":
            messagebox.showerror(title="Staying/Moving Error", message="Please Select Staying or Moving")
            break

        if day_night == "":
            messagebox.showerror(title="Time Error", message="Please Select Day or Night")
            break
        
        new_window()
        
        leader_name.delete(0, END)
        location_entry.delete(0, END)
        members.set(5)
        weathers.set("Sunny")
        staying_or_moving.set("")
        day_night_time.set("")
        

        global allEntries
        allEntries = []
        newEntry = []   
        newEntry.append(name)
        newEntry.append(location)
        newEntry.append(member)
        newEntry.append(weather)
        newEntry.append(dateEntry)
        newEntry.append(staying_moving)
        newEntry.append(day_night)
        allEntries.append(newEntry)

        print(newEntry)
        if row_num >= 0:
            print_entries()
        else:
            row_num = 0
            print_entries()
        
        break


# Widgets being placed inside 'functional_buttons_frame'
quit_button = Button(functional_buttons_frame, text="Quit", bg="white", command=root.quit, width=int(10 * RATIO), height=1, font=buttons_font).grid(row=0, column=5)
submit_button = Button(functional_buttons_frame, text="Submit", bg="white", command=submit, width=int(10 * RATIO), height=1, font=buttons_font).grid(row=0, column=3)
entries_window = Button(functional_buttons_frame, text="View Entires", bg="white", command=new_window, width=int(10 * RATIO), height=1, font=buttons_font).grid(row=0, column=1)



root.geometry(f'{window_width}x{window_height}+{margin_width}+{margin_height}') # Geometry of window in order : Win_X, Win_Y, PadX, PadY
root.resizable(False, False) # Can't resize window

mainloop()
