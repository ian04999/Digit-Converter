import tkinter as tk
from num_language import gui_version

# Function to handle Enter key press event
def on_enter_pressed(event):
    # Simulate button click event
    button.invoke()
    
# Define a function to handle button clicks
def on_button_click():
    # Get the input from the entry widget
    user_input = entry.get()
    user_output = gui_version(user_input)
        
    # Update the label with the input
    output_label.config(text=f"\nOutput:\n {user_output}", font=custom_font)

# Create the main application window
root = tk.Tk()
root.title("Digit Converter")

# Set the window size to 400x300 pixels
root.geometry("1000x300")

# Define a font
custom_font = ("Helvetica", 20, "bold")

# Create a label for instructions
instruction_label = tk.Label(root, text="Enter an integer: ")
instruction_label.pack()

# Create an entry widget (user input bar)
entry = tk.Entry(root)
entry.pack(padx=30, pady=20)

# Create a button that triggers the on_button_click function
button = tk.Button(root, text="Convert", command=on_button_click)
button.pack()

# Bind the Enter key press event to the button
root.bind("<Return>", on_enter_pressed)


# Create a label to display the output
output_label = tk.Label(root, text="\nIn English: ")
output_label.pack()

# Start the main loop
root.mainloop()