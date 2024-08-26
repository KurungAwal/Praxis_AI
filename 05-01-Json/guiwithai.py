import os
import tkinter as tk
from tkinter import messagebox
import json 

filename = 'C:\\Users\\Lenovo\\Documents\\Praxis_AI\\data.json'

if os.path.exists(filename):
    with open(filename, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {'name': '', 'kelas': ''}
else:
    data = {'name': '', 'kelas': ''}

# Pastikan data memiliki kunci 'name' dan 'kelas'
data.setdefault('name', '')
data.setdefault('kelas', '')

# Inisialisasi window
window = tk.Tk()

# Label dan Entry untuk nama
tk.Label(window, text='Masukkan nama anda').pack()
name_entry = tk.Entry(window)
name_entry.insert(tk.INSERT, data['name'])
name_entry.pack()

# Label dan Entry untuk kelas
tk.Label(window, text='Masukkan kelas anda').pack()
kelas_entry = tk.Entry(window)
kelas_entry.insert(tk.INSERT, data['kelas'])
kelas_entry.pack()

# Fungsi untuk menyimpan data
def save_command():
    name = name_entry.get()
    kelas = kelas_entry.get()
    data = {'name': name, 'kelas': kelas}
    
    # Menyimpan ke dalam file JSON
    with open(filename, 'w') as f:
        json.dump(data, f)
        
    messagebox.showinfo('Info', f'Halo {name}! Data Anda telah disimpan.')

# Tombol untuk menyimpan data
tk.Button(window, text='Simpan', command=save_command).pack()

# Menjalankan aplikasi
window.mainloop()
