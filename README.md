# Mandelbrot Visualiser

This is a Python program which visualises the Mandelbrot set. The core code is lightly modified from a Real Python tutorial, and I have used Tkinter to create a GUI to allow easy manipulation of the area observed.

I have made `main.py` executable, but it doesn't need to be in order to work. If you're worried that I'm up to no good, and assuming this executable permission carries over to other machines, you can revoke executable permissions with `chmod -x path/to/main.py` and just run the program using the usual `python path/to/main.py` command.

The images are intentionally low resolution, in order to enable the program to run well on my creaky old Thinkpad X220. To generate larger images, just change the `SIZE` constant. Note that this considerably slows down image generation. I don't know how adjusting the size will affect the Tkinter window.

Images can be saved with the relevant button: these will be saved into a directory named `mandelbrot-images` in the same directory as `main.py`.

If you have stumbled across this, feel free to clone the repo and do whatever you like with it, I don't mind. Any feedback gratefully appreciated.
