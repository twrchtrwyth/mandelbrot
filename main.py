#!/usr/bin/env python3
import os
import matplotlib.cm
import tkinter as tk
from PIL import Image, ImageTk
from mandelbrot import Mandelbrot
from viewport import Viewport

SIZE = 256

def paint(mandelbrot_set, viewport, palette, smooth):
    for pixel in viewport:
        stability = mandelbrot_set.stability(complex(pixel), smooth)
        index = int(min(stability * len(palette), len(palette) - 1))
        pixel.color = palette[index % len(palette)]

def denormalize(palette):
    return [
        tuple(int(channel * 255) for channel in color)
        for color in palette
    ]

def generate_set():
    """Update the area of the set that is shown in the window."""
    max_iterations = int(entry_iterations.get())
    escape_radius= float(entry_escape.get())
    center = complex(entry_centre.get().replace(" ", ""))
    width = float(entry_width.get())
    mandelbrot_set = Mandelbrot(
        max_iterations=max_iterations, escape_radius=escape_radius
    )
    image = Image.new(mode="RGB", size=(SIZE, SIZE))
    viewport = Viewport(image, center=center, width=width)
    paint(mandelbrot_set, viewport, palette, smooth=True)
    # First assignment also required to prevent image being garbage collected.
    window.tk_image = tk_image = ImageTk.PhotoImage(image)
    canvas_image = canvas.create_image(0, 0, anchor="nw", image=tk_image)
    canvas.itemconfig(canvas_image, image=tk_image)
    return image

def clear_input():
    """Clear all text from the entry boxes."""
    entry_iterations.delete(0, tk.END)
    entry_escape.delete(0, tk.END)
    entry_centre.delete(0, tk.END)
    entry_width.delete(0, tk.END)

def show_spiral():
    """Zoom to a beautiful spiral."""
    misiurewicz_point = "-0.7435 + 0.1314j"
    clear_input()
    entry_iterations.insert(0, "128")
    entry_escape.insert(0, "1000")
    entry_centre.insert(0, misiurewicz_point)
    entry_width.insert(0, "0.002")
    generate_set()

def reset():
    """Show the whole Mandelbrot set."""
    clear_input()
    entry_iterations.insert(0, 20)
    entry_escape.insert(0, 1000)
    entry_centre.insert(0, -0.75)
    entry_width.insert(0, 3)
    generate_set()

def save():
    """Save the image with a filename corresponding to the parameters of the
    generated image.
    May misname the image if the inputs have been altered without generating a
    new image, but this will probably happen rarely and it's not worth the time
    for me to implement a fix for this.
    """
    mi = int(entry_iterations.get())
    er = float(entry_escape.get())
    c = complex(entry_centre.get().replace(" ", ""))
    w = float(entry_width.get())
    image = generate_set()

    directory = os.getcwd()
    os.makedirs("mandelbrot-images", exist_ok=True)
    save_directory = f"{directory}/mandelbrot-images/mandelbrot_{mi}_{er}_{c}_{w}.png"
    image.save(save_directory)
    print(f"Image saved to {save_directory}")

colormap = matplotlib.cm.get_cmap("viridis").colors
palette = denormalize(colormap)

##########################
# Tkinter configuration. #
##########################

window = tk.Tk()
window.title("Mandelbrot Set")
window.resizable(width=False, height=False)

# Create the frame to hold the image.
frame_image = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frame_image.grid(row=0, rowspan=3, column=0)

# Load the image into Tkinter.
canvas = tk.Canvas(master=frame_image, width=SIZE, height=SIZE, bg="white")
canvas.pack()

# Create a frame for user input.
frame_input = tk.Frame(master=window)
frame_input.grid(row=0, column=1, columnspan=2)

# Create the input fields.
entry_labels = [
    "Max. Iterations",
    "Escape Radius",
    "Centre",
    "Width"
]
for i, label in enumerate(entry_labels):
    label = tk.Label(master=frame_input, text=label)
    label.grid(row=i, column=0, sticky="e")

entry_iterations = tk.Entry(master=frame_input, width=10)
entry_iterations.grid(row=0, column=1, padx=5, pady=5)

entry_escape = tk.Entry(master=frame_input, width=10)
entry_escape.grid(row=1, column=1, padx=5, pady=5)

entry_centre = tk.Entry(master=frame_input, width=10)
entry_centre.grid(row=2, column=1, padx=5, pady=5)

entry_width = tk.Entry(master=frame_input, width=10)
entry_width.grid(row=3, column=1, padx=5, pady=5)

frame_generate = tk.Frame(master=window, relief=tk.RAISED, borderwidth=2)
frame_generate.grid(row=1, column=1)
button_generate = tk.Button(
    master=frame_generate,
    text="Generate",
    command=generate_set
)
button_generate.pack()

frame_spiral = tk.Frame(master=window, relief=tk.RAISED, borderwidth=2)
frame_spiral.grid(row=1, column=2)
button_spiral = tk.Button(
    master=frame_spiral,
    text="Spiral",
    command=show_spiral
)
button_spiral.pack()

frame_reset = tk.Frame(master=window, relief=tk.RAISED, borderwidth=2)
frame_reset.grid(row=2, column=1)
button_reset = tk.Button(
    master=frame_reset,
    bg="#990000",
    fg="white",
    text="Reset",
    command=reset
)
button_reset.pack()

frame_save = tk.Frame(master=window, relief=tk.RAISED, borderwidth=2)
frame_save.grid(row=2, column=2)
button_save = tk.Button(
    master=frame_save,
    bg="#a3be8c",
    fg="black",
    text="Save",
    command=save
)
button_save.pack()

reset()
window.mainloop()
