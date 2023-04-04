from tkinter import *


root = Tk()
root.title("Simple Calculator")
root.iconbitmap('C:/Users/danie/OneDrive/Documents/GitHub/calculator/calculator.ico')

frame = LabelFrame(root, padx=10, pady=10, relief="groove", border=3, borderwidth=3)
frame.pack()

display_label = Label(frame, width=15, borderwidth=3)      # will use this to store the first number and the function
display_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

e = Entry(frame, width=30, borderwidth=2, border=2, font="calibri 14", background="light grey")
e.grid(row=1, column=0, columnspan=3, padx=0, pady=4,)

entry_padding = Label(frame)
entry_padding.grid(row=2, column=0, padx=0, pady=5, columnspan=6)

# Creating the get function to get inputs from the buttons.

f_num = ""
function = ""


def button_click(number):
    current = e.get()   # get the num that is already in the box, if there is no num, you get nothing.
    e.delete(0, END)    # Deleting what is already in there, to add the new ones in.
    e.insert(0, str(current) + str(number),)  # Inverting the numbers together /

    # You add this as strings, because you display strings only.

# Create the clear function


def button_clear():
    global display_label
    e.delete(0, END)
    display_label = Label(frame, font="Calibri 14", width=28, borderwidth=0, border=10, )
    display_label.grid(row=0, column=0, columnspan=3, padx=0, pady=0)


# Creating the Plus Button


def button_addition():
    global f_num, function, display_label

    if e.get().isnumeric():
        first_number = e.get()

        function = "addition"
        f_num = int(first_number)
        e.delete(0, END)
        display_label = Label(frame, text=str(f_num) + " +", font="calibri 14", anchor="w", width=28, borderwidth=0,
                              border=10, background="light grey")
        display_label.grid(row=0, column=0, columnspan=3, padx=0, pady=0)
    else:
        e.delete(0, END)


# Creating the = Button
def button_equal():
    global display_label
    second_number = e.get()
    e.delete(0, END)

    if function == "addition":
        e.insert(0, f_num + int(second_number))
        display_label = Label(frame, text=f"{str(f_num)} + {str(second_number)}", font="calibri 14", anchor="w",
                              width=28, borderwidth=0, border=10, background="light grey")
        display_label.grid(row=0, column=0, columnspan=3, padx=0, pady=0)

    elif function == "subtract":
        e.insert(0, f_num - int(second_number))
        display_label = Label(frame, text=f"{str(f_num)} - {str(second_number)}", font="calibri 14", anchor="w",
                              width=28, borderwidth=0, border=10, background="light grey")
        display_label.grid(row=0, column=0, columnspan=3, padx=0, pady=0)
    elif function == "multiply":
        e.insert(0, f_num * int(second_number))
        display_label = Label(frame, text=f"{str(f_num)} * {str(second_number)}", font="calibri 14", anchor="w",
                              width=28, borderwidth=0, border=10, background="light grey")
        display_label.grid(row=0, column=0, columnspan=3, padx=0, pady=0)
    elif function == "divide":
        if int(second_number) != 0:
            result = f_num / int(second_number)
        else:
            result = "Error"
        e.insert(0, result)
        display_label = Label(frame, text=f"{str(f_num)} / {str(second_number)}", font="calibri 14", anchor="w",
                              width=28, borderwidth=0, border=10, background="light grey")
        display_label.grid(row=0, column=0, columnspan=3, padx=0, pady=0)


def button_subtract():
    global display_label, f_num, function
    first_number = e.get()
    function = "subtract"
    f_num = int(first_number)
    e.delete(0, END)
    display_label = Label(frame, text=str(f_num) + " -", font="calibri 14", anchor="w", width=28,
                          borderwidth=0, border=10,
                          background="light grey")
    display_label.grid(row=0, column=0, columnspan=3, padx=0, pady=0)


def button_multiply():
    global display_label, f_num, function
    first_number = e.get()
    function = "multiply"
    f_num = int(first_number)
    e.delete(0, END)
    display_label = Label(frame, text=str(f_num) + " *", font="calibri 14", anchor="w", width=28,
                          borderwidth=0, border=10,
                          background="light grey")
    display_label.grid(row=0, column=0, columnspan=3, padx=0, pady=0)


def button_divide():
    global f_num, function, display_label
    first_number = e.get()
    function = "divide"
    f_num = int(first_number)
    e.delete(0, END)
    display_label = Label(frame, text=str(f_num) + " /", font="calibri 14", anchor="w",
                          width=28, borderwidth=0, border=10,
                          background="light grey")
    display_label.grid(row=0, column=0, columnspan=3, padx=0, pady=0)


# Creating The Buttons.
""" We are using the lambda function, in the Button object, so we can pass attributes to the function we are calling
since calling a function from the Button object, does not allow you to enter any attributes"""


button_1 = Button(frame, text="1", padx=60, pady=30, command=lambda: button_click(1), background="light grey")
button_2 = Button(frame, text="2", padx=60, pady=30, command=lambda: button_click(2), background="light grey")
button_3 = Button(frame, text="3", padx=60, pady=30, command=lambda: button_click(3), background="light grey")
button_4 = Button(frame, text="4", padx=60, pady=30, command=lambda: button_click(4), background="light grey")
button_5 = Button(frame, text="5", padx=60, pady=30, command=lambda: button_click(5), background="light grey")
button_6 = Button(frame, text="6", padx=60, pady=30, command=lambda: button_click(6), background="light grey")
button_7 = Button(frame, text="7", padx=60, pady=30, command=lambda: button_click(7), background="light grey")
button_8 = Button(frame, text="8", padx=60, pady=30, command=lambda: button_click(8), background="light grey")
button_9 = Button(frame, text="9", padx=60, pady=30, command=lambda: button_click(9), background="light grey")
button_0 = Button(frame, text="0", padx=60, pady=30, command=lambda: button_click(0), background="light grey")

button_plus = Button(frame, text="+", padx=59, pady=29, command=button_addition, background="light grey")
button_equal = Button(frame, text="=", padx=127, pady=29, command=button_equal, background="light grey", cursor="hand2")
button_clear = Button(frame, text="Clear", padx=119, pady=29, command=button_clear, background="light grey")

button_subtract = Button(frame, text="-", padx=60, pady=30, command=button_subtract, background="light grey")
button_multiply = Button(frame, text="*", padx=60, pady=30, command=button_multiply, background="light grey")
button_divide = Button(frame, text="/", padx=60, pady=30, command=button_divide, background="light grey")

# Displaying them on the screen
button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)
button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=6, column=0)
button_plus.grid(row=7, column=0)
button_equal.grid(row=7, column=1, columnspan=2)
button_clear.grid(row=6, column=1, columnspan=2)

button_subtract.grid(row=8, column=0)
button_multiply.grid(row=8, column=1)
button_divide.grid(row=8, column=2)


# Binding Button Functions With Actual Keys
def button_equal_key(_):
    global display_label
    second_number = e.get()
    e.delete(0, END)

    if function == "addition":
        e.insert(0, f_num + int(second_number))
        display_label = Label(frame, text=f"{str(f_num)} + {str(second_number)}", font="calibri 14", anchor="w",
                              width=28, borderwidth=0, border=10, background="light grey")
        display_label.grid(row=0, column=0, columnspan=3, padx=0, pady=0)

    elif function == "subtract":
        e.insert(0, f_num - int(second_number))
        display_label = Label(frame, text=f"{str(f_num)} - {str(second_number)}", font="calibri 14", anchor="w",
                              width=28, borderwidth=0, border=10, background="light grey")
        display_label.grid(row=0, column=0, columnspan=3, padx=0, pady=0)
    elif function == "multiply":
        e.insert(0, f_num * int(second_number))
        display_label = Label(frame, text=f"{str(f_num)} * {str(second_number)}", font="calibri 14", anchor="w",
                              width=28, borderwidth=0, border=10, background="light grey")
        display_label.grid(row=0, column=0, columnspan=3, padx=0, pady=0)
    elif function == "divide":
        if int(second_number) != 0:
            e.insert(0, f_num / int(second_number))
            display_label = Label(frame, text=f"{str(f_num)} / {str(second_number)}", font="calibri 14", anchor="w",
                                  width=28, borderwidth=0, border=10, background="light grey")
            display_label.grid(row=0, column=0, columnspan=3, padx=0, pady=0)
        else:
            display_label = Label(frame, text=f"Error", font="calibri 14", anchor="w",
                                  width=28, borderwidth=0, border=10, background="light grey")
            display_label.grid(row=0, column=0, columnspan=3, padx=0, pady=0)


def button_subtract_key(_):
    global display_label, f_num, function
    first_number = e.get()
    function = "subtract"
    f_num = int(first_number)
    e.delete(0, END)
    display_label = Label(frame, text=str(f_num) + " -", font="calibri 14", anchor="w", width=28, borderwidth=0,
                          border=10,
                          background="light grey")
    display_label.grid(row=0, column=0, columnspan=3, padx=0, pady=0)


def button_multiply_key(_):
    global display_label, f_num, function
    first_number = e.get()
    function = "multiply"
    f_num = int(first_number)
    e.delete(0, END)
    display_label = Label(frame, text=str(f_num) + " *", font="calibri 14", anchor="w", width=28, borderwidth=0,
                          border=10,
                          background="light grey")
    display_label.grid(row=0, column=0, columnspan=3, padx=0, pady=0)


def button_divide_key(_):
    global f_num, function, display_label
    first_number = e.get()
    function = "divide"
    f_num = int(first_number)
    e.delete(0, END)
    display_label = Label(frame, text=str(f_num) + " /", font="calibri 14", anchor="w", width=28, borderwidth=0,
                          border=10,
                          background="light grey")
    display_label.grid(row=0, column=0, columnspan=3, padx=0, pady=0)


def button_addition_key(_):
    global f_num, function, display_label
    first_number = e.get()
    function = "addition"
    f_num = int(first_number)
    e.delete(0, END)
    display_label = Label(frame, text=str(f_num) + " +", font="calibri 14", anchor="w",
                          width=28, borderwidth=0, border=10, background="light grey")
    display_label.grid(row=0, column=0, columnspan=3, padx=0, pady=0)


def button_click_key(number):  # Binding (n) as an event to add it to entry
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + number.char)


# Creating delete function
def deleting_key(_):
    current = e.get()  # Get what u have writen in string
    e.delete(0, END)
    current_list = list(current)
    current_list.pop()
    inserting = ""

    for j in range(len(current_list)):
        inserting += current_list[j]

    e.insert(0, inserting)


root.bind('<BackSpace>', deleting_key)
root.bind('+', button_addition_key)
root.bind('-', button_subtract_key)
root.bind('*', button_multiply_key)
root.bind('/', button_divide_key)
root.bind('<Return>', button_equal_key)
for i in range(10):
    root.bind(str(i), button_click_key)

root.mainloop()

