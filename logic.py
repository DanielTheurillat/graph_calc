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
            '0' : '0',
            '1' : '1',
            '2' : '2',
            '3' : '3',
            '4' : '4',
            '5' : '5',
            '6' : '6',
            '7' : '7',
            '8' : '8',
            '9' : '9',
            '.' : '.',
            '+' : '+',
            '-' : '-',
            '\u00d7' : '*',
            '/' : '/',
            '*' : '*',
            's' : 'sin',
            '(' : '(',
            ')' : ')',
        }

        self.func_dict = {
            '\r' : self.evaluate,
            'Ans' : self.get_sol,
        }

    def get_sol(self):
        print(self.sol)
        self.update(self.sol)

    def look_dict(self,dict:dict,key):
        if dict.get(key) is not None:
            return dict[key]
        else: 
            return None

    def insert(self,chars,*args):
        if self.flush: self.stream.set('');self.TOK_list=[];self.flush=False
        if chars is not None:
            self.TOK_list.append(chars)
            self.stream.set(self.stream.get()+str(chars))

    def update(self,TOK):
        TOK = str(TOK)
        if self.mode=='D':
            self.insert(self.look_dict(self.default_dict,TOK))
            # if self.default_dict.get(TOK) is not None:
            #     self.insert(self.default_dict[TOK])

    def callback(self,event:tk.Event|str):
        if type(event) == tk.Event:
            print(f'Pulsante: {repr(event.char)}')
            val = self.look_dict(self.func_dict,event.char)
            if val is not None:
                val()
                return
            self.update(event.char)
        elif type(event) == str:
            val = self.look_dict(self.func_dict,event)
            if val is not None:
                val()
                return
            self.update(event)
        else: print('Errore di callback')

    def evaluate(self):
        try:
            self.sol = eval(''.join(str(x) for x in self.TOK_list))
            self.stream.set(self.sol)
            self.TOK_list=[self.sol]
        except (SyntaxError, NameError, TypeError, ZeroDivisionError):
            self.stream.set('Errore')
            self.sol = None
            self.flush = True