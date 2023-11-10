import tkinter as tk
from math import atan2, degrees, hypot

def convert_rectangular_to_polar(x: float, y: float) -> tuple:
    """
    Converts rectangular coordinates (x, y) to polar coordinates (r, theta).

    Parameters:
    - x: float
        The x-coordinate in the rectangular system.
    - y: float
        The y-coordinate in the rectangular system.

    Returns:
    - tuple:
        A tuple containing the polar coordinates (r, theta), where:
        - r: float
            The distance from the origin to the point (x, y).
        - theta: float
            The angle in degrees between the positive x-axis and the line segment from the origin to the point (x, y).
    """

    # Calculating the distance from the origin to the point (x, y)
    r = hypot(x, y)

    # Calculating the angle in degrees between the positive x-axis and the line segment from the origin to the point (x, y)
    theta = degrees(atan2(y, x))

    return r, theta

def convert_button_click():
    """
    Event handler for the convert button click.

    Retrieves the values from the input fields, calls the conversion function,
    and updates the result label with the converted polar coordinates.
    """

    # Retrieving the values from the input fields
    x = float(x_entry.get())
    y = float(y_entry.get())

    # Calling the conversion function
    polar_coordinates = convert_rectangular_to_polar(x, y)

    # Updating the result label with the converted polar coordinates
    result_label.config(text=f"Polar Coordinates: (r={polar_coordinates[0]}, theta={polar_coordinates[1]}°)")

# Creating the GUI window
window = tk.Tk()
window.title("Rectangular to Polar Converter")

# Creating the input fields for rectangular coordinates
x_label = tk.Label(window, text="x:")
x_label.grid(row=0, column=0)
x_entry = tk.Entry(window)
x_entry.grid(row=0, column=1)

y_label = tk.Label(window, text="y:")
y_label.grid(row=1, column=0)
y_entry = tk.Entry(window)
y_entry.grid(row=1, column=1)

# Creating the convert button
convert_button = tk.Button(window, text="Convert", command=convert_button_click)
convert_button.grid(row=2, column=0, columnspan=2)

# Creating the result label
result_label = tk.Label(window, text="Polar Coordinates: ")
result_label.grid(row=3, column=0, columnspan=2)

# Running the GUI main loop
window.mainloop()
