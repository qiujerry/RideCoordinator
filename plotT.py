import matplotlib as mpl
import tkinter as tk
import matplotlib as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg
from PIL import ImageTk,Image


def draw_figure(canvas, figure, loc=(0, 0)):
    """ Draw a matplotlib figure onto a Tk canvas

    loc: location of top-left corner of figure on canvas in pixels.
    Inspired by matplotlib source: lib/matplotlib/backends/backend_tkagg.py
    """
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)

    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)
    tkagg.backends.tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)

    return photo


class LineCoordsEntry(tk.Toplevel):
    def __init__(self, master):
        self.master = master
        super().__init__(self.master)
        self.label_x0 = tk.Label(self, text='x0:')
        self.label_x0.grid(row=0, column=0)
        self.entry_x0 = tk.Entry(self, width=6)
        self.entry_x0.grid(row=0, column=1)
        self.label_y0 = tk.Label(self, text='y0:')
        self.label_y0.grid(row=0, column=2)
        self.entry_y0 = tk.Entry(self, width=6)
        self.entry_y0.grid(row=0, column=3)

        self.label_x1 = tk.Label(self, text='x1:')
        self.label_x1.grid(row=1, column=0)
        self.entry_x1 = tk.Entry(self, width=6)
        self.entry_x1.grid(row=1, column=1)
        self.label_y1 = tk.Label(self, text='y1:')
        self.label_y1.grid(row=1, column=2)
        self.entry_y1 = tk.Entry(self, width=6)
        self.entry_y1.grid(row=1, column=3)

        self.quit_button = tk.Button(self, text='quit', command=self.destroy)
        self.quit_button.grid(row=2, column=0)

        self.validate_button = tk.Button(self, text='validate', command=self.send_data)
        self.validate_button.grid(row=2, column=1, columnspan=3)

    def send_data(self):
        p0 = float(self.entry_x0.get()), float(self.entry_y0.get())
        p1 = float(self.entry_x1.get()), float(self.entry_y1.get())
        self.master.retrieve_line_data(p0, p1)


class App(tk.Frame):
    def __init__(self, master, w=1000, h=700):
        self.master = master
        super().__init__(self.master)
        self.w = w
        self.h = h
        self.canvas = tk.Canvas(self.master, width=self.w, height=self.h)
        img = ImageTk.PhotoImage(Image.open("Cbus.png"))  
        self.canvas.create_image(800, 800, anchor='nw', image=img) 
        self.canvas.pack()

        self.enter_line_coordinates_button = tk.Button(self, text='make new line', command=self.spawn_entry_coordinates)
        self.enter_line_coordinates_button.pack()

        self.draw_lines_button = tk.Button(self, text='draw lines', command=self.draw_lines)
        self.draw_lines_button.pack()

        self.draw_overlay_button = tk.Button(self, text='draw overlaid axis', command=self.draw_overlay)
        self.draw_overlay_button.pack()

        self.erase_overlay_button = tk.Button(self, text='remove overlaid axis', command=self.erase_overlay)
        self.erase_overlay_button.pack()

        self.lines = []

    def spawn_entry_coordinates(self):
        LineCoordsEntry(self)

    def retrieve_line_data(self, p0, p1):
        self.lines.append((p0, p1))
        print(self.lines)

    def draw_lines(self):
        """draw the lines on the matplotlib canvas
        """
        fig = mpl.figure.Figure(figsize=(5, 5))
        ax = fig.add_axes([0, 0, 1, 1])
        for p0, p1 in self.lines:
            x0, y0, x1, y1 = *p0, *p1
            X = x0, x1
            Y = y0, y1
            print(X, Y)
            ax.plot(X, Y)

        self.fig_x, self.fig_y = 0, 0 #self.w, self.h
        self.fig_photo = draw_figure(self.canvas, fig, loc=(self.fig_x, self.fig_y))
        self.fig_w, self.fig_h = self.fig_photo.width(), self.fig_photo.height()

    def draw_overlay(self):
        """draw lines on the tkinter canvas, overlaid on the matplotlib canvas
        """
        self.canvas.create_line(0, self.h//2, self.w, self.h//2, tags=('overlay',))
        self.canvas.create_line(self.w//2, 0, self.w//2, self.h, tags=('overlay',))

    def erase_overlay(self):
        self.canvas.delete('overlay')


root = tk.Tk()
App(root).pack()
root.mainloop()