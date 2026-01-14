import tkinter as tk
import threading
import time

# Create window
root = tk.Tk()
root.title("Virtual LED Simulator")
root.geometry("300x350")
root.configure(bg="white")

# LED state
led_on = False
stop_pattern = False

# Canvas for LED
canvas = tk.Canvas(root, width=200, height=200, bg="white", highlightthickness=0)
canvas.pack(pady=20)

# Draw LED (circle)
led = canvas.create_oval(50, 50, 150, 150, fill="gray", outline="black")

# Functions
def led_on_func():
    global led_on
    led_on = True
    canvas.itemconfig(led, fill="red")

def led_off_func():
    global led_on
    led_on = False
    canvas.itemconfig(led, fill="gray")

def blink():
    global stop_pattern
    stop_pattern = False
    while not stop_pattern:
        canvas.itemconfig(led, fill="red")
        time.sleep(0.5)
        canvas.itemconfig(led, fill="gray")
        time.sleep(0.5)

def start_blink():
    threading.Thread(target=blink, daemon=True).start()

def stop():
    global stop_pattern
    stop_pattern = True
    led_off_func()

# Buttons
btn_on = tk.Button(root, text="LED ON", command=led_on_func, bg="green", fg="white", width=15)
btn_on.pack(pady=5)

btn_off = tk.Button(root, text="LED OFF", command=led_off_func, bg="red", fg="white", width=15)
btn_off.pack(pady=5)

btn_blink = tk.Button(root, text="BLINK", command=start_blink, bg="orange", width=15)
btn_blink.pack(pady=5)

btn_stop = tk.Button(root, text="STOP", command=stop, bg="black", fg="white", width=15)
btn_stop.pack(pady=5)

root.mainloop()
