import tkinter as tk
import math

MAX_LENGTH = 20   # prevent extremely long numbers


# Add value to screen
def click(value):
    current = entry.get()

    if current == "Error":
        clear()
        current = ""

    # Prevent overly long input
    if len(current) > MAX_LENGTH:
        return

    # Handle decimal point properly
    if value == ".":
        # Find last operator position
        operators = ['+', '-', '*', '/']
        last_operator_index = -1

        for op in operators:
            index = current.rfind(op)
            if index > last_operator_index:
                last_operator_index = index

        current_number = current[last_operator_index + 1:]

        # Prevent multiple decimals in same number
        if "." in current_number:
            return

        # If number is empty or operator just pressed, start with 0.
        if current_number == "":
            value = "0."

    if current == "0" and value not in ['+', '-', '*', '/']:
        entry.delete(0, tk.END)
        entry.insert(0, str(value))
    else:
        entry.insert(tk.END, str(value))

# Clear screen
def clear():
    entry.delete(0, tk.END)
    entry.insert(0, "0")


# Perform calculation
def calculate():
    try:
        expression = entry.get()

        # Replace symbols (optional safety formatting)
        expression = expression.replace("×", "*").replace("÷", "/")

        result = eval(expression)

        # Handle extremely large numbers
        if abs(result) > 1e100:
            raise OverflowError

        # Remove unnecessary .0
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        entry.delete(0, tk.END)
        entry.insert(0, str(result))

    except ZeroDivisionError:
        show_error()
    except OverflowError:
        show_error()
    except:
        show_error()


def show_error():
    entry.delete(0, tk.END)
    entry.insert(0, "Error")


# Create window
window = tk.Tk()
window.title("Advanced Calculator")
window.geometry("300x400")
window.resizable(False, False)

# Display
entry = tk.Entry(window, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)
entry.insert(0, "0")

# Buttons layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '.', '+'],
    ['=']
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


window.mainloop()
