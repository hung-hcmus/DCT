from os import path
import tkinter as tk
from tkinter import PhotoImage, filedialog as fd
from cmf_detect import DCT_Classic
root= tk.Tk()
canvas = tk.Canvas(root, width = 680, height = 480)
canvas.pack()

logo = PhotoImage(file='Triocate.png')
canvas.create_image(180, 0, image=logo, anchor='nw')

# Block size
Block_size_entry_label = tk.Label(root, text='Enter block size')
canvas.create_window(80, 60, window=Block_size_entry_label)
Block_size_entry = tk.Entry (root) 
canvas.create_window(100, 80, window=Block_size_entry)

# Q_factor 
Q_label = tk.Label(root, text='Enter Quantized factor')
canvas.create_window(100, 120, window=Q_label)
Q_factor_entry = tk.Entry (root) 
canvas.create_window(100, 140, window=Q_factor_entry)

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
    print(filename)
    
    # Block size 
    if Block_size_entry.get() != "":
        block_size = int(Block_size_entry.get())
        if (block_size < 0):
            block_size = 0
    else:
        block_size = 0
    # Q_factor
    if Q_factor_entry.get() != "":
        Q_factor = float(Q_factor_entry.get())
        if Q_factor < 0:
            Q_factor = 0
        if Q_factor > 1:
            Q_factor = 1
    else:
        Q_factor = 0.75
    # Threshold 
    if T_entry.get() != "":
        threshold = float(T_entry.get())
        if threshold < 0: 
            threshold = 0
    else:
        threshold = 10
    
    DCT_Classic(block_size, Q_factor, threshold, filename)


Path_button = tk.Button(text='Choose an image', command=getFileName)
canvas.create_window(100, 250, window=Path_button)

root.mainloop()