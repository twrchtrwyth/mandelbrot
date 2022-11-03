# Mandelbrot Visualiser

This is a Python program which visualises the Mandelbrot set. The core code is from a Real Python tutorial, and I have used Tkinter to create a GUI to allow easy manipulation of the area observed.

The images are intentionally low resolution, in order to enable the program to run well on my creaky old Thinkpad X220. To generate larger images, just change the SIZE constant. Note that this considerably slows down image generation. I don't know how adjusting the size will affect the Tkinter window.

Images can be saved with the relevant button: these will be saved into a directory named `mandelbrot-images` within the current directory.
