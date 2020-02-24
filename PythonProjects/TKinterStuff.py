from tkinter import *

def pltw152():
    root = tk.Tk()
    canvas = tk.Canvas(root, height=600, width=600, relief=tk.RAISED, bg='white')
    canvas.grid()
    
    checkbox = canvas.create_rectangle(100, 200, 200, 300, dash=[1,4])
    check = canvas.create_line(100, 250, 150, 300, 220, 150, fill='red', width=20)
    message = canvas.create_text(380, 250, text='Try this!', font=('Arial', -100))
    shadow = canvas.create_oval(100,450,500,550, fill='#888888', outline='#888888')
    
    circles = []
    for r in range (10, 60, 10):
        circles.append(canvas.create_oval(300-r, 400-r, 300+r, 400+r, outline="red"))
    
    canopy = canvas.create_arc(0, 50, 600, 650, start=30, extent=120, width=50, style=tk.ARC)
    
    root.mainloop()

def pltw153():
    root = tk.Tk()
    radius_intvar = tk.IntVar()
    radius_intvar.set(100)
    
    x = 150
    y = 150
    
    def radius_changed(new_intval):
        r = radius_intvar.get()
        canvas.coords(circle_item, x-r, y-r, x+r, y+r)
        
    radius_slider = tk.Scale(root, from_=1, to=150, variable=radius_intvar, label="Radius", command=radius_changed)
    radius_slider.grid(row=1, column=0, sticky=tk.W)
    
    text = tk.Label(root, text="Drag slider \n to adjust \n circle.")
    text.grid(row=0, rowspan=2, column=1)
    
    canvas = tk.Canvas(root, width=300, height=300, background="#FFFFFF")
    canvas.grid(row=0, rowspan=2, column=1)
    
    r = radius_intvar.get()
    circle_item = canvas.create_oval(x-r, y-r, x+r, y+r, outline="#000000", fill="#00FFFF")
    
    root.mainloop()

def display_image():
    
    window = Tk()
    
    canvas = Canvas(window, width=300, height=300)
    canvas.pack()
    
    imgDirectoryPPM = "/Users/akkuma22/PythonProjects/soccerBall.ppm"
    
    img = PhotoImage(file=imgDirectoryPPM)
    
    label = Label(image=img)
    label.image = img
    label.pack()
    
    canvas.create_image(20,20, anchor=NW, image=img)
    
    mainloop()

display_image()
    
    