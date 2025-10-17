import tkinter as tk
from logic import Logic

class Calc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('550x700')
        self.title('provaaaaaaaaaa')
        # self.stream = tk.StringVar(self, value='')
        self.logic = Logic(self)
        # self.grid_rowconfigure([0,1,2,3,4], weight=1)
        # self.grid_rowconfigure(5, weight=10)
        # self.grid_columnconfigure([0,1,2,3,4], weight=1)
        self.create_gui()
        self.create_number_frame(self.number_frame)

    def create_gui(self):
        self.columns = (0,1,2,3)
        self.grid_columnconfigure(self.columns, weight=1)
        self.number_frame = tk.Frame(self)
        self.number_frame.grid(row=1,column=self.columns[-1],sticky='NSEW')
        self.entry_label = tk.Label(self, textvariable=self.logic.stream, anchor='e', height=3, background='white', cursor='xterm', font=('Helvetica',25))
        self.entry_label.grid(columnspan=len(self.columns),row=0,sticky='NSEW')

    def create_number_frame(self,frame):
        self.but0 = tk.Button(frame,text='0', command=lambda: self.logic.callback('0'))
        self.but0.grid(column=1,row=3,sticky='NSEW')
        self.but1 = tk.Button(frame,text='1', command=lambda: self.logic.callback('1'))
        self.but1.grid(column=0,row=2,sticky='NSEW')
        self.but2 = tk.Button(frame,text='2', command=lambda: self.logic.callback('2'))
        self.but2.grid(column=1,row=2,sticky='NSEW')
        self.but3 = tk.Button(frame,text='3', command=lambda: self.logic.callback('3'))
        self.but3.grid(column=2,row=2,sticky='NSEW')
        self.but4 = tk.Button(frame,text='4', command=lambda: self.logic.callback('4'))
        self.but4.grid(column=0,row=1,sticky='NSEW')
        self.but5 = tk.Button(frame,text='5', command=lambda: self.logic.callback('5'))
        self.but5.grid(column=1,row=1,sticky='NSEW')
        self.but6 = tk.Button(frame,text='6', command=lambda: self.logic.callback('6'))
        self.but6.grid(column=2,row=1,sticky='NSEW')
        self.but7 = tk.Button(frame,text='7', command=lambda: self.logic.callback('7'))
        self.but7.grid(column=0,row=0,sticky='NSEW')
        self.but8 = tk.Button(frame,text='8', command=lambda: self.logic.callback('8'))
        self.but8.grid(column=1,row=0,sticky='NSEW')
        self.but9 = tk.Button(frame,text='9', command=lambda: self.logic.callback('9'))
        self.but9.grid(column=2,row=0,sticky='NSEW')
        self.but_eq = tk.Button(frame,text='=', command=self.logic.evaluate)
        self.but_eq.grid(column=2,row=3,sticky='NSEW')
        self.but_point = tk.Button(frame,text='.', command=lambda: self.logic.callback('.'))
        self.but_point.grid(column=0,row=3,sticky='NSEW')
        self.but_add = tk.Button(frame,text='+', command=lambda: self.logic.callback('+'))
        self.but_add.grid(row=0,column=3,sticky='NSEW')
        self.but_diff = tk.Button(frame,text='-', command=lambda: self.logic.callback('-'))
        self.but_diff.grid(row=1,column=3,sticky='NSEW')
        self.but_molt = tk.Button(frame, text='\u00d7', command=lambda: self.logic.callback('\u00d7'))
        self.but_molt.grid(row=2,column=3,sticky='NSEW')
        self.but_div = tk.Button(frame, text='/', command=lambda: self.logic.callback('/'))
        self.but_div.grid(row=3,column=3,sticky='NSEW')
        self.but_ans = tk.Button(frame,text='Ans', command=lambda: self.logic.callback('Ans'))
        self.but_ans.grid(row=3,column=4, sticky='NSEW')
        self.but_C = tk.Button(frame, text='C', command=lambda: self.logic.callback('Canc'))
        self.but_C.grid(row=0,column=4, sticky='NSEW')
        self.but_C_all = tk.Button(frame, text='CE', command=lambda: self.logic.callback('CE'))
        self.but_C_all.grid(row=1,column=4,sticky='NSEW')

        self.bind('<Key>',self.logic.callback)


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