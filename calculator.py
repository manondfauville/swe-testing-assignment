import tkinter as tk

# Function to update the display
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to calculate result
def calculate():
    expression = entry.get()
    result = eval(expression)   # No error handling as requested
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

# Function to clear display
def clear():
    entry.delete(0, tk.END)
    entry.insert(0, "0")

# Create window
window = tk.Tk()
window.title("Basic Calculator")
window.geometry("300x400")

# Display field
entry = tk.Entry(window, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Buttons layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Create buttons
for row in buttons:
    frame = tk.Frame(window)
    frame.pack(expand=True, fill="both")
    for btn in row:
        button = tk.Button(frame, text=btn, font=("Arial", 18))
        button.pack(side="left", expand=True, fill="both")
        
        if btn == "=":
            button.config(command=calculate)
        elif btn == "C":
            button.config(command=clear)
        else:
            button.config(command=lambda b=btn: click(b))

# Start the GUI loop
window.mainloop()