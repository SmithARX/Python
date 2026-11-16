import tkinter
window = tkinter.Tk()
window.title("Program")
window.minsize(width="900", height="600")

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24) )
my_label.pack()

window.mainloop()
