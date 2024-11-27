#functions

import os
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pydub import AudioSegment
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


# Global variables to hold song data
songs = []
current_canvas = None


def load_music(root, songList):
    file_path = filedialog.askopenfilename(
        filetypes=[("Audio Files", "*.mp3;*.wav;*.flac;*.aac;*.ogg;*.m4a;*.wma"),
                  ("All Files", "*.*")]
    )  # Open dialog to select a file

    if not file_path:
        return

    # Extract filename and extension
    name, ext = os.path.splitext(os.path.basename(file_path))  # split the file name and extension
    directory = os.path.dirname(file_path)  # Get the directory of the file

    # If the file is not .wav, convert it
    if ext.lower() != '.wav':
        converted_song = convert_to_wav(file_path, directory)
        if converted_song:
            songList.insert("end", converted_song)  # Insert converted file into the list
        else:
            messagebox.showerror("Error", "Failed to convert the file to .wav format")
    else:
        # If it's already a .wav, add it directly
        songList.insert("end", file_path )






def convert_to_wav(song, directory):
    name, ext = os.path.splitext(song)

    audio_path = os.path.join(directory, song)
    output_path = os.path.join(directory, f"{name}.wav")

    if ext.lower() == '.wav':  # Skip if the file is already .wav
        return f"{name}.wav"
    else:
        try:
            audio = AudioSegment.from_file(audio_path, format=ext[1:])
            audio.export(output_path, format="wav")  # Convert to .wav
            print(f"Converted {song} to {name}.wav")
            return f"{name}.wav" #returns converted file

        except Exception as e:
            print(f"Error converting {song}: {e}")
            return None


def show_waveform(songList, root):
    global current_canvas  # Refer to the global canvas variable

    if songList.size() == 0:
        messagebox.showerror("Error", "No songs loaded!")  #if there is no song loaded and button is pressed it throws this error
        return

    try:
        # Get the currently selected song (full path)
        selected_song = songList.get(songList.curselection())
        if not selected_song:
            messagebox.showerror("Error", "No song selected!")
            return

        # Check if the file exists
        if not os.path.exists(selected_song):
            messagebox.showerror("Error", f"Audio file '{selected_song}' not found!")
            return

        # Remove the previous canvas if it exists
        if current_canvas:
            current_canvas.get_tk_widget().destroy()  # Remove the previous canvas from the window

        # Load the audio file
        audio = AudioSegment.from_wav(selected_song)

        # Convert the audio to an array of samples
        samples = np.array(audio.get_array_of_samples())
        sample_rate = audio.frame_rate

        # Generate the time axis for the waveform
        duration = len(samples) / sample_rate
        time = np.linspace(0, duration, num=len(samples))

        # Create a matplotlib figure and axis
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(time, samples, color='purple')
        ax.set_title(f"Waveform of {selected_song}")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")

        # Embed the figure into Tkinter window
        current_canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
        current_canvas.draw()

        # Place the canvas in the Tkinter window (inside a frame or pack it directly)
        current_canvas.get_tk_widget().pack(pady=20)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def clean(songList, root):
    try:
        #check if a song is loaded
        if songList.size() == 0:
            messagebox.showerror("Error", "No songs loaded!") #if no song loaded it throws this error
            return

        #checks if song is selected
        selected = songList.get(songList.curselection())
        if not selected:
            messagebox.showerror("Error", "No song selected!") # if not throws this error
            return

        #gets the selected file
        audio = AudioSegment.from_wav(selected)

        #if it has more than 1 channel, remove them and make it one channel
        if audio.channels > 1:
            audio = audio.set_channels(1)

        #allows us to access the cleaned file
        directory = os.path.dirname(selected)
        filename = os.path.basename(selected)
        cleaned_file_name = f"cleaned_{filename}"
        cleaned_file_path = os.path.join(directory, cleaned_file_name)

        # removes meta data
        audio.export(cleaned_file_path, format="wav", tags=None)

        #removes old non-cleaned song from listbox and inserts the new one
        selected_index = songList.curselection()[0]  # Get the index of the selected song
        songList.delete(selected_index) #deletes it
        songList.insert("end", cleaned_file_path) #adds in the cleaned one

        #shows that it cleaned it
        messagebox.showinfo("Success", "Waveform cleaned!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to clean audio: {str(e)}")


def update_len_freq_diff():
    #this function will update the text in the box that contains frequency, length and difference
    #you will do this by calculating all 3 and inserting the text when ever the button is pressed
    #when it is pressed you will also delete the current text that was in there, and put the new text in
    pass

def displayRTFunc():
    #deletes the current_canvas
    #displays the RT graph
    pass
def alternateRTFunc():
    # deletes the current_canvas
    # cycles through the 3 RT graphs every time it is pressed
    # each a diff color
    pass
def combineRTFunc():
    # deletes the current_canvas
    # combines the 3 RT graphs into one, each a diff color
    pass
def intensityFunc():
    # deletes the current_canvas
    # displays an intensity graph like shown in the video
    pass
def funkyButtonFunc(songList, root):
    #gets funky - this is the "add button and additional visual output for useful data (your choice)"
    #delete the current_canvas and replaces it with the funky one IDK change this name later
    global current_canvas

    if songList.size() == 0:
        messagebox.showerror("Error", "No songs loaded!")
        return

    try:
        # Get selected song
        selected_song = songList.get(songList.curselection())
        if not selected_song:
            messagebox.showerror("Error", "No song selected!")
            return

        # Load audio
        audio = AudioSegment.from_wav(selected_song)
        samples = np.array(audio.get_array_of_samples())
        sample_rate = audio.frame_rate

        # Generate time array
        duration = len(samples) / sample_rate
        time = np.linspace(0, duration, num=len(samples))

        # Create color gradients for the waveform
        points = np.array([time, samples]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)

        # Normalize the amplitude for better visuals
        norm = plt.Normalize(samples.min(), samples.max())
        cmap = plt.get_cmap("rainbow")  # Use a fun colormap!

        # Create a colorful LineCollection
        lc = LineCollection(segments, cmap=cmap, norm=norm)
        lc.set_array(samples)  # Use the amplitude to set the colors
        lc.set_linewidth(1.5)

        # Plot the waveform
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.add_collection(lc)
        ax.set_xlim(time.min(), time.max())
        ax.set_ylim(samples.min(), samples.max())
        ax.set_title("Funky Colors!")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")

        # Remove the previous canvas
        if current_canvas:
            current_canvas.get_tk_widget().destroy()

        # Embed the plot into Tkinter
        current_canvas = FigureCanvasTkAgg(fig, master=root)
        current_canvas.draw()
        current_canvas.get_tk_widget().pack(pady=20)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    pass
