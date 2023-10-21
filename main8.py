from tkinter import*
def paint(event):
    x1,y1= event.x-1, event.y-1
    x2, y2 = event.x+1, event.y+1
    canvas.create_oval(x1,y1,x2,y2, fill=pen_color,outline=pen_color,width=pen_size)
def blue():
    global pen_color
    pen_color="blue"
def change_color(color):
    global pen_color
    pen_color=color
def size_up():
    global pen_size
    pen_size +=1

def size_down():
    global pen_size
    if pen_size>1:
        pen_size -=1


pen_color="black"
pen_size =1

window=Tk()
canvas=Canvas(window, width=700,height=700)
canvas.pack()
canvas.bind("<B1-Motion>", paint)



button_r = Button(window, text="빨강",width=5, bg="#dc143c",
                 command=lambda: change_color("#dc143c"), font=(12))
button_r.place(x=0, y=40)

button_o = Button(window, text="주황",width=5, bg="orange",
                 command=lambda: change_color("red"), font=(12))
button_o.place(x=0, y=80)

button_y = Button(window, text="노랑",width=5, bg="#ffd700",
                 command=lambda: change_color("#ffd700"), font=(12))
button_y.place(x=0, y=120)

button_g = Button(window, text="초록",width=5, bg="#228b22",
                 command=lambda: change_color("#228b22"), font=(12))
button_g.place(x=0, y=160)

button_b = Button(window, text="파랑",width=5, bg="#4169e1",
                 command=lambda: change_color("#4169e1"), font=(12))
button_b.place(x=0, y=200)

button_p = Button(window, text="보라",width=5, bg="#9932cc",
                 command=lambda: change_color("#9932cc"), font=(12))
button_p.place(x=0, y=240)

button_size_up=Button(window, text="굵게", command=size_up, width=5,font=(12))
button_size_up.place(x=0, y=280)

button_size_down=Button(window, text="가늘게", command=size_down, width=5,font=(12))
button_size_down.place(x=0, y=320)

button_e=Button(window, text="지우개", command=lambda:canvas.delete("all"), width=5,font=(12))
button_e.place(x=0, y=360)

message=Label(window, text="드래그해서 그림을 그려 보세요",font=(40)).pack()


window.mainloop()

