import tkinter as tk

def button_click():
    label.config(text="Button clicked!")

# Create the main application window
root = tk.Tk()
root.title("Tkinter Example")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(padx=20, pady=20)

# Create a button widget
button = tk.Button(root, text="Click me!", command=button_click)
button.pack()

# Start the main event loop
root.mainloop()
