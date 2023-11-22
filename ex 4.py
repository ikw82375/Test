import tkinter as tk

def draw_stick_figure(canvas):
    #head
    canvas.create_oval(75,50,125,100, outline="black")

    #body
    canvas.create_line(100,100,100,200, fill="black")

    #left arm
    canvas.create_line(100,180,50,150, fill="black")

    #right arm
    canvas.create_line(100,180,150,150, fill="black")

    #left foot
    canvas.create_line(100,200,50,250, fill="black")

    #right foot
    canvas.create_line(100,200,150,250, fill="black")

def main():
    root=tk.Tk()
    root.title("Stick Figure")
    canvas=tk.Canvas(root,width=200,height=300)
    canvas.pack()
    draw_stick_figure(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()