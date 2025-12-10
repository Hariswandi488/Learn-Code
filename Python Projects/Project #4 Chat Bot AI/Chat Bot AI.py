import tkinter as tk

window  = tk.Tk()
window.geometry("720x1280")
window.title("Chat BOT AI")

frame = tk.Frame(window, bg="#2f2f2f")
frame.place(x=0, y=0, relheight=1, relwidth=1)

title_text = tk.Label(frame, font=("Arial", 25), fg="white", bg="#2f2f2f", text="Input Promt")
title_text.place(relx=0.5, rely=0.05, anchor="center")

entry = tk.Entry(frame, width=30, font=("Arial", 18))
entry.place(relx=0.5, rely=0.1, anchor="center")


window.mainloop()