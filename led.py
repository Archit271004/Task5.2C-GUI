import tkinter as tk
from tkinter import font  # Import the font module
from gpiozero import PWMLED

# Connecting LEDs to GPIO pins with PWM support
blue_led = PWMLED(17)
orange_led = PWMLED(27)
red_led = PWMLED(22)

# Dictionary to keep track of LED PWM controls
led_controls = {
    1: blue_led,
    2: orange_led,
    3: red_led
}

def adjust_led_intensity(led_id, intensity):
    """Adjust the selected LED's intensity based on the slider value."""
    intensity = float(intensity) / 100  # Convert percentage to a 0-1 scale
    led_controls[led_id].value = intensity  # Set PWM duty cycle

def turn_off_all_leds():
    """Turn off all LEDs."""
    for led in led_controls.values():
        led.off()

def exit_app():
    """Cleanup GPIO pins and close the GUI window."""
    turn_off_all_leds()
    win.destroy()

# Create the main window
win = tk.Tk()
win.title("LED Control")

# Define a custom font
custom_font = font.Font(family="Helvetica", size=12, weight="bold")

# Frame for sliders and radio buttons
frame = tk.Frame(win)
frame.pack(padx=100, pady=100)

# Slider creation and placement
sliders = {}    # empty dictionary in which slider widgets will be insterted as key value pairs for future modification to make it easier.
colors = ['light blue', 'orange', 'red']
for idx, (led_id, led) in enumerate(led_controls.items(), start=1):
    # Create a label for each slider
    label = tk.Label(frame, text=f"{['Blue', 'Orange', 'Red'][led_id-1]} LED Intensity:", font=custom_font, bg = colors[led_id - 1]) # dynamically text is choosen because of f-string
    label.grid(row=idx, column=0, pady=5)
    
    # Create a slider for each LED
    slider = tk.Scale(frame, from_=0, to=100, orient='horizontal', command=lambda value, id=led_id: adjust_led_intensity(id, value), bg = colors[led_id - 1])
    slider.grid(row=idx, column=1,padx = 5 ,pady=5)
    sliders[led_id] = slider

# Exit button
exit_button = tk.Button(win, text="Exit", command=exit_app, font=custom_font)
exit_button.pack(pady=10)

# Start the GUI event loop
win.protocol("WM_DELETE_WINDOW", exit_app)
win.mainloop()
