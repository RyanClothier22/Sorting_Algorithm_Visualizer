from tkinter import ttk
from board import *
from tkinter.colorchooser import askcolor

root = Tk()

rect_var = StringVar()
time_var = StringVar()

header = ttk.Frame(root)
header.pack()
header.config(height=200,width=800)

header_2 = ttk.Frame(root)
header_2.pack(pady=10)
header_2.config(height=200,width=800)

header_3 = ttk.Frame(root)
header_3.pack()
header_3.config(height=200,width=800)

header_31 = ttk.Frame(header_3)
header_31.pack(side='left')
header_31.config(height=200,width=400)

header_32 = ttk.Frame(header_3)
header_32.pack(side='right', pady=5)
header_32.config(height=200,width=400)


body = ttk.Frame(root)
body.pack()
body.config(height=300, width=800, relief="solid")

canvas = Canvas(body, width = 600, height=600, bg='black')
canvas.pack()
b = Board(25, canvas, 600, 600)

def color_bg():
    colors = askcolor(title="Select Your Rectanlge Color!!!")
    canvas.configure(bg=colors[1])

def color_rect():
    colors = askcolor(title="Select Your Rectanlge Color!!!")
    b.rect_color = colors[1]
    b.remove_all()
    b.update_all()
    b.build()

def change_rect():
    try:
        int(rect_var.get())
    except:
        num_rects_entry.delete(0, END)
    else:
        b.rect_nums = int(rect_var.get())
        b.remove_all()
        b.update_all()
        b.build()


def change_time():
    try:
        float(time_var.get())
    except:
        time_delay_entry.delete(0, END)
    else:
        b.time_delay = float(time_var.get())


def sort():
    b.sort(clicked.get())


time_delay_butt = ttk.Button(header_2, text='Sorting Delay(<1)', command=change_time).pack(side='right')
time_delay_entry = ttk.Entry(header_2, textvariable=time_var)
time_delay_entry.pack(side='right')
time_delay_entry.insert(0, "0.05")

num_rects_entry = Entry(header_2, textvariable = rect_var)
num_rects_entry.pack(side='left')
num_rects_entry.insert(0, "25")

num_rects_sub_butt = ttk.Button(header_2, text='SUBMIT RECT #', command=change_rect)
num_rects_sub_butt.pack(side='left')

shuff_butt = ttk.Button(header_31, text="SHUFFLE", command=b.shuffle, padding=10)
shuff_butt.pack(side='left', padx= 5, pady=5)

sort_butt = ttk.Button(header_31, text="SORT", command=sort, padding=10)
sort_butt.pack(side='right', padx=5, pady=5)

ttk.Button(header, text="Change BG", command=color_bg, padding=10).pack(side="left", padx=5)
ttk.Button(header, text="Change Rect", command=color_rect, padding=10).pack(side="right", padx=5)

clicked = StringVar()

drop = ttk.OptionMenu(header_32, clicked, "SORTING TYPE", "Selection", "Insertion", "Bubble")
drop.pack(side="right")

mainloop()

