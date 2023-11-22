import tkinter as tk

def draw_stick_figure(canvas, x):
    canvas.delete("all")

    # Head
    canvas.create_oval(75+x,50,125+x,100,outline="black")

    # Body
    canvas.create_line(100+x,100,100+x,200,fill="black")

    # Left arm
    canvas.create_line(100+x,180,50+x,150,fill="black")

    # Right arm
    canvas.create_line(100+x,180,150+x,150,fill="black")

    # Left foot
    canvas.create_line(100+x,200,50+x,250,fill="black")

    # Right foot
    canvas.create_line(100+x,200,150+x,250,fill="black")

def animate(canvas, x):
    draw_stick_figure(canvas, x)
    root.after(10, lambda: animate(canvas,x + 1))

def main():
    global root
    root=tk.Tk()
    root.title("Stick Figure")
    canvas=tk.Canvas(root,width=1000,height=300)
    canvas.pack()
    animate(canvas, 0)
    root.mainloop()

if __name__ == "__main__":
    main()