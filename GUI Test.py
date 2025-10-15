import tkinter as tk

window = tk.Tk()
window.title("GUI TESTER")
window.geometry("1280x720")

label = tk.Label(window, text="Testing Text Hello World")
label.pack(pady=20)

def button_onclick():
    label.config(text="Tombol Di Klik")

button = tk.Button(window, text="Tekan Aku", command=button_onclick)
button.pack(pady=10)

window.mainloop()