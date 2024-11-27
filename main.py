#main
import os
from tkinter import *
from functions import load_music, show_waveform, clean, funkyButtonFunc, intensityFunc, update_len_freq_diff, alternateRTFunc, displayRTFunc, combineRTFunc

root = Tk()

root.title("Audio Zone")
screen_width = root.winfo_screenwidth() #gets screen width
screen_height = root.winfo_screenheight() #gets screen height

# Set the window size to the screen size
root.geometry(f"{screen_width}x{screen_height}")

# Song Listbox (for original files)
songList = Listbox(root, bg="white", fg="purple4", width=100, height=5)
songList.pack(pady=10)

# Menubar setup
menubar = Menu(root)
root.config(menu=menubar)

# load audio file
organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label='Select Folder',command=lambda: load_music(root, songList))  # Pass the required arguments
organise_menu.entryconfig("Select Folder", foreground="purple1")
menubar.add_cascade(label='Load Music', menu=organise_menu)

#top frame for info box
button_frame_top = Frame(root)
button_frame_top.pack(pady=10)


info_box = Text(button_frame_top, height=3, width=45, fg="black", font=("Arial", 12))
info_box.pack(side="left", pady=20)

# Insert sample data into the Text widget
file_length = "File Length:"
frequency = "Resonant Frequency:"
difference = "Difference:"

#filler untill we update with graph data
info_box.insert("1.0", file_length + "\n")  # Insert on the first line
info_box.insert("2.0", frequency + "\n")   # Insert on the second line
info_box.insert("3.0", difference + "\n")  # Insert on the third line
#makes read only
info_box.config(state="disabled")
#middle frame for buttons
button_frame_middle = Frame(root)
button_frame_middle.pack(pady=10)


clean_button = Button(button_frame_middle, text="Clean Waveform", command=lambda: clean(songList, root), bg="SpringGreen2", fg="black", width = 15)
clean_button.pack(side="left", padx=10)


waveform_button = Button(button_frame_middle, text="Show Waveform", command=lambda: show_waveform(songList, root),bg="deepskyblue2", fg="black", width = 15)
waveform_button.pack(side="left", padx=10)
                                                     #you will have to put stuff here v
intensity= Button(button_frame_middle, text="Intensity",command=lambda: intensityFunc(  ) ,bg="brown1", fg="black", width = 15)
intensity.pack(side="left", padx=10)
                                                        # you will have to put stuff here v
funkybttn= Button(button_frame_middle, text= "Get funky",command=lambda: funkyButtonFunc(songList, root), bg="dark orchid", fg= "snow", width = 15)
funkybttn.pack(side="left", padx=10)


#bottom frame  for buttons
button_frame_bottom = Frame(root)
button_frame_bottom.pack(pady=10)
                                                        # you will have to put stuff here v
displayRT= Button(button_frame_bottom, text="Display RT60",command=lambda: displayRTFunc(   ),bg="plum3", fg="black", width = 15)
displayRT.pack(side="left", padx=10)
                                                            # you will have to put stuff here v
alternateRT= Button(button_frame_bottom, text="Alternate RT60",command=lambda: combineRTFunc(   ),bg="plum2", fg="black", width = 15)
alternateRT.pack(side="left", padx=10)
                                                        # you will have to put stuff here v
combineRT= Button(button_frame_bottom, text="Combine RT60",command=lambda: combineRTFunc(    ),bg="plum1", fg="black", width = 15)
combineRT.pack(side="left", padx=10)

root.mainloop()

