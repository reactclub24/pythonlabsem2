#Write a GUI program that convert temperature from Celsius to Fahrenheit
#error ara hai
# command=self.convert)
            ^^^^^^^^^^^^
#AttributeError: 'CConverttoF' object has no attribute 'convert'

import tkinter


class CConverttoF:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create frame on window
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create the widgets for the top frame.
        self.prompt_label = tkinter.Label(self.top_frame,
                                          text='Enter temparature in Celsius ')
        self.celsius_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side='left')
        self.celsius_entry.pack(side='left')

        self.descr_label = tkinter.Label(self.mid_frame,
                                         text='Converted to Fahrenheit ')
        self.value = tkinter.StringVar()
        self.fahrenheit_label = tkinter.Label(self.mid_frame,
                                              textvariable=self.value)
        self.descr_label.pack(side='left')
        self.fahrenheit_label.pack(side='left')

        # Create the button
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Convert',
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        # Pack the buttons.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()



# Convert temperature from Celsius to Fahrenheit
def convert(self):
    self.C = float(self.celsius_entry.get())


    self.F = 9 / 5 * (self.C) + 32
    self.value.set(self.F)
# Create an instance of the CConverttoF class.
obj = CConverttoF()