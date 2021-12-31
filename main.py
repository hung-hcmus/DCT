from os import path
import tkinter as tk
from tkinter import PhotoImage, filedialog as fd
from cmf_detect import DCT_Classic
from tkinter import ttk

root= tk.Tk()
canvas = tk.Canvas(root, width = 680, height = 480)
canvas.pack()

logo = PhotoImage(file='Triocate.png')
canvas.create_image(180, 0, image=logo, anchor='nw')

# Q_factor 
Q_label = tk.Label(root, text='Choose Quantized factor')
canvas.create_window(100, 120, window=Q_label)
n = tk.StringVar()
Q_factor_entry = ttk.Combobox(root, width = 17, textvariable = n)
# Adding combobox drop down list
Q_factor_entry['values'] = ('Q_50',
                     'Q_75',
                     'Q_90',
                     'Random',  
                     )
Q_factor_entry.current()
canvas.create_window(100, 150, window=Q_factor_entry)

# Threshold T
T_label = tk.Label(root, text='Enter Threshold')
canvas.create_window(80, 180, window=T_label)
T_entry = tk.Entry (root) 
canvas.create_window(100, 200, window=T_entry)

# Path
def getFileName():
    # Path
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',)

    # Q_factor
    Q_factor = Q_factor_entry.get()
    if Q_factor == 'Q_50':
        Q_factor = 0.5
    elif Q_factor == 'Q_75':
        Q_factor = 0.75
    elif Q_factor == 'Q_90':
        Q_factor = 0.9
    else:
        Q_factor = 0
    
    # Threshold 
    if T_entry.get() != "":
        threshold = float(T_entry.get())
        if threshold < 0: 
            threshold = 0
    else:
        threshold = 10
    
    DCT_Classic(Q_factor, threshold, filename)


Path_button = tk.Button(text='Choose an image', command=getFileName)
canvas.create_window(100, 250, window=Path_button)

root.mainloop()