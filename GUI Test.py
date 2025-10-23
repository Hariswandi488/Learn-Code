import tkinter as tk

window = tk.Tk()
window.geometry("600x400")
window.title("Transisi Tombol Demo")

frame_main = tk.Frame(window, bg="#222")
frame_main.place(relwidth=1, relheight=1)

frame_next = tk.Frame(window, bg="#444")
frame_next.place(relwidth=1, relheight=1)
frame_next.place_forget()  # awalnya disembunyikan

btn = tk.Button(frame_main, text="Mulai", font=("Arial", 20), bg="#29a19c", fg="white")
btn.place(relx=0.5, rely=0.5, anchor="center")


def animate_button_down(y=0):
    # tombol turun sedikit demi sedikit
    if y < 150:
        btn.place_configure(rely=0.5 + y / 300)
        window.after(10, lambda: animate_button_down(y + 3))
    else:
        fade_out(btn, 1.0)


def fade_out(widget, alpha):
    # fade efek dengan ubah warna latar (simulasi opacity)
    if alpha > 0:
        col = int(34 + (255 - 34) * (1 - alpha))
        widget.config(bg=f"#{col:02x}{col:02x}{col:02x}")
        window.after(20, lambda: fade_out(widget, alpha - 0.1))
    else:
        widget.place_forget()
        show_next_gui()


def show_next_gui():
    # transisi ke GUI lain dengan animasi fade-in
    frame_next.place(relwidth=1, relheight=1)
    frame_next.attributes = {"alpha": 0}
    fade_in_frame(frame_next, 0)


def fade_in_frame(frame, alpha):
    if alpha < 1:
        color = int(68 + (255 - 68) * alpha)
        frame.config(bg=f"#{color:02x}{color:02x}{color:02x}")
        window.after(30, lambda: fade_in_frame(frame, alpha + 0.05))


btn.config(command=lambda: animate_button_down())

window.mainloop()
