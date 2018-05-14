import tkinter as tk

window = tk.Tk()
window.title("test")
window.geometry("200x300")

var = tk.StringVar()
l = tk.Label(window, bg='green', textvariable=var, font=('Arial', 12), width=15, height=2)
l.pack()

isHited = False


def hit_me():
    global isHited
    if isHited == False:
        isHited = True
        var.set('not hited')
    else:
        isHited = False
        var.set('hited')

b = tk.Button(window, text='hit me', width=15, height=2, command=hit_me)
b.pack()

window.mainloop()
