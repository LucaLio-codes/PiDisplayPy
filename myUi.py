# -*- coding: utf-8 -*-
import pathlib
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "myui.ui"


class MyUiWidget(tk.Frame):
    def __init__(self, master=None, **kw):
        super(MyUiWidget, self).__init__(master, bg='black', **kw)
        self.menu = tk.Frame(self, bg='black')
        self.scanPng = tk.Button(self.menu, bg='black', fg="white")
        self.scanPng.configure(text='scan png')
        self.scanPng.pack(pady='20', side='top')
        self.scanPDF = tk.Button(self.menu, bg='black', fg="white")
        self.scanPDF.configure(text='scan pdf')
        self.scanPDF.pack(pady='20', side='top')
        self.exitButton = tk.Button(self.menu)
        self.exitButton.configure(text='close', bg='black', fg="white")
        self.exitButton.pack(pady='20', side='bottom')
        self.menu.configure(height='200', width='200')
        self.menu.pack(fill='y', ipadx='20', side='left')
        self.menu.bind('<1>', self.callback, add='+')
        self.clock = tk.Frame(self,bg='black')
        self.currentWeather = tk.Frame(self.clock, bg='black')
        self.frame12 = tk.Frame(self.currentWeather,bg='black')
        self.frame14 = tk.Frame(self.frame12,bg='black')
        self.frame1 = tk.Frame(self.frame12)
        self.currentDegreeLabel = tk.Label(self.frame14,bg='black', fg="white")
        # self.currentDegree = tk.IntVar(value="°C")
        self.currentDegreeLabel.configure(font='{arial Black} 36 {bold}', text='°C')
        self.currentDegreeLabel.pack(anchor='w', fill='y', side='top')
        self.currentFeelLabel = tk.Label(self.frame14,bg='black', fg="white")
        # self.currentFeel = tk.IntVar(value="Feels Like 20°C")
        self.currentFeelLabel.configure(font='{arial black} 12 {}', text='Feels Like 20°C', pady=15)
        self.currentFeelLabel.pack(expand='true', side='bottom')
        self.frame1.configure(height='200', width='200', bg='black')
        self.frame1.pack(expand='true', side='left')
        self.frame14.configure(height='200', width='150')
        self.frame14.pack(side='right')
        self.frame14.pack_propagate(0)
        self.weatherimg = tk.Label(self.frame1,bg='black', fg="white")
        self.weatherdescr = tk.Label(self.frame1, bg='black', fg='white',font='{arial black} 12 {bold}', pady=10)
        self.weatherimg.pack(side='top')
        self.weatherdescr.pack(side='bottom')
        self.frame12.configure(height='150', width='300')
        self.frame12.pack(expand='false', side='top')
        self.frame12.pack_propagate(0)
        self.currentWeather.configure(height='200', width='300')
        self.currentWeather.pack(anchor='center', expand='true', side='left')
        self.futureWeather = tk.Frame(self.clock, bg='black')
        self.maxLabel = tk.Label(self.futureWeather,bg='black', fg="white")
        self.maxLabel.configure(font='{arial black} 12 {bold}', text='Max')
        self.maxLabel.grid(column='0', row='0')
        self.minLabel = tk.Label(self.futureWeather, bg='black', fg="white")
        self.minLabel.configure(font='{arial black} 12 {bold}', text='Min')
        self.minLabel.grid(column='0', row='1')
        self.riseLabel = tk.Label(self.futureWeather, bg='black', fg="white")
        self.riseLabel.configure(font='{arial black} 12 {bold}', text='Sunset')
        self.riseLabel.grid(column='0', row='2')
        self.setLabel = tk.Label(self.futureWeather, bg='black', fg="white")
        self.setLabel.configure(font='{arial black} 12 {bold}', text='Sunrise')
        self.setLabel.grid(column='0', row='3')
        self.maxLabelVal = tk.Label(self.futureWeather, bg='black', fg="white")
        # self.maxVal = tk.IntVar(value='')
        self.maxLabelVal.configure(font='{arial black} 12 {bold}')
        self.maxLabelVal.grid(column='1', row='0')
        self.minLabelVal = tk.Label(self.futureWeather, bg='black', fg="white")
        # self.minVal = tk.IntVar(value='')
        self.minLabelVal.configure(font='{arial black} 12 {bold}')
        self.minLabelVal.grid(column='1', row='1')
        self.sunsetLabelVal = tk.Label(self.futureWeather, bg='black', fg="white")
        # self.sunsetVal = tk.IntVar(value='')
        self.sunsetLabelVal.configure(font='{arial black} 12 {bold}')
        self.sunsetLabelVal.grid(column='1', row='2')
        self.sunriseLabelVal = tk.Label(self.futureWeather, bg='black', fg="white")
        # self.sunriseVal = tk.IntVar(value='')
        self.sunriseLabelVal.configure(font='{arial black} 12 {bold}')
        self.sunriseLabelVal.grid(column='1', row='3')
        self.futureWeather.configure(height='200', width='300')
        self.futureWeather.pack(anchor='center', expand='true', fill='x', side='right')
        self.futureWeather.pack_propagate(0)
        self.clock.configure(height='200', width='200')
        self.clock.pack(anchor='center', expand='true', fill='both', padx='5', pady='5', side='bottom')
        self.weather = tk.Frame(self, bg='black')
        self.timeLabel = tk.Label(self.weather, bg='black', fg="white")
        self.timeLabel.configure(font='{Arial Black} 48 {}', foreground='white', text='<time>')
        self.timeLabel.pack(anchor='center', expand='true', pady='0', side='top')
        self.dateLabel = tk.Label(self.weather, bg='black')
        self.dateLabel.configure(font='{arial black} 12 {}', foreground='white', text='<date>')
        self.dateLabel.pack(anchor='center', expand='true', pady='0', side='bottom')
        self.weather.configure(height='200', width='300')
        self.weather.pack(anchor='center', expand='true', fill='both', padx='5', pady='5', side='top')
        self.weather.pack_propagate(0)

    def callback(self, event=None):
        pass


class Preview(ttk.Frame):
    def __init__(self, master=None, image=None, **kw):
        super(Preview, self).__init__(master, **kw)
        self.canvas1 = ScrollableImage(self, image=image)
        self.canvas1.configure(confine='false')
        self.canvas1.pack(anchor='center', fill='both', side='left')
        self.button1 = ttk.Button(self)
        self.button1.configure(text='close')
        self.button1.pack(pady='20', padx='10', side='bottom')


class ScrollableImage(tk.Frame):
    def __init__(self, master=None, **kw):
        self.image = kw.pop('image', None)
        sw = kw.pop('scrollbarwidth', 10)
        super(ScrollableImage, self).__init__(master=master, **kw)
        self.cnvs = tk.Canvas(self, highlightthickness=0, **kw)
        self.cnvs.create_image(0, 0, anchor='nw', image=self.image)
        # Vertical and Horizontal scrollbars
        self.v_scroll = tk.Scrollbar(self, orient='vertical', width=sw)
        self.h_scroll = tk.Scrollbar(self, orient='horizontal', width=sw)
        # Grid and configure weight.
        self.cnvs.grid(row=0, column=0,  sticky='nsew')
        self.h_scroll.grid(row=1, column=0, sticky='ew')
        self.v_scroll.grid(row=0, column=1, sticky='ns')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        # Set the scrollbars to the canvas
        self.cnvs.config(xscrollcommand=self.h_scroll.set,
                           yscrollcommand=self.v_scroll.set)
        # Set canvas view to the scrollbars
        self.v_scroll.config(command=self.cnvs.yview)
        self.h_scroll.config(command=self.cnvs.xview)
        # Assign the region to be scrolled
        self.cnvs.config(scrollregion=self.cnvs.bbox('all'))
        self.cnvs.bind_class(self.cnvs, "<MouseWheel>", self.mouse_scroll)

    def mouse_scroll(self, evt):
        if evt.state == 0 :
            self.cnvs.yview_scroll(-1*(evt.delta), 'units') # For MacOS
            self.cnvs.yview_scroll(int(-1*(evt.delta/120)), 'units') # For windows
        if evt.state == 1:
            self.cnvs.xview_scroll(-1*(evt.delta), 'units') # For MacOS
            self.cnvs.xview_scroll(int(-1*(evt.delta/120)), 'units') # For windows

if __name__ == '__main__':
    root = tk.Tk()
    widget = MyUiWidget(root)
    widget.pack(expand=True, fill='both')
    root.mainloop()

