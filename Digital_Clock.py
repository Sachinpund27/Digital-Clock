import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime('Time - %H:%M:%S %p \n Date - %D')
    label.config(text=string)
    label.after(1000,time)

label = tk.Label(root, font=('Futura', 80, 'bold'), background='Black', foreground='purple')
label.pack(anchor='center')

time()
 
root.mainloop()