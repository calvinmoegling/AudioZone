Audio Analysis Tool
Overview
This Python project is a comprehensive audio analysis tool that processes audio files to visualize and analyze their 
properties.

The application uses the following libraries:

pydub: For handling audio file conversion.
numpy: For numerical computations.
matplotlib: For creating visualizations.
tkinter: For the graphical user interface (GUI).
scipy: for the rt60 stuff
Requirements
Libraries
Ensure the following Python libraries are installed:

pydub
numpy
matplotlib
tkinter
scipy

External Tools
FFmpeg: Required by pydub for handling audio file conversions. Follow [FFmpeg Installation Guide to install it.](https://www.youtube.com/watch?v=JR36oH35Fgg)



Running instructions,

must run from the main, once the program is loaded find the load music button in the top left of the screen
from there you can load in any file but preferably a mp3 or wav file. 

after loaded it, it is converted to a wav
click on the song in the list box, and click the clean button, this removes the 
metadata as well as takes it down to a mono channel audio.

from there you can click on any of the buttons but preferably click on the show waveform button first.

reminder - you must click on the song in the listbox for anything to work, otherwise it will pop up an error saying no 
song selected. 
