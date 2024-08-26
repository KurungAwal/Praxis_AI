import os
import tkinter as tk
from tkinter import messagebox
import json 

filename = 'C:\\Users\\Lenovo\\Documents\\Praxis_AI\\data.json'

if os.path.exists(filename):

    with open(filename, 'r') as f:
        data = json.load(f)

else:

    data = {
        'name': '', 
        'kelas': ''
    }

window = tk.Tk()

tk.Label(window, text='Masukkan nama anda').pack()
name_entry = tk.Entry(window)
name_entry.insert(tk.INSERT, data['name'])
name_entry.pack()

tk.Label(window, text='Masukkan kelas anda').pack()
kelas_entry = tk.Entry(window)
kelas_entry.insert(tk.INSERT, data['kelas'])
kelas_entry.pack()


def save_command():
    name = name_entry.get()
    kelas = kelas_entry.get()
    data = {'name' : name, 'kelas' : kelas}
    with open('data.json', 'w') as f:
        json.dump(data, f)
    messagebox.showinfo('Info', f'Halo {name}!')

tk.Button(window, text='Simpan', command=save_command).pack()

window.mainloop()

# messagebox.showinfo('Info', 'Dek Mimi')