from math import *
import tkinter as tk

class Logic():

    def __init__(self,root):
        super().__init__()
        self.stream = tk.StringVar(root, value='')
        self.TOK_list = []
        self.mode = 'D'
        self.flush = False
        self.sol = None
        self.default_dict = {
            '0' : 0,
            '1' : 1,
            '2' : 2,
            '3' : 3,
            '4' : 4,
            '5' : 5,
            '6' : 6,
            '7' : 7,
            '8' : 8,
            '9' : 9,
            '.' : '.',
            '+' : '+',
            '-' : '-',
            '\u00d7' : '*',
            '/' : '/'
        }

    def update_stream(self,chars,*args):
        self.stream.set(self.stream.get()+str(chars))

    def insert(self,TOK):
        if self.flush: self.stream.set('');self.TOK_list=[];self.flush=False
        if self.mode=='D':
            try:
                self.TOK_list.append(self.default_dict[str(TOK)])
                self.update_stream(TOK)
            except KeyError:
                pass

    def callback(self,*args):
        pass

    def evaluate(self):
        try:
            self.sol = eval(''.join(str(x) for x in self.TOK_list))
            self.stream.set(self.sol)
        except (SyntaxError, NameError, TypeError, ZeroDivisionError):
            self.stream.set('Errore')
            self.sol = None
            pass
        self.flush = True

        