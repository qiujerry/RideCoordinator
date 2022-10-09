import tkinter as tk
from PIL import ImageTk, Image

def main():
    
    window = tk.Tk()

    window.rowconfigure(0, minsize=50)
    window.columnconfigure([0, 1, 2, 3], minsize=50)

    window.geometry("1000x1000")

    f = tk.Frame(window, width=800, height=500)
    f.pack()
    f.place(anchor='center', relx=0.5, rely=0.5)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("Cbus.png"))

    # Create a Label Widget to display the text or Image
    label = tk.Label(f, image = img)
    label.pack()


    window.mainloop()
if __name__ == "__main__": main()