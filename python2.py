import tkinter as tk
from tkinter import ttk



class Window(tk.Tk):
    def __init__(self):
        super().__init__()

    # configure the root window
        self.title('My Window')
        self.geometry('300x300')

    # label
        self.label = ttk.Label(self, text='Enter your Name')
        self.label.grid(row=0,column=0,padx=10,pady=10)
    
    # entry
    
        self.entry1=ttk.Entry(self)
        self.entry1.grid(row=0,column=1,padx=10,pady=10)

    # button
    
        self.button = ttk.Button(self, text='Click Me',command=self.click)
    
        self.button.grid(row=2,column=0, columnspan=2,padx=10,pady=10)
    
    
    # label2
    
        self.label2 = ttk.Label(self)
        self.label2.grid(row=3,column=0,padx=50,pady=10)
    

    def click(self):
        name=self.entry1.get()
        self.label2.configure(text='Good Morning ' + name,background='red',font=('Arial',20))
      
if __name__ == "__main__":
    win = Window()
    win.mainloop()
