import sys
import tkinter as tk


# Calculator app with GUI that allows user to add/multiply/divide,etc. I will add more in depth functionality in the future.
#Working on getting a working GUI, then I will add more complex features, like calc functions and such
# Corey Prince, 2026

#FIXME: Get the functions working with a menu that has clickable buttons and such,then move towards making the GUI look pretty
#
# function that adds the numbers a and b, will let users enter their own numbers to multiply
def add(a, b):
    return a + b

# function that subtracts the numbers and b, will let users enter own number to subtract
def subtract(a, b):
    return a - b

# same deal for multiplication
def multiply(a, b):
    return a * b

# division function with exception logic for catching if a user tries to divide by zero.
def divide(a, b):
    if b == 0:
        raise RuntimeError("Math error: Attempted to divide by Zero\n")
    return a // b


#FIXME: Add advanced calculus functionality, and eventually add binary number math.

#FIXME: Implement definite integrals

#FIXME: Implement indefinite integrals


def menu():
    # FIXME: Get the menu to work with a switch statement as opposed to this rudementary starting format
    print("Welcome to the calculator app!")
    print("Please choose from the available options:")
    print("1: Add:")
    print("2: Subtract")
    print("3: Multiply:")
    print("4: Divide")
    print("5: Exit")


def main():

    print("Welcome to the calculator app!")

    # ask user to enter number for the add, incorporate into menu later
    num1 = 0
    num2 = 0
    result = 0
    choice = 0

    while True:
        # clearing the input buffer after reading choice
        menu()

        try:
            choice = int(input())
        except ValueError:
            choice = 0

        # asking for numbers if the user has performed an operation
        if 1 <= choice <= 4:
            try:
                print("Enter first number: ")
                num1 = int(input())
            except ValueError:
                num1 = 0

            try:
                print("Enter second number: ")
                num2 = int(input())
            except ValueError:
                num2 = 0

        elif choice == 5:
            print("Exiting Program...")
            return

        # switch statement for adding the choices
        match choice:
            case 1:
                result = add(num1, num2)
                print("Result", result)

            case 2:
                result = subtract(num1, num2)
                print("Subtracted Result :", result)

            case 3:
                result = multiply(num1, num2)
                print("Multiplied Result :", result)

            case 4:
                # try the division operation and catch the exception if user tries to divide by zero
                try:
                    result = divide(num1, num2)
                    print("Divided Result", result)
                except RuntimeError as e:
                    print("Exception occurred", e)

            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    # Create main window for the GUI




    root = tk.Tk()
    root.configure(background="#d9d9d9")

    #set the size and on screen offset for the window


    # Set the window  title
    root.title("Calculator")
    root.geometry("260x360+500+160")

    display = tk.StringVar()
    display.set("")














    # Creating the calculator display widget


    #Setting Button Labels

    button_label = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+','C'
    ]
    #Sets the entry widget for the screen,sets it above the numbers

    calc_screen = tk.Entry(root, textvariable = display,font = ('Arial', 20), justify = 'right',bd = 5)
    calc_screen.grid(row = 0, column=0, columnspan = 4, ipadx = 8, ipady = 15, pady = 10)


    # function to handle clicking and entering into the calculator itself
    def button_clicked(num):
        if num == 'C':
            calc_screen.delete(0, tk.END)
        elif num == '=':
            try:
                result = eval(calc_screen.get())
                calc_screen.delete(0,tk.END)
                calc_screen.insert(tk.END,str(result))
            except Exception:
                calc_screen.delete(0,tk.END)
                calc_screen.insert(tk.END,"Error")
        else:
            calc_screen.insert(tk.END, num)

    #Creating and arranging e buttons into a grid
    row_val = 1
    col_val = 0
    #setting the labels for the calculator



    for label in button_label:
        #Create the buttons using the lambda l=label to capture the current label for each button
        tk.Button(root, text = label, padx = 20, pady= 20, command = lambda l = label: button_clicked(l)).grid(row = row_val, column = col_val)

        col_val+=1
        if col_val > 3:
            col_val = 0
            row_val +=1


    # Set the main loop for the menu
    root.mainloop()
