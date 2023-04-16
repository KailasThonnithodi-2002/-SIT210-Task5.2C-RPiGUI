# new
import RPi.GPIO as GPIO
from tkinter import *

window = Tk() # initialising a window for the GUI
radio_buttons = ["RED", "YELLOW", "GREEN"]  # creating an list of all the radio buttons which will be used in the program
GPIO.setmode(GPIO.BOARD)  # setting up GPIO on the rpi
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)  # red
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)  # yellow
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)  # green

x = IntVar()  # value will be assigned for each radio button in the form of an integer

def radio_button_selection():
    if x.get() == 0:  # red
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(10, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
    elif x.get() == 1:  # yellow
        GPIO.output(8, GPIO.LOW)
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
    elif x.get() == 2:  # green
        GPIO.output(8, GPIO.LOW)
        GPIO.output(10, GPIO.LOW)
        GPIO.output(12, GPIO.HIGH)


# turn off all leds
def clear():
    GPIO.output(8, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    close()

# closing the program using quit button
def close():
    window.quit()

# creating radio buttons for each colour in the list
for i in range(len(radio_buttons)):
    radio_button = Radiobutton(window, text=radio_buttons[i], variable=x, width=10, padx=25, font=("Arial", 20),
                               background=radio_buttons[i], value=i, command=radio_button_selection)
    # inside the window, create 3 radio buttons based on array text, assign with same variable, but different value like a switch
    # the command will execute the certain if statement (from the function radio_button_function)
    radio_button.pack(anchor=W) # anchors, so they are aligned

quit_button = Button(window, text="QUIT", font=("Arial", 20, "bold"), command=clear)
quit_button.pack()
window.mainloop()
