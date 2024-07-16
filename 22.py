#Write a GUI program that displays your details when a button is clicked
#error hai
#raise RuntimeError(f"Too early to {what}: no default root window")
#RuntimeError: Too early to run the main loop: no default root window

import tkinter


class Details:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create frame on window
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)

        # Create the widgets for the top frame.
        self.name_label = tkinter.Label(self.frame1, text='Name ')
        self.name_entry = tkinter.Entry(self.frame1, width=20)

        self.addr_label = tkinter.Label(self.frame2, text='address ')
        self.addr_entry = tkinter.Entry(self.frame2, width=20)

        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')
        self.addr_label.pack(side='left')
        self.addr_entry.pack(side='left')

        self.name1_label = tkinter.Label(self.frame4, text='Name ')
        self.value1 = tkinter.StringVar()
        self.name2_label = tkinter.Label(self.frame4,
                                         textvariable=self.value1)
        self.addr1_label = tkinter.Label(self.frame5, text='Address ')
        self.value2 = tkinter.StringVar()
        self.addr2_label = tkinter.Label(self.frame5,
                                         textvariable=self.value2)

        self.name1_label.pack(side='left')
        self.name2_label.pack(side='left')
        self.addr1_label.pack(side='left')
        self.addr2_label.pack(side='left')

        # Create the button
        self.show_button = tkinter.Button(self.frame3, text='Display',
                                          command=self.display)
        self.quit_button = tkinter.Button(self.frame3, text='Quit',
                                          command=self.main_window.destroy)
        # Pack the buttons.
        self.show_button.pack(side='left')
        self.quit_button.pack(side='left')



# Pack the frames.

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

# Enter the tkinter main loop.
tkinter.mainloop()


# Convert temperature from Celsius to Fahrenheit
def display(self):
    self.value1.set(self.name_entry.get())


self.value2.set(self.addr_entry.get())
# Create an instance of the MyGUI class.
obj = Details()