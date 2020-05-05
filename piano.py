from tkinter import *
from playsound import playsound
import threading as th
import time

window =Tk()
window.resizable(0,0)
window.geometry("775x275")
window.iconbitmap("keys.ico")
window.title("SB Software: Piano")
window.configure(bg="#ffffff")
window.wm_attributes("-alpha",0.85)

def key_a1_hover_enter(e):
    key_a1.configure(bg="#78a5ff")
    key_a1_click(e)

def key_a1_hover_Leave(e):
    key_a1.configure(bg="#f0f0f0")

def key_a1_enter():
    key_a1.configure(bg="#78a5ff")

def key_a1_exit():
    time.sleep(0.3)
    key_a1.configure(bg="#f0f0f0")

def key_a1_click(e):
    a1 = th.Thread(target=lambda : playsound('piano\\176487__goup-1__piano-key-a4.wav')).start()
    enter_a1 = th.Thread(target=key_a1_enter).start()
    exit_a1 = th.Thread(target=key_a1_exit).start()


def key_b1_hover_enter(e):
    key_b1.configure(bg="#78a5ff")
    key_b1_click(e)

def key_b1_hover_Leave(e):
    key_b1.configure(bg="#f0f0f0")

def key_b1_enter():
    key_b1.configure(bg="#78a5ff")

def key_b1_exit():
    time.sleep(0.3)
    key_b1.configure(bg="#f0f0f0")

def key_b1_click(e):
    b1 = th.Thread(target=lambda : playsound('piano\\176480__goup-1__piano-key-b4.wav')).start()
    enter_b1 = th.Thread(target=key_b1_enter).start()
    exit_b1 = th.Thread(target=key_b1_exit).start()

def key_c1_hover_enter(e):
    key_c1.configure(bg="#78a5ff")
    key_c1_click(e)

def key_c1_hover_Leave(e):
    key_c1.configure(bg="#f0f0f0")

def key_c1_enter():
    key_c1.configure(bg="#78a5ff")

def key_c1_exit():
    time.sleep(0.3)
    key_c1.configure(bg="#f0f0f0")

def key_c1_click(e):
    c1 = th.Thread(target=lambda : playsound('piano\\176449__goup-1__piano-key-c4.wav')).start()
    enter_c1 = th.Thread(target=key_c1_enter).start()
    exit_c1 = th.Thread(target=key_c1_exit).start()

def key_d1_hover_enter(e):
    key_d1.configure(bg="#78a5ff")
    key_d1_click(e)

def key_d1_hover_Leave(e):
    key_d1.configure(bg="#f0f0f0")

def key_d1_enter():
    key_d1.configure(bg="#78a5ff")

def key_d1_exit():
    time.sleep(0.3)
    key_d1.configure(bg="#f0f0f0")

def key_d1_click(e):
    d1 = th.Thread(target=lambda : playsound('piano\\176516__goup-1__piano-key-d4.wav')).start()
    enter_d1 = th.Thread(target=key_d1_enter).start()
    exit_d1 = th.Thread(target=key_d1_exit).start()

def key_e1_hover_enter(e):
    key_e1.configure(bg="#78a5ff")
    key_e1_click(e)

def key_e1_hover_Leave(e):
    key_e1.configure(bg="#f0f0f0")

def key_e1_enter():
    key_e1.configure(bg="#78a5ff")

def key_e1_exit():
    time.sleep(0.3)
    key_e1.configure(bg="#f0f0f0")

def key_e1_click(e):
    e1 = th.Thread(target=lambda : playsound('piano\\176526__goup-1__piano-key-e4.wav')).start()
    enter_e1 = th.Thread(target=key_e1_enter).start()
    exit_e1 = th.Thread(target=key_e1_exit).start()

def key_f1_hover_enter(e):
    key_f1.configure(bg="#78a5ff")
    key_f1_click(e)

def key_f1_hover_Leave(e):
    key_f1.configure(bg="#f0f0f0")

def key_f1_enter():
    key_f1.configure(bg="#78a5ff")


def key_f1_exit():
    time.sleep(0.3)
    key_f1.configure(bg="#f0f0f0")

def key_f1_click(e):
    f1 = th.Thread(target=lambda : playsound('piano\\176491__goup-1__piano-key-f4.wav')).start()
    enter_f1 = th.Thread(target=key_f1_enter).start()
    exit_f1 = th.Thread(target=key_f1_exit).start()

def key_g1_hover_enter(e):
    key_g1.configure(bg="#78a5ff")
    key_g1_click(e)

def key_g1_hover_Leave(e):
    key_g1.configure(bg="#f0f0f0")

def key_g1_enter():
    key_g1.configure(bg="#78a5ff")


def key_g1_exit():
    time.sleep(0.3)
    key_g1.configure(bg="#f0f0f0")

def key_g1_click(e):
    g1 = th.Thread(target=lambda : playsound('piano\\176502__goup-1__piano-key-g4.wav')).start()
    enter_g1 = th.Thread(target=key_g1_enter).start()
    exit_g1 = th.Thread(target=key_g1_exit).start()


key_a1 = Button(window, text="a4", bg="#f0f0f0", padx=18, pady=125, bd=0, activebackground="#4885ef")
key_a1.grid(row=3, column=5, pady=1, padx=1)
key_b1 = Button(window, text="b4", bg="#f0f0f0", padx=18, pady=125, bd=0, activebackground="#4885ef")
key_b1.grid(row=3, column=6, pady=1, padx=1)
key_c1 = Button(window, text="c4", bg="#f0f0f0", padx=18, pady=125, bd=0, activebackground="#4885ef")
key_c1.grid(row=3, column=0, pady=1, padx=1)
key_d1 = Button(window, text="d4", bg="#f0f0f0", padx=18, pady=125, bd=0, activebackground="#4885ef")
key_d1.grid(row=3, column=1, pady=1, padx=1)
key_e1 = Button(window, text="e4", bg="#f0f0f0", padx=18, pady=125, bd=0, activebackground="#4885ef")
key_e1.grid(row=3, column=2, pady=1, padx=1)
key_f1 = Button(window, text="f4", bg="#f0f0f0", padx=18, pady=125, bd=0, activebackground="#4885ef")
key_f1.grid(row=3, column=3, pady=1, padx=1)
key_g1 = Button(window, text="g4", bg="#f0f0f0", padx=18, pady=125, bd=0, activebackground="#4885ef")
key_g1.grid(row=3, column=4, pady=1, padx=1)


key_a1.bind("<Enter>",key_a1_hover_enter)
key_a1.bind("<Leave>",key_a1_hover_Leave)
key_a1.bind("<Button-1>",key_a1_click)
window.bind_all("h", key_a1_click)

key_b1.bind("<Enter>",key_b1_hover_enter)
key_b1.bind("<Leave>",key_b1_hover_Leave)
key_b1.bind("<Button-1>",key_b1_click)
window.bind_all("j", key_b1_click)

key_c1.bind("<Leave>",key_c1_hover_Leave)
key_c1.bind("<Enter>",key_c1_hover_enter)
key_c1.bind("<Button-1>",key_c1_click)
window.bind_all("a", key_c1_click)

key_d1.bind("<Enter>",key_d1_hover_enter)
key_d1.bind("<Leave>",key_d1_hover_Leave)
key_d1.bind("<Button-1>",key_d1_click)
window.bind_all("s", key_d1_click)

key_e1.bind("<Enter>",key_e1_hover_enter)
key_e1.bind("<Leave>",key_e1_hover_Leave)
key_e1.bind("<Button-1>",key_e1_click)
window.bind_all("d", key_e1_click)

key_f1.bind("<Leave>",key_f1_hover_Leave)
key_f1.bind("<Enter>",key_f1_hover_enter)
key_f1.bind("<Button-1>",key_f1_click)
window.bind_all("f", key_f1_click)

key_g1.bind("<Enter>",key_g1_hover_enter)
key_g1.bind("<Leave>",key_g1_hover_Leave)
key_g1.bind("<Button-1>",key_g1_click)
window.bind_all("g", key_g1_click)



















def key_a2_hover_enter(e):
    key_a2.configure(bg="#78a5ff")
    key_a2_click(e)


def key_a2_hover_Leave(e):
    key_a2.configure(bg="#f0f0f0")

def key_a2_enter():
    key_a2.configure(bg="#78a5ff")

def key_a2_exit():
    time.sleep(0.3)
    key_a2.configure(bg="#f0f0f0")

def key_a2_click(e):
    a2 = th.Thread(target=lambda: playsound('piano\\176486__goup-1__piano-key-a5.wav')).start()
    enter_a2 = th.Thread(target=key_a2_enter).start()
    exit_a2 = th.Thread(target=key_a2_exit).start()


def key_b2_hover_enter(e):
    key_b2.configure(bg="#78a5ff")
    key_b2_click(e)


def key_b2_hover_Leave(e):
    key_b2.configure(bg="#f0f0f0")

def key_b2_enter():
    key_b2.configure(bg="#78a5ff")

def key_b2_exit():
    time.sleep(0.3)
    key_b2.configure(bg="#f0f0f0")

def key_b2_click(e):
    b2 = th.Thread(target=lambda: playsound('piano\\176479__goup-1__piano-key-b5.wav')).start()
    enter_b2 = th.Thread(target=key_b2_enter).start()
    exit_b2 = th.Thread(target=key_b2_exit).start()

def key_c2_hover_enter(e):
    key_c2.configure(bg="#78a5ff")
    key_c2_click(e)

def key_c2_hover_Leave(e):
    key_c2.configure(bg="#f0f0f0")

def key_c2_enter():
    key_c2.configure(bg="#78a5ff")

def key_c2_exit():
    time.sleep(0.3)
    key_c2.configure(bg="#f0f0f0")

def key_c2_click(e):
    c2 = th.Thread(target=lambda: playsound('piano\\176442__goup-1__piano-note-c5.wav')).start()
    enter_c2 = th.Thread(target=key_c2_enter).start()
    exit_c2 = th.Thread(target=key_c2_exit).start()

def key_d2_hover_enter(e):
    key_d2.configure(bg="#78a5ff")
    key_d2_click(e)

def key_d2_hover_Leave(e):
    key_d2.configure(bg="#f0f0f0")

def key_d2_enter():
    key_d2.configure(bg="#78a5ff")

def key_d2_exit():
    time.sleep(0.3)
    key_d2.configure(bg="#f0f0f0")

def key_d2_click(e):
    d2 = th.Thread(target=lambda: playsound('piano\\176517__goup-1__piano-key-d5.wav')).start()
    enter_d2 = th.Thread(target=key_d2_enter).start()
    exit_d2 = th.Thread(target=key_d2_exit).start()

def key_e2_hover_enter(e):
    key_e2.configure(bg="#78a5ff")
    key_e2_click(e)

def key_e2_hover_Leave(e):
    key_e2.configure(bg="#f0f0f0")

def key_e2_enter():
    key_e2.configure(bg="#78a5ff")

def key_e2_exit():
    time.sleep(0.3)
    key_e2.configure(bg="#f0f0f0")

def key_e2_click(e):
    e2 = th.Thread(target=lambda: playsound('piano\\176525__goup-1__piano-key-e5.wav')).start()
    enter_e2 = th.Thread(target=key_e2_enter).start()
    exit_e2 = th.Thread(target=key_e2_exit).start()


def key_f2_hover_enter(e):
    key_f2.configure(bg="#78a5ff")
    key_f2_click(e)

def key_f2_hover_Leave(e):
    key_f2.configure(bg="#f0f0f0")

def key_f2_enter():
    key_f2.configure(bg="#78a5ff")

def key_f2_exit():
    time.sleep(0.3)
    key_f2.configure(bg="#f0f0f0")

def key_f2_click(e):
    f2 = th.Thread(target=lambda: playsound('piano\\176492__goup-1__piano-key-f5.wav')).start()
    enter_f2 = th.Thread(target=key_f2_enter).start()
    exit_f2 = th.Thread(target=key_f2_exit).start()


def key_g2_hover_enter(e):
    key_g2.configure(bg="#78a5ff")
    key_g2_click(e)

def key_g2_hover_Leave(e):
    key_g2.configure(bg="#f0f0f0")

def key_g2_enter():
    key_g2.configure(bg="#78a5ff")

def key_g2_exit():
    time.sleep(0.3)
    key_g2.configure(bg="#f0f0f0")

def key_g2_click(e):
    g2 = th.Thread(target=lambda: playsound('piano\\176467__goup-1__piano-key-g5.wav')).start()
    enter_g2 = th.Thread(target=key_g2_enter).start()
    exit_g2 = th.Thread(target=key_g2_exit).start()



key_c2 = Button(window, text="c5", bg="#f0f0f0", padx=18, pady=125, bd=0, activebackground="#4885ef")
key_c2.grid(row=3, column=8, pady=1, padx=1)
key_a2 = Button(window, text="a5", bg="#f0f0f0", padx=18, pady=125, bd=0, activebackground="#4885ef")
key_a2.grid(row=3, column=13, pady=1, padx=1)
key_b2 = Button(window, text="b5", bg="#f0f0f0", padx=18, pady=125, bd=0, activebackground="#4885ef")
key_b2.grid(row=3, column=14, pady=1, padx=1)
key_d2 = Button(window, text="d5", bg="#f0f0f0", padx=18, pady=125, bd=0, activebackground="#4885ef")
key_d2.grid(row=3, column=9, pady=1, padx=1)
key_e2 = Button(window, text="e5", bg="#f0f0f0", padx=18, pady=125, bd=0, activebackground="#4885ef")
key_e2.grid(row=3, column=10, pady=1, padx=1)
key_f2 = Button(window, text="f5", bg="#f0f0f0", padx=18, pady=125, bd=0, activebackground="#4885ef")
key_f2.grid(row=3, column=11, pady=1, padx=1)
key_g2 = Button(window, text="g5", bg="#f0f0f0", padx=18, pady=125, bd=0, activebackground="#4885ef")
key_g2.grid(row=3, column=12, pady=1, padx=1)


key_a2.bind("<Enter>",key_a2_hover_enter)
key_a2.bind("<Leave>",key_a2_hover_Leave)
key_a2.bind("<Button-1>",key_a2_click)
window.bind_all("v", key_a2_click)

key_b2.bind("<Enter>",key_b2_hover_enter)
key_b2.bind("<Leave>",key_b2_hover_Leave)
key_b2.bind("<Button-1>",key_b2_click)
window.bind_all("b", key_b2_click)

key_c2.bind("<Leave>",key_c2_hover_Leave)
key_c2.bind("<Enter>",key_c2_hover_enter)
key_c2.bind("<Button-1>",key_c2_click)
window.bind_all("k", key_c2_click)

key_d2.bind("<Enter>",key_d2_hover_enter)
key_d2.bind("<Leave>",key_d2_hover_Leave)
key_d2.bind("<Button-1>",key_d2_click)
window.bind_all("l", key_d2_click)

key_e2.bind("<Enter>",key_e2_hover_enter)
key_e2.bind("<Leave>",key_e2_hover_Leave)
key_e2.bind("<Button-1>",key_e2_click)
window.bind_all("z", key_e2_click)

key_f2.bind("<Leave>",key_f2_hover_Leave)
key_f2.bind("<Enter>",key_f2_hover_enter)
key_f2.bind("<Button-1>",key_f2_click)
window.bind_all("x", key_f2_click)

key_g2.bind("<Enter>",key_g2_hover_enter)
key_g2.bind("<Leave>",key_g2_hover_Leave)
key_g2.bind("<Button-1>",key_g2_click)
window.bind_all("c", key_g2_click)





window.mainloop()
