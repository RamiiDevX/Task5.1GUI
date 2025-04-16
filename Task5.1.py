import tkinter as tk
import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO pins for LEDs
RED_LED = 17
GREEN_LED = 27
BLUE_LED = 22

# Set up LED pins as outputs
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(BLUE_LED, GPIO.OUT) 

# Turn off all LEDs initially
def reset_leds():
    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(GREEN_LED, GPIO.LOW)
    GPIO.output(BLUE_LED, GPIO.LOW)

reset_leds()

# Create the main window
root = tk.Tk()
root.title("LED Control")
root.geometry("300x200")

# Variable to track selected LED
selected_led = tk.StringVar()
selected_led.set("none")

# Function to handle LED selection
def on_led_select():
    reset_leds()
    selection = selected_led.get()
    
    if selection == "red":
        GPIO.output(RED_LED, GPIO.HIGH)
    elif selection == "green":
        GPIO.output(GREEN_LED, GPIO.HIGH)
    elif selection == "blue":
        GPIO.output(BLUE_LED, GPIO.HIGH)

# Create radio buttons
tk.Label(root, text="Select LED to turn on:").pack(pady=10)

tk.Radiobutton(root, text="Red LED", variable=selected_led,
               value="red", command=on_led_select).pack(anchor=tk.W, padx=20)
tk.Radiobutton(root, text="Green LED", variable=selected_led,
               value="green", command=on_led_select).pack(anchor=tk.W, padx=20)
tk.Radiobutton(root, text="Blue LED", variable=selected_led,
               value="blue", command=on_led_select).pack(anchor=tk.W, padx=20)

# Exit button
def on_exit():
    reset_leds()
    GPIO.cleanup()
    root.destroy()

tk.Button(root, text="Exit", command=on_exit).pack(pady=20)

# Start the main loop
root.mainloop()
