import tkinter as tk
from logic import Logic

class Calc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('550x700')
        self.title('provaaaaaaaaaa')
        # self.stream = tk.StringVar(self, value='')
        self.logic = Logic(self)
        self.grid_rowconfigure([0,1,2,3,4], weight=1)
        self.grid_rowconfigure(5, weight=10)
        self.grid_columnconfigure([0,1,2,3,4], weight=1)
        self.create_gui()



    def create_gui(self):
        self.entry_label = tk.Label(self, textvariable=self.logic.stream, anchor='e', height=3, background='white', cursor='xterm', font=('Helvetica',25))
        self.entry_label.grid(columnspan=5,row=0,sticky='NSEW')

        self.but0 = tk.Button(self,text='0', command=lambda: self.logic.insert('0'))
        self.but0.grid(column=2,row=4,sticky='NSEW')
        self.but1 = tk.Button(self,text='1', command=lambda: self.logic.insert('1'))
        self.but1.grid(column=1,row=3,sticky='NSEW')
        self.but2 = tk.Button(self,text='2', command=lambda: self.logic.insert('2'))
        self.but2.grid(column=2,row=3,sticky='NSEW')
        self.but3 = tk.Button(self,text='3', command=lambda: self.logic.insert('3'))
        self.but3.grid(column=3,row=3,sticky='NSEW')
        self.but4 = tk.Button(self,text='4', command=lambda: self.logic.insert('4'))
        self.but4.grid(column=1,row=2,sticky='NSEW')
        self.but5 = tk.Button(self,text='5', command=lambda: self.logic.insert('5'))
        self.but5.grid(column=2,row=2,sticky='NSEW')
        self.but6 = tk.Button(self,text='6', command=lambda: self.logic.insert('6'))
        self.but6.grid(column=3,row=2,sticky='NSEW')
        self.but7 = tk.Button(self,text='7', command=lambda: self.logic.insert('7'))
        self.but7.grid(column=1,row=1,sticky='NSEW')
        self.but8 = tk.Button(self,text='8', command=lambda: self.logic.insert('8'))
        self.but8.grid(column=2,row=1,sticky='NSEW')
        self.but9 = tk.Button(self,text='9', command=lambda: self.logic.insert('9'))
        self.but9.grid(column=3,row=1,sticky='NSEW')
        self.but_eq = tk.Button(self,text='=', command=self.logic.evaluate)
        self.but_eq.grid(column=3,row=4,sticky='NSEW')
        self.but_point = tk.Button(self,text='.', command=lambda: self.logic.insert('.'))
        self.but_point.grid(column=1,row=4,sticky='NSEW')
        self.but_add = tk.Button(self,text='+', command=lambda: self.logic.insert('+'))
        self.but_add.grid(row=1,column=4,sticky='NSEW')
        self.but_diff = tk.Button(self,text='-', command=lambda: self.logic.insert('-'))
        self.but_diff.grid(row=2,column=4,sticky='NSEW')
        self.but_molt = tk.Button(self, text='\u00d7', command=lambda: self.logic.insert('\u00d7'))
        self.but_molt.grid(row=3,column=4,sticky='NSEW')
        self.but_div = tk.Button(self, text='/', command=lambda: self.logic.insert('/'))
        self.but_div.grid(row=4,column=4,sticky='NSEW')

        self.bind('<Key>',Logic.callback)


    # def add_to_stream(self,char):
    #     self.logic.stream.set(self.logic.stream.get()+str(char))

    # def callback(self,event:tk.Event):

    #     self.logic.stream

    #     # dicto = {'a':self.button1.invoke,'b':self.button2.invoke}
    #     # if event.char in [*dicto]:
    #     #     dicto[event.char]()


if __name__ =='__main__':
    calc = Calc()
    calc.mainloop()