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
    output_label.config(text=f"\nCurrent Output:\n {user_output}", font=custom_font)
    handle_new_history(user_input, user_output)
    entry.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("Digit Converter")

# Set the window size to 400x300 pixels
root.geometry("1000x500")

# Define a font
custom_font = ("Helvetica", 15, "bold")


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

#===================================== History log =====================================

# List to store output items 
history_list = []

history_label = tk.Label(root, text="\nHistory: ")
history_label.pack()

# Create a Text widget to display the output
history_text = tk.Text(root, height=10, width=60)
history_text.pack()

# Function to update the output Text widget
def update_history(new_history):
    # Append new output to the existing content of the Text widget
    history_text.insert(tk.END, f"{new_history}\n")
    # Scroll to the end of the Text widget to show the latest output
    history_text.see(tk.END)

# Function to handle new output
def handle_new_history(user_input, current_output):
    # Generate new output
    new_history = f"{len(history_list) + 1}. {user_input} = {current_output}"
    # Append new output to the output list
    history_list.append(new_history)
    # Update the output Text widget with the new output
    update_history(new_history)

# Start the main loop
root.mainloop()