import tkinter as tk

# Create window
window = tk.Tk()
window.title("Hello GUI")
window.geometry("300x200")

# Add label
label = tk.Label(window, text="Hello!", font=("Arial", 16))
label.pack(pady=20)

# Button
def on_click():
    label.config(text="You clicked the button!")

button = tk.Button(window, text="Click me", command=on_click)
button.pack()

# Run loop
window.mainloop()
