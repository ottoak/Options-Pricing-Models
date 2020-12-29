# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 15:35:28 2020

@author: Alex
"""
import options.Binomial_Models as Binomial_Model
import tkinter as tk
from tkinter.ttk import Combobox

# GUI Window setup
window = tk.Tk()

window.title("Option Pricing")
window.geometry('350x200')

# Drop down box to select b/w american/european and put/call
Am_or_Eu = Combobox(window)
Am_or_Eu['values'] = ("American", "European", "Text")
Am_or_Eu.current(0)
Am_or_Eu.grid(column=0, row=0)

C_or_P = Combobox(window)
C_or_P['values'] = ("Call", "Put", "Text")
C_or_P.current(0)
C_or_P.grid(column=1, row=0)

# Entry boxes and labels
Out = tk.Label(window, text="Option price is")
S0_lbl = tk.Label(window, text="Enter initial stock price:")
K_lbl = tk.Label(window, text="Enter strike price:")
R_lbl = tk.Label(window, text="Enter risk free rate:")
u_lbl = tk.Label(window, text="Enter u:")
N_lbl = tk.Label(window, text="Enter number of periods:")

S0_lbl.grid(column=0, row=1)
K_lbl.grid(column=0, row=2)
R_lbl.grid(column=0, row = 3)
u_lbl.grid(column=0, row = 4)
N_lbl.grid(column=0, row = 5)
Out.grid(column=0, row=7)

S0_in = tk.Entry(window,width=10)
K_in = tk.Entry(window,width=10)
u_in = tk.Entry(window,width=10)
R_in = tk.Entry(window,width=10)
N_in = tk.Entry(window,width=10)

S0_in.grid(column=1, row=1)
K_in.grid(column=1, row=2)
R_in.grid(column=1, row=3)
u_in.grid(column=1, row=4)
N_in.grid(column=1, row=5)

# Function to perform the calculation
def clicked():
    S0 = float(S0_in.get())
    K = float(K_in.get())
    R = float(R_in.get())
    u = float(u_in.get())
    N = int(N_in.get())
    
    if (C_or_P.get()=="Call") & (Am_or_Eu.get()=="American"):
        Out.configure(text = "Option price is {}$".format(Binomial_Model.American(u, R, N, S0, K, "call").Option_Price))
    if (C_or_P.get()=="Put") & (Am_or_Eu.get()=="American"):
        Out.configure(text = "Option price is {}$".format(Binomial_Model.American(u, R, N, S0, K, "put").Option_Price))
    if (C_or_P.get()=="Call") & (Am_or_Eu.get()=="European"):
        Out.configure(text = "Option price is {}$".format(Binomial_Model.European(u, R, N, S0, K, "call").Option_Price))
    if (C_or_P.get()=="Put") & (Am_or_Eu.get()=="European"):
        Out.configure(text = "Option price is {}$".format(Binomial_Model.American(u, R, N, S0, K, "call").Option_Price))

# Button to perform the calculation
btn = tk.Button(window, text="Click Me", command=clicked)

btn.grid(column=0, row=6)

window.mainloop()